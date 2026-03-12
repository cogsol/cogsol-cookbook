from cogsol.content import BaseMetadataConfig, MetadataType


class CategoryMetadata(BaseMetadataConfig):
    name = "category"
    type = MetadataType.STRING
    possible_values = [
        "Network",
        "Hardware",
        "Software",
        "Security",
        "Onboarding",
    ]
    filtrable = True
    required = False
    in_retrieval = True
