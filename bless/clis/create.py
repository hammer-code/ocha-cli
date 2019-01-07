from bless.clis.base import Base
from bless.libs import parsing as parse
from bless.libs import utils
import os


CURR_DIR = os.getcwd()


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
            check_yml = utils.read_file(CURR_DIR+"/database.yml")
            if not check_yml:
                pass
            exit()
        if self.args['auth']:
            print("auth")
            exit()
        if self.args['config']:
            print("Config")
            exit()
        if self.args['endpoint']:
            print("Endpoint")