from lib.recipe import *

'''
Recipe constructs with an id, name, cooking_time and rating
'''
def test_recipe_constructs_with_fields():
    recipe = Recipe(1, "Test recipe", 20, 4)
    assert recipe.id == 1
    assert recipe.name == "Test recipe"
    assert recipe.cooking_time == 20
    assert recipe.rating == 4

'''
I can format recipes to strings for readability
'''
def test_format_recipes_nicely():
    recipe = Recipe(1, "Test recipe", 20, 4)
    assert str(recipe) == 'Recipe(1, Test recipe, 20, 4)'

'''
I can compare two identical recipes 
And have them be equal
'''
def test_recipes_are_equal():
    recipe1 = Recipe(1, "Test recipe", 20, 4)
    recipe2 = Recipe(1, "Test recipe", 20, 4)
    assert recipe1 == recipe2
