from cogsol.content import BaseIngestionConfig, ChunkingMode


class RecipeIngestionConfig(BaseIngestionConfig):
    name = "recipe_ingestion"
    chunking_mode = ChunkingMode.LANGCHAIN
    max_size_block = 2500
    chunk_overlap = 300
    separators = ["\n\n", "\n", " "]
