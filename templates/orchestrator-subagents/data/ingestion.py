from cogsol.content import BaseIngestionConfig, PDFParsingMode, ChunkingMode
#
# class DefaultIngestionConfig(BaseIngestionConfig):
#     """Default ingestion configuration for documents."""
#
#     name = "default_ingestion"
#     pdf_parsing_mode = PDFParsingMode.BOTH
#     chunking_mode = ChunkingMode.LANGCHAIN
#     max_size_block = 1500
#     chunk_overlap = 0
#     separators = []
#     ocr = False
#     additional_prompt_instructions = ""
#     assign_paths_as_metadata = False
