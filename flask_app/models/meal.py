from flask_app.config.mysqlconnection import connectToMySQL
from .food import Food

class Meal:
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.type = data.get('type')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')


    @classmethod
    def add_meal(cls, data, ingredient_ids):
        query = "INSERT INTO meals (name, type) VALUES (%(name)s, %(type)s);"

        result = connectToMySQL('omnom').query_db(query, data)

        for ingredient_id in ingredient_ids:
            ing_data = {
                'food_id': ingredient_id,
                'meal_id': result,
                'quantity': 1
            }

            ing_query = "INSERT INTO ingredients (food_id, meal_id, quantity) VALUES (%(food_id)s, %(meal_id)s, %(quantity)s);"

            connectToMySQL('omnom').query_db(ing_query, ing_data)

        return result


    @classmethod
    def get_all_meals(cls):
        query = "SELECT * FROM meals;"

        results = connectToMySQL('omnom').query_db(query)

        meals = []

        for result in results:
            meals.append(cls(result))

        return meals


    # Need to make a classmethod that returns a meal with its foods
    @classmethod
    def get_meal(cls, data):
        meal_query = "SELECT * FROM meals WHERE id = %(id)s;"

        meal = connectToMySQL('omnom').query_db(meal_query, data)

        foods_query = "SELECT foods.id, foods.name, foods.calories, foods.serving_size, foods.caloric_density, foods.measurement_type, foods.updated_at, foods.created_at FROM ingredients JOIN meals ON meal_id = meals.id JOIN foods ON food_id = foods.id WHERE meal_id = %(id)s;"

        foods = connectToMySQL('omnom').query_db(foods_query, data)

        food_instances = []

        for food in foods:
            food_instances.append(Food(food))

        return [cls(meal[0]), food_instances]