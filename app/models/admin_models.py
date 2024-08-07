from ..import mongo


class Get_admin:
    def admin_collection(admin_data):
        return mongo.db.admin_collection.insert_one(admin_data)