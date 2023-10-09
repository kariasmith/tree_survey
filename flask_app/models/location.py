from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Location:
    DB = "tree_survey_schema"
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.address = data["address"]
        self.address_2 = data["address_2"]
        self.city = data["city"]
        self.state = data["state"]
        self.zip = data["zip"]
        self.deciduous_trees = data["deciduous_trees"]
        self.coniferous_trees = data["coniferous_trees"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        # LONGTEXT column can hold up to 4 gigabytes of data.
        # https://dev.mysql.com/doc/workbench/en/wb-migration-database-postgresql-typemapping.html

    @classmethod
    def get_one(cls, id):
        data = {"id": id}
        query = "SELECT * from locations LEFT JOIN users on locations.user_id = users.id WHERE locations.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("Raw data for one location: ", results)
        location = results[0]
        print("The initiated location result:", location)
        return location

    @classmethod
    def get_locations_for_user(cls, id):
        data = {"id": id}
        query = "SELECT * from locations LEFT JOIN users on locations.user_id = users.id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("Raw data for user's location: ", results)
        locations = []
        for x in results:
            locations.append(x)
        print("The initiated locations result:", locations)
        return locations
    
    @classmethod
    def save(cls, data):
        if not cls.validate_location(data):
            print("in save if not valid...")
            return False
        print("Data passed into create METHOD: ", data)
        query = "INSERT into locations (name, address, address_2, city, state, zip, deciduous_trees, coniferous_trees, created_at, updated_at, user_id) values (%(name)s, %(address)s, %(address_2)s, %(city)s, %(state)s, %(zip)s, %(deciduous_trees)s, %(coniferous_trees)s, NOW(), NOW(), %(user_id)s);"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    @classmethod
    def edit(cls, data):
        print("Data passed into edit METHOD: ", data)
        query = "UPDATE locations SET name=%(name)s, address=%(address)s, address_2=%(address_2)s, city=%(city)s, state=%(state)s, zip=%(zip)s, deciduous_trees=%(deciduous_trees)s, coniferous_trees=%(coniferous_trees)s, updated_at=NOW() WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    @classmethod
    def delete(cls, id):
        query = "DELETE from locations WHERE id = %(id)s;"
        connectToMySQL(cls.DB).query_db(query, {"id": id})
        return id

    @staticmethod
    def validate_location(data):
        is_valid = True
        if len(data["name"]) == 0:
            flash("Name of the location is required.", "new_location")
            is_valid = False
        if len(data["address"]) == 0:
            flash("Address is required.", "new_location")
            is_valid = False
        if len(data["city"]) == 0:
            flash("City is required.", "new_location")
            is_valid = False
        if len(data["state"]) == 0:
            flash("State is required.", "new_location")
            is_valid = False
        # if len(data["state"]) == 0:
        #     flash("State selection must be valid.", "new_location")
        #     is_valid = False
        if len(data["zip"]) == 0:
            flash("Zip code is required.", "new_location")
            is_valid = False
        if len(data["deciduous_trees"]) == 0:
            flash("Deciduous Trees must be a positive number or zero.", "new_location")
            is_valid = False
        if len(data["coniferous_trees"]) == 0:
            flash("Coniferous Trees must be a positive number or zero.", "new_location")
            is_valid = False
        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * from locations LEFT JOIN users on locations.user_id = users.id;"
        results = connectToMySQL(cls.DB).query_db(query)
        print("Raw data for all locations: ", results)
        all_recipes = []
        # iterate over raw data list of post dictionaries
        for row in results:
            # each loop
            #  - make user instance
            # posting_user = User({
            #     "id": row["user_id"],
            #     "first_name": row["first_name"],
            #     "last_name": row["last_name"],
            #     "email": row["email"],
            #     "password": row["password"],
            #     "created_at": row["users.created_at"],
            #     "updated_at": row["users.updated_at"]
            # })
            # #  - make post instance with a user object
            # new_recipe = Recipe({
            #     "id": row["id"],
            #     "name": row["name"],
            #     "description": row["description"],
            #     "instructions": row["instructions"],
            #     "date_made": row["date_made"],
            #     "under_30": row["under_30"],
            #     "created_at": row["created_at"],
            #     "updated_at": row["updated_at"],
            #     #"user_id": row["user_id"]
            #     "user_id": posting_user
            # })
            # Add post to all_posts list
            all_recipes.append(row)
        # print("first all_recipes result: ", all_recipes[0])
        # print("second all_recipes result: ", all_recipes[1])
        return all_recipes