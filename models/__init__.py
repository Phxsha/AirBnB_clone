#!/usr/bin/python3
"""package initializer"""
from models.engine.file_storge import FileStorage


storage = FileStorage()
storage.reload()
