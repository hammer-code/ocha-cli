from bless.clis.base import Base
from bless.libs import parsing as parse
import os


class Create(Base):
    """
        usage:
            create database
            create auth
            create config
            create endpoint

        Build Yaml File

        Commands :
        database                              Create Database Object
        auth                                  Create Auth Object
        config                                Create Config Object
        endpoint                              Create Endpoint Object

        Options:
        -h --help                             Print usage
    """

    def execute(self):
        if self.args['database']:
            print("database")
            exit()
        if self.args['auth']:
            print("auth")
            exit()
        if self.args['config']:
            print("Config")
            exit()
        if self.args['endpoint']:
            print("Endpoint")