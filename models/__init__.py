#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
import os
import os.environ.get('HBNB_TYPE_STORAGE')



storage = FileStorage()
storage.reload()
