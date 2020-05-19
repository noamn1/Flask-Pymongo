
import pymongo
from bson import ObjectId

from model.user import User


class DataLayer:

    def get_user(self, user_name):
        user_dict = self.__db.users.find_one({"username": user_name})
        user = self.create_user_from_dict(user_dict)
        return user

    def get_user_by_id(self, user_id):
        user_dict = self.__db.users.find_one({"_id": ObjectId(user_id)})
        user = self.create_user_from_dict(user_dict)
        return user

    # create user from dict
    def create_user_from_dict(self, user_dict):
        user = User(user_dict['_id'], user_dict['first_name'], user_dict['last_name'], user_dict['username'],
                    user_dict['email'], user_dict['age'], user_dict['date'])
        return user

    def __init__(self):
        self.__client = pymongo.MongoClient('localhost', 27017)
        self.__db = self.__client["music"]
