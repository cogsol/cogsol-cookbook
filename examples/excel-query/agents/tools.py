from cogsol.tools import BaseTool, tool_params


class QueryExcelAttachment(BaseTool):
    """Script tool that queries an Excel file attached to the chat using pandas."""

    name = "analyze_excel"
    description = (
        "Use this tool to answer ANY question about an Excel (.xlsx) file "
        "attached to the conversation. You MUST call this tool whenever the "
        "user asks about attached data. Start with 'describe' to understand "
        "the structure, then use 'filter', 'aggregate', or 'lookup'."
    )
    show_tool_message = True

    @tool_params(
        operation={
            "description": (
                "Operation to perform: 'describe', 'filter', "
                "'aggregate', or 'lookup'."
            ),
            "type": "string",
            "required": True,
        },
        sheet={
            "description": (
                "Worksheet name to read (e.g. 'Sheet1'). "
                "If not provided, reads the first sheet."
            ),
            "type": "string",
            "required": False,
        },
        column={
            "description": (
                "Column name to operate on. Required for 'filter' and "
                "'aggregate' operations."
            ),
            "type": "string",
            "required": False,
        },
        value={
            "description": (
                "Value to filter by or look up. Required for 'filter' "
                "and 'lookup' operations."
            ),
            "type": "string",
            "required": False,
        },
        agg_function={
            "description": (
                "Aggregation function: 'sum', 'mean', 'count', 'min', or "
                "'max'. Required for 'aggregate' operation."
            ),
            "type": "string",
            "required": False,
        },
        group_by={
            "description": (
                "Column name to group by before aggregating. "
                "Optional, only used with 'aggregate' operation."
            ),
            "type": "string",
            "required": False,
        },
    )
    def run(
        self,
        operation="",
        sheet="",
        column="",
        value="",
        agg_function="",
        group_by="",
        chat=None,
        data=None,
        secrets=None,
        log=None,
    ):
        # NOTE: On the platform, this code runs as a top-level script.
        # Imports must be at top-level (not inside functions) when no
        # functions are defined. The framework transforms this method
        # into platform script format automatically.
        #
        # Available platform variables: chat, params, data, secrets, log
        # Attachments are accessed via: chat.messages → message.attachments
        # File bytes via: attachment.load_file()
        import io
        import pandas as pd

        log.append("Starting analyze_excel")

        try:
            last_msg = (
                chat.messages.filter(role="user")
                .order_by("msg_num")
                .last()
            )
            if not last_msg:
                return "No user message found."

            atts = list(last_msg.attachments.all())
            if not atts:
                return (
                    "No file attached. "
                    "Please upload an Excel file and try again."
                )

            attachment = atts[0]
            log.append(f"File: {attachment.original_file_name}")

            file_bytes = attachment.load_file()
            log.append(f"Loaded {len(file_bytes)} bytes")

        except Exception as e:
            log.append(f"Attachment error: {str(e)}")
            return f"Could not read the attached file: {str(e)}"

        try:
            df = pd.read_excel(
                io.BytesIO(file_bytes),
                sheet_name=sheet if sheet else 0,
            )
            log.append(f"Parsed {len(df)} rows, {len(df.columns)} columns")

        except Exception as e:
            log.append(f"Parse error: {str(e)}")
            return f"Could not parse the Excel file: {str(e)}"

        operation = operation.strip().lower()

        if operation == "describe":
            return self._describe(df, log)
        elif operation == "filter":
            return self._filter(df, column, value, log)
        elif operation == "aggregate":
            return self._aggregate(df, column, agg_function, group_by, log)
        elif operation == "lookup":
            return self._lookup(df, value, log)
        else:
            return (
                f"Unknown operation '{operation}'. "
                "Use 'describe', 'filter', 'aggregate', or 'lookup'."
            )

    def _describe(self, df, log):
        """Return dataset overview: columns, types, row count, and a sample."""
        col_info = []
        for col in df.columns:
            non_null = df[col].notna().sum()
            col_info.append(
                f"- **{col}** ({df[col].dtype}): {non_null} non-null"
            )

        sample = df.head(5).to_csv(index=False)
        log.append("Describe completed")

        return (
            f"**Rows:** {len(df)} | **Columns:** {len(df.columns)}\n\n"
            f"**Column details:**\n"
            + "\n".join(col_info)
            + f"\n\n**First 5 rows:**\n```\n{sample}```"
        )

    def _filter(self, df, column, value, log):
        """Return rows where column matches value."""
        import pandas as pd

        if not column or not value:
            return "Both 'column' and 'value' are required for filter."

        if column not in df.columns:
            return (
                f"Column '{column}' not found. "
                f"Available: {', '.join(str(c) for c in df.columns)}"
            )

        if pd.api.types.is_numeric_dtype(df[column].dtype):
            try:
                mask = df[column] == float(value)
            except ValueError:
                mask = (
                    df[column]
                    .astype(str)
                    .str.contains(value, case=False, na=False)
                )
        else:
            mask = (
                df[column]
                .astype(str)
                .str.contains(value, case=False, na=False)
            )

        result = df[mask]

        if result.empty:
            return f"No rows found where '{column}' matches '{value}'."

        max_rows = 50
        truncated = len(result) > max_rows
        output = result.head(max_rows).to_csv(index=False)
        log.append(f"Filter: {len(result)} rows matched")

        msg = (
            f"**{len(result)} rows** where '{column}' "
            f"matches '{value}':\n\n```\n{output}```"
        )
        if truncated:
            msg += (
                f"\n\n*(Showing first {max_rows} "
                f"of {len(result)} rows)*"
            )
        return msg

    def _aggregate(self, df, column, agg_function, group_by, log):
        """Aggregate a column with optional grouping."""
        if not column or not agg_function:
            return (
                "Both 'column' and 'agg_function' are required "
                "for aggregate."
            )

        agg_function = agg_function.strip().lower()
        valid_funcs = ("sum", "mean", "count", "min", "max")
        if agg_function not in valid_funcs:
            return (
                f"Invalid agg_function '{agg_function}'. "
                f"Use: {', '.join(valid_funcs)}."
            )

        if column not in df.columns:
            return (
                f"Column '{column}' not found. "
                f"Available: {', '.join(str(c) for c in df.columns)}"
            )

        if group_by:
            if group_by not in df.columns:
                return (
                    f"Group-by column '{group_by}' not found. "
                    f"Available: {', '.join(str(c) for c in df.columns)}"
                )
            result = (
                df.groupby(group_by)[column]
                .agg(agg_function)
                .reset_index()
            )
            result.columns = [group_by, f"{agg_function}({column})"]
            output = result.to_csv(index=False)
            log.append(
                f"Aggregate: {agg_function}({column}) by {group_by}"
            )
            return (
                f"**{agg_function}({column})** grouped by "
                f"**{group_by}**:\n\n```\n{output}```"
            )
        else:
            result = df[column].agg(agg_function)
            log.append(
                f"Aggregate: {agg_function}({column}) = {result}"
            )
            return f"**{agg_function}({column}):** {result}"

    def _lookup(self, df, value, log):
        """Search for a value across all columns."""
        if not value:
            return "The 'value' parameter is required for lookup."

        mask = df.apply(
            lambda col: col.astype(str).str.contains(
                value, case=False, na=False
            )
        ).any(axis=1)

        result = df[mask]

        if result.empty:
            return f"No rows found containing '{value}'."

        max_rows = 50
        truncated = len(result) > max_rows
        output = result.head(max_rows).to_csv(index=False)
        log.append(f"Lookup: {len(result)} rows contain '{value}'")

        msg = (
            f"**{len(result)} rows** containing "
            f"'{value}':\n\n```\n{output}```"
        )
        if truncated:
            msg += (
                f"\n\n*(Showing first {max_rows} "
                f"of {len(result)} rows)*"
            )
        return msg
