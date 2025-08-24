"""
Data types:

@dataclass
Ingredient:
    name: str
    quantity: float
    unit: MeasuringUnit
    cost: float

@dataclass
RecipeTime:
    days: int
    hours: int
    minutes: int

class MealType(Enum):
    BREAKFAST = 1
    LUNCH = 2
    DINNER = 3
    SIDES = 4
    APPETIZER = 5
    DESSERT = 6

class MeasuringUnit(Enum):
    QUARTER_TEASPOON = 1
    HALF_TEASPOON = 2
    TEASPOON = 3
    HALF_TABLESPOON = 4
    TABLESPOON = 5
    FOURTH_CUP = 6
    THIRD_CUP = 7
    HALF_CUP = 8
    THREE_FOURTHS_CUP = 9
    CUP = 10
    OZ = 11

class Recipe:
    hyperlink: <str optional>
    meal_type: MealType
    recipe_time: RecipeTime
    ingredients: list[Ingredient]
    total_cost: float

    def consolidate_ingredients(self):
        "Consolidates duplicate ingredients by adding their quantities and displaying them in a common unit type
        We will assume that whichever duplicate occurs first is the units we will use to convert the others to"
        pass
    
    def calculate_total_cost(self):
        "Use the list of ingredients to calculate the total cost by summing their indiviual cost"

class RecipeBuilder:
    recipes: list[Recipe]

    def filter_by_meal_type(self, meal_type: MealType)
        "We reduce the number of recipes by those which have the matching MealType"
        pass
        
    def filter_by_cost(self, cost_threshold: float):
        "We reduce the number of recipes which are above the threshold"
        pass
        
    def filter_by_time(self, time: RecipeTime):
        "We reduce the number of recipes based on the length of time it takes to complete the recipe"
        pass
        
    def sort_by_cost(self, asc: bool = True):
        "Sorts the recipe by cost in ascending order if asc==True and in descending order if asc==False"
        pass
        
    def load_valid_ingredients_from_json(self, path: str = "ingredients.json"):
        "Stores the list of valid ingredients in the RecipeBuilder class from the ingredients json file"
        pass
    
    def load_recipes_from_json(self, path: str = "recipes.json"):
        "Stores the list of recipes into the RecipeBuilder class from the recipe json file"
        pass
        
    def add_new_recipe(self):
        "Display a menu for the user to step through so that they can add a new recipe to the app and store it automatically in the recipes.json file"
        pass
        
    def update_recipe(self, recipe_name: str):
        "Display a menu for the user to update an existing recipe based on the recipe name and change the store the changes in the recipes.json file"
        pass
        
    def delete_recipe(self, recipe_name: str):
        "Delete an existing recipe from the RecipeBuilder class and the recipes.json file"
        pass

    def main_menu(self):
        "Displays a selection menu for the user"
        pass

    def main(self):
        "Main event loop which
        1. load_valid_ingredients_from_json()
        2. load_recipes_from_json()
        3. main_menu()"
"""