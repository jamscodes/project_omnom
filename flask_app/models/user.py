from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class User:
    def __init__(self, data):
        self.id = data.get('id')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.email = data.get('email')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')


    @staticmethod
    def validate_user_login(form_data):
        is_valid = True

        # Check if everything was submitted
        if not form_data.get('email'):
            flash('Email is required')
            is_valid = False
        if not form_data.get('password'):
            flash('Password is required')
            is_valid = False
        # Check if user exists

        return is_valid


    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"

        result = connectToMySQL('omnom').query_db(query, data)

        return cls(result[0])



    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"

        result = connectToMySQL('omnom').query_db(query, data)

        return cls(result[0])