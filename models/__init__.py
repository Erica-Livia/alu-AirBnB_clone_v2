#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from engine.file_storage import FileStorage
from engine.db_storage import DBStorage
import os

if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
