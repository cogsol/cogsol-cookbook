from cogsol.content import BaseMetadataConfig, MetadataType


class GenreMetadata(BaseMetadataConfig):
    name = "genre"
    type = MetadataType.STRING
    possible_values = [
        "Action",
        "Comedy",
        "Drama",
        "Horror",
        "Sci-Fi",
        "Romance",
        "Thriller",
        "Animation",
    ]
    filtrable = True
    required = False
    in_retrieval = True


class LanguageMetadata(BaseMetadataConfig):
    name = "language"
    type = MetadataType.STRING
    possible_values = [
        "English",
        "Spanish",
        "French",
        "Japanese",
        "Korean",
    ]
    filtrable = True
    required = False
    in_retrieval = True


class DecadeMetadata(BaseMetadataConfig):
    name = "decade"
    type = MetadataType.STRING
    possible_values = [
        "1990s",
        "2000s",
        "2010s",
        "2020s",
    ]
    filtrable = True
    required = False
    in_retrieval = True
