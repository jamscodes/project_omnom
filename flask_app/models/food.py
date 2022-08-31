from flask_app.config.mysqlconnection import connectToMySQL

# calories / 453.5924 (if < 300 then it is not dense) (if 300 < x < 800 then it is dense) (if 800 < x then it is very dense)


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

    @staticmethod
    def determine_density(calories, serving_size):
        calories_per_unit = calories * (456.5924 / serving_size)

        if calories_per_unit < 300:
            return 'not dense'
        elif 300 < calories_per_unit < 800:
            return 'dense'
        else:
            return 'very dense'


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
        query = "INSERT INTO foods (name, calories, serving_size, measurement_type, caloric_density) VALUES (%(name)s, %(calories)s, %(serving_size)s, %(measurement_type)s, %(caloric_density)s);"

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
        query = "UPDATE foods SET name = %(name)s, calories = %(calories)s, serving_size = %(serving_size)s, measurement_type = %(measurement_type)s, caloric_density = %(caloric_density)s WHERE id = %(id)s;"

        data['caloric_density'] = cls.determine_density(data.get('calories'), data.get('serving_size'))

        connectToMySQL('omnom').query_db(query, data)

        return True