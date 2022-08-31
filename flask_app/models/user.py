from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data.get('id')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.email = data.get('email')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

    
    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"

        result = connectToMySQL('omnom').query_db(query, data)

        return cls(result[0])