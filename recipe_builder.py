from utils import MealType, RecipeTime
from recipe import Recipe

import time

class RecipeBuilder:

    def __init__(self):
        self.recipes = self.load_recipes_from_json()
        self.valid_ingredients = self.load_valid_ingredients_from_json()

    def filter_by_meal_type(self, meal_type: MealType):
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

    def search_for_recipe(self, recipe_name: str) -> list[Recipe]:
        """Retrieve a recipe by searching for it by name and then display options for editting or deleting this recipe

        Args:
            recipe_name (str): the name of the recipe
        """

    def main_menu(self):
        "Displays a selection menu for the user"
        
        while True:
            self.display_main_menu()
            selection = input("Selection: ")
            if not self.is_valid_user_input(selection=selection):
                print(f"Invalid input: {selection}")
                time.sleep(1)
                continue
            else:
                should_exit = self.direct_user_to_correct_page(selection=selection)
                if should_exit:
                    print("Thanks for using the Recipe Builder App!")
                    break
            
    def display_main_menu(self):
        print("Welcome to the Recipe Builder App! Please select one of the following options:\n")
        print("1.   Add a new recipe")
        print("2.   Search for a recipe")
        print("3.   Filter recipes by cost")
        print("4.   Filter recipes by meal type")
        print("5.   Filter recipes by time")
        print("q.   Quit the app")
        print()

    def is_valid_user_input(self, selection: str):
        if selection in "12345qQ":
            return True
        else:
            return False
        
    def direct_user_to_correct_page(self, selection: str):
        if selection == '1':
            return False
        elif selection == '2':
            return False
        elif selection == '3':
            return False
        elif selection == '4':
            return False
        elif selection == '5':
            return False
        elif selection == 'q' or selection == 'Q':
            return True
        else:
            print("Invalid option, this should never execute!")
            return False

    def main(self):
        """Main event loop"""
        self.main_menu()


if __name__ == "__main__":
    recipe_builder = RecipeBuilder()
    recipe_builder.main()
