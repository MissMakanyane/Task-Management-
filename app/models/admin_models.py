from ..import mongo


class Data_admin:
    def create_new(signup_data):
        return mongo.db.user.insert_one(signup_data)
   
   
    def admin_login(signup_data):
        return mongo.db.user.insert_one(signup_data)
    