"""
Mongo Database storage implementation
"""
from mongoengine import connect, Document, DoesNotExist
from os import environ
from pymongo import MongoClient
from server.models.listing import Listing



class DBStorage():
    """
    MongoDB storage engine
    """
    __client = None
    __db = None
    __registered_classes = [Listing]  # List of registered MongoEngine model classes


    def __init__(self, host, port, db_name):
        """ Initialize the MongoDB client and database
        """
        self.__client = MongoClient(host, port)
        try:
            self.__db = self.__client[db_name]
        except TypeError as e:
            raise e('Invalid database name provided. Please check environment setup/configuration.')

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
        self.__client.drop_database(self.__db.name)
        self.__db = self.__client[self.__db.name]  # Reinitialize the db after drop
    
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
        if clss is None:
            all_objects = []
            for model_class in self.__registered_classes:
                all_objects.extend(model_class.objects())
            return all_objects

        if not issubclass(clss, Document):
            raise ValueError(f"The provided class '{clss}' is not a valid MongoEngine model class.")
        
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

    def delete(self, obj):
        """ Delete an object from the database
        """
        if obj:
            obj.delete()

    def new(self, obj):
        """ Add/Save a new document object to the database
        Args:
            obj (object): The MongoDB Document instance to be saved.
        """
        if obj:
            obj.save()
