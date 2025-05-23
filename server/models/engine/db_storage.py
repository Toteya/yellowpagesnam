"""
Mongo Database storage implementation
"""
from os import environ
from pymongo import MongoClient


class DBStorage():
    """
    MongoDB storage engine
    """
    __client = None
    __db = None

    def __init__(self, host, port, db_name):
        """ Initialize the MongoDB client and database
        """
        self.__client = MongoClient(host, port)
        self.__db = self.__client[db_name]

        if environ.get('DIRECTORY_ENV') == 'testing':
            print("Testing...")
            for collection_name in self.__db.list_collection_names():
                self.__db[collection_name].drop()
    
    
    def all(self):
        """ Returns all  objects stored in the database
        """
        pass

    def get_collection(self, collection_name):
        """ Get a collection from the database
        """
        return self.__db[collection_name]
    
    def new(self, collection_name, item):
        """ Add a new item to the database
        """
        collection = self.get_collection(collection_name)
        collection.insert_one(item)
    
    def load(self):
        """ Load items from database
        """
        pass
