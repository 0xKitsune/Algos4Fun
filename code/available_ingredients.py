from code.unittestSingleton import test
#The Baker
#---------------------------------------------------------
# Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). 
# For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
# Ingredients that are not present in the objects, can be considered as 0.
#---------------------------------------------------------
#solution
#------------

from math import floor

def cakes(recipe, available):
    try:
        ingredient_availablity=[]
        #find the quotient of ingredients available/the recipe
        for (k,v) in recipe.items():
            ingredient_availablity.append(available[k]/v)
        return floor(min(ingredient_availablity))
    #if missing an ingredient, return 0
    except: 
        return 0


#sample tests
recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
test.assert_equals(cakes(recipe, available), 2, 'example #1')

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
test.assert_equals(cakes(recipe, available), 0, 'example #2')