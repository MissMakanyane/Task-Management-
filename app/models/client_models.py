from ..import mongo


class User:
   
    def create_user(details):
    #  mongo.db.user2.insert_one(details)
     return mongo.db.user2.insert_one(details)

    def login_user(loginDetails):
        # mongo.db.user2.find_one(loginDetails)
        return mongo.db.user2.find_one(loginDetails)
                               