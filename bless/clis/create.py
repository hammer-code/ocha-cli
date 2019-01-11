from bless.clis.base import Base
from bless.libs import parsing as parse
from bless.libs import create_utils
import os, json


CURR_DIR = os.getcwd()
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


class Create(Base):
    """
        usage:
            create
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
        internet = create_utils.utils.check_internet()
        url_bless_object = "https://raw.githubusercontent.com/Blesproject/bless_object/master/"
       
        if self.args['database']:
            check_yml = create_utils.utils.read_file(CURR_DIR+"/database.yml")
            if not check_yml:
                if not internet:
                    value = {
                        "database": {
                            "tables": {
                                "tb_userdata": {
                                    "id_userdata": {
                                        "type": "serial",
                                        "notNull": True,
                                        "primaryKey": True
                                    },
                                    "first_name": {
                                        "type": "varchar",
                                        "notNull": True
                                    },
                                    "last_name": {
                                        "type": "varchar",
                                        "notNull": True
                                    },
                                    "location": {
                                        "type": "varchar"
                                    },
                                    "email": {
                                        "type": "varchar",
                                        "unique": True
                                    }
                                },
                                "tb_user": {
                                    "id_user": {
                                        "type": "serial",
                                        "notNull": True,
                                        "primaryKey": True
                                    },
                                    "id_userdata": {
                                        "type": "int",
                                        "notNull": True,
                                        "foreignKey": {
                                            "reference": "tb_userdata",
                                            "field": "id_userdata",
                                            "on_delete": "cascade",
                                            "on_update": "cascade"
                                        }
                                    },
                                    "username": {
                                        "type": "varchar",
                                        "unique": True
                                    },
                                    "password": {
                                        "type": "varchar"
                                    }
                                }
                            }
                        }
                    }
                else:
                    value = create_utils.utils.download(url_bless_object+"database.yml")
                    value = value.read().decode('utf-8')
                file = create_utils.utils.yaml_create(value,CURR_DIR+"/database.yml")
            exit()
        if self.args['auth']:
            check_yml = create_utils.utils.read_file(CURR_DIR+"/auth.yml")
            if not check_yml:
                if not internet:
                    value = ""
                else:
                    value = create_utils.utils.download(url_bless_object+"auth.yml")
                    value = value.read().decode('utf-8')
                file = create_utils.utils.yaml_create(value,CURR_DIR+"/auth.yml")
            exit()
        if self.args['config']:
            check_yml = create_utils.utils.read_file(CURR_DIR+"/config.yml")
            if not check_yml:
                if not internet:
                    value = ""
                else:
                    value = create_utils.utils.download(url_bless_object+"config.yml")
                    value = value.read().decode('utf-8')
                file = create_utils.utils.yaml_create(value,CURR_DIR+"/config.yml")
            exit()

        if self.args['endpoint']:
            check_yml = create_utils.utils.read_file(CURR_DIR+"/endpoint.yml")
            if not check_yml:
                if not internet:
                    value = ""
                else:
                    value = create_utils.utils.download(url_bless_object+"endpoint.yml")
                    value = value.read().decode('utf-8')
                file = create_utils.utils.yaml_create(value,CURR_DIR+"/endpoint.yml")
            exit()
        
        all_project = ['database','auth','config','endpoint']
       
        for i in all_project:
            value_fix = ""
            if not internet:
                value = ""
                if i == 'database':
                    value = {
                        "database": {
                            "tables": {
                                "tb_userdata": {
                                    "id_userdata": {
                                        "type": "serial",
                                        "notNull": True,
                                        "primaryKey": True
                                    },
                                    "first_name": {
                                        "type": "varchar",
                                        "notNull": True
                                    },
                                    "last_name": {
                                        "type": "varchar",
                                        "notNull": True
                                    },
                                    "location": {
                                        "type": "varchar"
                                    },
                                    "email": {
                                        "type": "varchar",
                                        "unique": True
                                    }
                                },
                                "tb_user": {
                                    "id_user": {
                                        "type": "serial",
                                        "notNull": True,
                                        "primaryKey": True
                                    },
                                    "id_userdata": {
                                        "type": "int",
                                        "notNull": True,
                                        "foreignKey": {
                                            "reference": "tb_userdata",
                                            "field": "id_userdata",
                                            "on_delete": "cascade",
                                            "on_update": "cascade"
                                        }
                                    },
                                    "username": {
                                        "type": "varchar",
                                        "unique": True
                                    },
                                    "password": {
                                        "type": "varchar"
                                    }
                                }
                            }
                        }
                    }
            else:
                value = create_utils.utils.download(url_bless_object+"/"+i+".yml")
                # value = create_utils.utils.yaml_parser(value.read())
                # print(type(value.read()))
                value_fix = value.read().decode('utf-8')
            file = create_utils.utils.create_file(i+".yml",CURR_DIR,value_fix)
        exit()