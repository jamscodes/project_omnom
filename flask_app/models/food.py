from ..config.mysqlconnection import MySQLConnection

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

        results = MySQLConnection('omnom').query_db(query)

        foods = []

        for food in results:
            foods.append(cls(food))

        return foods

    
    # @classmethod
    # def add_food(cls):
    #     query = "INSERT INTO foods (name, calories, serving_size, measurement_type, caloric_density) VALUES ("Whole Coffee Beans", 10, 250, "grams", 1);"

# invisible process that returns a dictionary with all of the 
# database columns

# @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM friends;"
    #     # make sure to call the connectToMySQL function with the schema you are targeting.
    #     results = connectToMySQL('first_flask').query_db(query)
    #     # Create an empty list to append our instances of friends
    #     friends = []
    #     # Iterate over the db results and create instances of friends with cls.
    #     for friend in results:
    #         friends.append( cls(friend) )
    #     return friends