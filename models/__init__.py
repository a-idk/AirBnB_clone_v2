#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
# from models.engine.file_storage import FileStorage
from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place


if getenv("HBNB_TYPE_STORAGE") == "db":  # if environ variable is set to db
    # from models.engine.db_storage import DBStorage
    storage = DBStorage()  # set storage to database storage engine
else:  # set storage to filestorage
    # from models.engine.file_storage import FileStorage
    storage = FileStorage()
# storage = FileStorage()
storage.reload()
