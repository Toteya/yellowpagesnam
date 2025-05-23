"""
models package initialisation file
"""
from os import environ
from server.models.engine.db_storage import DBStorage

HOST = environ.get('DIRECTORY_HOST', 'localhost')
PORT = int(environ.get('DIRECTORY_PORT', 27017))
DB_NAME = environ.get('DIRECTORY_DB')

storage = DBStorage(HOST, PORT, DB_NAME)
storage.load()
