from cogsol.tools import BaseTool, tool_params


class QueryExcelAttachment(BaseTool):
    """Script tool that queries an Excel file attached to the chat using pandas."""

    name = "query_excel_attachment"
    description = (
        "Query an Excel file attached to the conversation. "
        "Always call with operation 'describe' first, then use "
        "'filter', 'aggregate', or 'lookup' for specific queries."
    )
    show_tool_message = False

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
        import io
        from django.apps import apps

        MessageAttachment = apps.get_model("assistant", "MessageAttachment")

        try:
            last_msg = (
                chat.messages.filter(role="user")
                .order_by("msg_num")
                .last()
                .get_message_dict()
            )
            attachments = last_msg.get("attachments", [])
            if not attachments:
                return "No file attached. Please upload an Excel file and try again."

            attachment_ref = attachments[0]
            if len(attachment_ref.split("-")) > 1:
                attachment_id = attachment_ref.split("-")[1]
            else:
                attachment_id = attachment_ref

            attachment = MessageAttachment.objects.get(id=attachment_id)
            file_bytes = attachment.load_file()
            log.append(f"File loaded: {attachment.content_type}")

        except Exception as e:
            log.append(f"Attachment error: {str(e)}")
            return f"Could not read the attached file: {str(e)}"

        try:
            import pandas as pd

            df = pd.read_excel(
                io.BytesIO(file_bytes),
                sheet_name=sheet if sheet else 0,
            )
            log.append(f"Loaded {len(df)} rows, {len(df.columns)} columns")

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
            col_info.append(f"- **{col}** ({df[col].dtype}): {non_null} non-null values")

        sample = df.head(5).to_markdown(index=False)
        log.append("Describe operation completed")

        return (
            f"**Rows:** {len(df)} | **Columns:** {len(df.columns)}\n\n"
            f"**Column details:**\n"
            + "\n".join(col_info)
            + f"\n\n**First 5 rows:**\n{sample}"
        )

    def _filter(self, df, column, value, log):
        """Return rows where column matches value."""
        import pandas as pd

        if not column or not value:
            return "Both 'column' and 'value' are required for filter operation."

        if column not in df.columns:
            return (
                f"Column '{column}' not found. "
                f"Available columns: {', '.join(df.columns)}"
            )

        col_dtype = df[column].dtype
        if pd.api.types.is_numeric_dtype(col_dtype):
            try:
                value_parsed = float(value)
                mask = df[column] == value_parsed
            except ValueError:
                mask = df[column].astype(str).str.contains(value, case=False, na=False)
        else:
            mask = df[column].astype(str).str.contains(value, case=False, na=False)

        result = df[mask]

        if result.empty:
            return f"No rows found where '{column}' matches '{value}'."

        max_rows = 50
        truncated = len(result) > max_rows
        output = result.head(max_rows).to_markdown(index=False)
        log.append(f"Filter: {len(result)} rows matched")

        msg = f"**{len(result)} rows** where '{column}' matches '{value}':\n\n{output}"
        if truncated:
            msg += f"\n\n*(Showing first {max_rows} of {len(result)} rows)*"
        return msg

    def _aggregate(self, df, column, agg_function, group_by, log):
        """Aggregate a column with optional grouping."""
        if not column or not agg_function:
            return "Both 'column' and 'agg_function' are required for aggregate operation."

        agg_function = agg_function.strip().lower()
        valid_funcs = ("sum", "mean", "count", "min", "max")
        if agg_function not in valid_funcs:
            return f"Invalid agg_function '{agg_function}'. Use: {', '.join(valid_funcs)}."

        if column not in df.columns:
            return (
                f"Column '{column}' not found. "
                f"Available columns: {', '.join(df.columns)}"
            )

        if group_by:
            if group_by not in df.columns:
                return (
                    f"Group-by column '{group_by}' not found. "
                    f"Available columns: {', '.join(df.columns)}"
                )
            result = df.groupby(group_by)[column].agg(agg_function).reset_index()
            result.columns = [group_by, f"{agg_function}({column})"]
            output = result.to_markdown(index=False)
            log.append(f"Aggregate: {agg_function}({column}) grouped by {group_by}")
            return f"**{agg_function}({column})** grouped by **{group_by}**:\n\n{output}"
        else:
            result = df[column].agg(agg_function)
            log.append(f"Aggregate: {agg_function}({column}) = {result}")
            return f"**{agg_function}({column}):** {result}"

    def _lookup(self, df, value, log):
        """Search for a value across all columns."""
        if not value:
            return "The 'value' parameter is required for lookup operation."

        mask = df.apply(
            lambda col: col.astype(str).str.contains(value, case=False, na=False)
        ).any(axis=1)

        result = df[mask]

        if result.empty:
            return f"No rows found containing '{value}'."

        max_rows = 50
        truncated = len(result) > max_rows
        output = result.head(max_rows).to_markdown(index=False)
        log.append(f"Lookup: {len(result)} rows contain '{value}'")

        msg = f"**{len(result)} rows** containing '{value}':\n\n{output}"
        if truncated:
            msg += f"\n\n*(Showing first {max_rows} of {len(result)} rows)*"
        return msg
