from lib.recipe import *

class RecipeRepository:
    #Initialise with a database connection
    def __init__(self, connection) -> None:
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from recipes')
        recipes = []
        for row in rows:
            print(row)
            item = Recipe(row['id'], row['name'], row['cooking_time'], row['rating'])
            recipes.append(item)
            print(recipes)
        return recipes
    
    def find(self, name):
        rows = self._connection.execute('SELECT * from recipes WHERE id = %s', [name])
        row = rows[0]
        return Recipe(row['id'], row['name'], row['cooking_time'], row['rating'])