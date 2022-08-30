from flask_app.config.mysqlconnection import connectToMySQL

class Food:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.calories = data['calories']
        self.serving_size = data['serving_size']
        self.measurement_type = data['measurement_type']
        self.caloric_density = data['caloric_density']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM foods;"

        results = connectToMySQL('omnom').query_db(query)

        foods = []

        for food in results:
            foods.append(cls(food))

        return foods

    @classmethod
    def add_food(cls, data):
        query = "INSERT INTO foods (name, calories, serving_size, measurement_type, caloric_density) VALUES (%(name)s, %(calories)s, %(serving_size)s, %(measurement_type)s, 'very dense');"

        result = connectToMySQL('omnom').query_db(query, data)

        return result


    @classmethod
    def get_food(cls, data):
        query = "SELECT * FROM foods WHERE id = %(id)s;"

        result = connectToMySQL('omnom').query_db(query, data)

        # print(result)

        return cls(result[0])


    @classmethod
    def update_food(cls, data):
        query = "UPDATE foods SET name = %(name)s, calories = %(calories)s, serving_size = %(serving_size)s, measurement_type = %(measurement_type)s WHERE id = %(id)s;"

        connectToMySQL('omnom').query_db(query, data)

        return True

    # add a CREATE query
    # @classmethod
    # def add_food(cls):
    #     query = "INSERT INTO foods (name, calories, serving_size, measurement_type, caloric_density) VALUES ("Whole Coffee Beans", 10, 250, "grams", 1);"

    # add a READ query that only reads one food

    # add an UPDATE query

    # add a DELETE query