#!/usr/bin/python3
''' create a unique fileStorage instance for application'''

from models.engine.file_storage import FileStorage

storage = FileStorage()

#storage.new(self)
#storage.save()
storage.reload()
