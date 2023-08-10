from lib.recipe_repository import *
from lib.recipe import *

'''
When I call RecipeRepository#all
I get a list of Recipe objects reflecting the seed data
'''
def test_get_all_records(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    recipes = repository.all()
    #Assert on the results
    assert recipes == [
        Recipe(1, 'Shakshuka', 12, 3),
        Recipe(2, 'Apple crumble', 25, 3),
        Recipe(3, 'Paella', 30, 5),
        Recipe(4, 'Lemon tart', 5, 4)
    ]
    assert len(recipes) == 4

'''
When I call RecipeRepository#find with a specific condition (name)
I get back a single Recipe object matching that condition
'''
def test_get_single_record(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    recipe = repository.find(2)
    assert recipe == Recipe(2, 'Apple crumble', 25, 3)