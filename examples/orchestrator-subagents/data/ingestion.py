from cogsol.content import BaseIngestionConfig, PDFParsingMode, ChunkingMode


class TravelIngestionConfig(BaseIngestionConfig):
    name = "orchestrator_ingestion"
    pdf_parsing_mode = PDFParsingMode.MANUAL
    chunking_mode = ChunkingMode.LANGCHAIN
    max_size_block = 2500
    chunk_overlap = 100
    separators = []
    ocr = False
    additional_prompt_instructions = ""
    assign_paths_as_metadata = False
