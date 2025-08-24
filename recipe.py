from utils import *

class Recipe:

    def __init__(self, meal_type: MealType, recipe_time: RecipeTime, ingredients: list[Ingredient], hyperlink: str = None):
        self.hyperlink = hyperlink
        self.meal_type = meal_type
        self.recipe_time = recipe_time
        self.ingredients = ingredients
        self.total_cost = self.calculate_total_cost()

    def consolidate_ingredients(self):
        """Consolidates duplicate ingredients by adding their quantities and displaying them in a common unit type
        We will assume that whichever duplicate occurs first is the units we will use to convert the others to"""
        pass
    
    def calculate_total_cost(self):
        "Use the list of ingredients to calculate the total cost by summing their indiviual cost"
        pass