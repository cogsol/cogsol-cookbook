from cogsol.content import BaseReferenceFormatter


class RecipeFormatter(BaseReferenceFormatter):
    name = "recipe_formatter"
    description = "Reference format for recipe documents."
    expression = "[{name}]"
