"""
Mongo Database storage implementation
"""
from mongoengine import connect, DoesNotExist
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

        connect(
            db=db_name,
            host=host,
            port=port,
            alias='default',
            uuidRepresentation='standard'
        )

        if environ.get('DIRECTORY_ENV') == 'testing':
            print("Testing...")
            self.clear()
    
    def clear(self):
        """ Clears the database by dropping all collections
        """
        for collection_name in self.__db.list_collection_names():
            self.__db[collection_name].drop()
    
    def get_collection_name(self, clss):
        """ Returns the collection name for the given class
        """
        collections = {
            'Listing': 'listings'
        }
        return collections.get(clss.__name__)
    
    def all(self, clss=None):
        """ Retrieves all objects for the given class. Or returns all objects
        of all classes if no class is specified.
        Args:
            clss (class, optional): The class to retrieve objects for. Defaults to None.
        Returns:
            list: A list of objects retrieved from the database.
        """
        # if clss is not None and clss.__name__ not in self.__db.list_collection_names():
        if not clss:
            raise ValueError(f"Class {clss.__name__} does not exist in the database.")
        else:
            return list(clss.objects())

    def get(self, clss=None, id=None):
        """ Returns the object matching the given class and id
        Args:
            clss (class): The class of the object to retrieve.
            id (str): The id of the object to retrieve.
        """
        if not all([clss, id]):
            return None
        try:
            return clss.objects.get(id=id)
        except DoesNotExist:
            return None

    def new(self, obj):
        """ Add/Save a new document object to the database
        Args:
            obj (object): The MongoDB Document instance to be saved.
        """
        if obj:
            obj.save()
