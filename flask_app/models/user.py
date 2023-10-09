from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
import string
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB = "tree_survey_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM users;"
    #     # make sure to call the connectToMySQL function with the schema you are targeting.
    #     results = connectToMySQL(cls.DB).query_db(query)
    #     # Create an empty list to append our instances of users
    #     users = []
    #     # Iterate over the db results and create instances of users with cls.
    #     for user in results:
    #         users.append(cls(user))
    #     return users

    # class method to save our user to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {"id": id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        #print(results)
        return cls(results[0])
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    # @classmethod
    # def edit_user(cls, data):
    #     query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
    #     print(query)
    #     result =  connectToMySQL(cls.DB).query_db(query, data)
    #     print(result)
    #     return result
    
    # @classmethod
    # def delete_user(cls, id):
    #     query = "DELETE FROM users WHERE id = %(id)s;"
    #     return connectToMySQL(cls.DB).query_db(query, {"id": id})
    
    @staticmethod
    def validate_register(user):
        """
        First Name - letters only, at least 3 characters and that it was submitted
        Last Name - letters only, at least 3 characters and that it was submitted
        Email - valid Email format, does not already exist in the database, and that it was submitted
        Password - at least 8 characters, and that it was submitted
        Password Confirmation - matches password
        Level up your password validations by requiring at least one capital letter and one number.
        Passwords must contain a special character ~ ! @ # $ % ^ & *
        https://docs.python.org/3/library/string.html
        """
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(User.DB).query_db(query,user)
        is_valid = True # we assume this is true
        if len(results) >= 1:
            flash("Email already has been used.", "register")
            is_valid = False
        if len(user['first_name']) < 3:
            flash("First name is required and must be at least 3 characters.", "register")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name is required and must be at least 3 characters.", "register")
            is_valid = False
        if (user['first_name']).isalpha() == False:
            flash("First name must be all letters.", "register")
            is_valid = False
        if (user['last_name']).isalpha() == False:
            flash("Last name must be all letters.", "register")
            is_valid = False
        if len(user['email']) <= 0:
            flash("Email is required.", "register")
            is_valid = False
        # if len(user['email']) < 3:
        #     flash("Email must be at least 3 characters.", "register")
        #     is_valid = False
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", "register")
            is_valid = False
        if len(user["email"]) > 0 and not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email format.", "register")
            is_valid = False
        if len(user['password']) <= 0:
            flash("Password is required.", "register")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters long.", "register")
            is_valid = False
        NON_ALPHABETIC_CHARACTERS = {'#', '@', '%', '!', '~', '$', '^', '&', '*'}
        DIGITS_CHARACTERS = set(string.digits)
        LETTERS_CHARACTERS = set(string.ascii_letters)
        LOWER_CASE_LETTERS = set(string.ascii_lowercase)
        UPPER_CASE_LETTERS = set(string.ascii_uppercase)
        if not any(character in user['password']
            for character in UPPER_CASE_LETTERS):
            flash("Password must contain at least one Capital letter.", "register")
            is_valid = False
        if not any(character in user['password']
            for character in LOWER_CASE_LETTERS):
            flash("Password must contain at least one lower cased letter.", "register")
            is_valid = False
        if not any(character in user['password']
            for character in DIGITS_CHARACTERS):
            flash("Password must contain at least one number.", "register")
            is_valid = False
        if not any(character in user['password']
            for character in NON_ALPHABETIC_CHARACTERS):
            flash("Password must contain at least one special character.", "register")
            is_valid = False
        if user['password'] != user['confirm']:
            flash("Passwords don't match", "register")
            is_valid = False
        #print("First character of password: ", user['password'][0])
        # if len(user['password']) > 0 and user['password'][0] != LETTERS_CHARACTERS:
        #     flash("Password must start with a letter.", "register")
        #     is_valid = False
        return is_valid
