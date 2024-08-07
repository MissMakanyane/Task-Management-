from ..import mongo
from flask_bcrypt import Bcrypt


class Data_admin:
    def create_new(signup_data):
        return mongo.db.user.insert_one(signup_data)
    