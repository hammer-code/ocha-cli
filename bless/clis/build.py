from bless.clis.base import Base
from bless.libs import build_utils
from bless.libs import database
import os


CURR_DIR = os.getcwd()

class Build(Base):
    """
        usage:
            build
            build database [-f File]
            build endpoint [-f File]

        Build Project

        Options:
        -h --help                             Print usage
        -f file --file=FILE       sequence execute object
    """

    def execute(self):
        config = build_utils.utils.yaml_read("config.ocha")['config']

        if self.args['database']:
            file = self.args['--file']
            database_obj = build_utils.utils.yaml_read(file)['database']
            config = config['database']
            if config['host'] == "localhost" or config['host'] == "127.0.0.1":
                database.database_parse(config, database_obj,
                                            security = None, auth_config = None)
            exit()

        if self.args['endpoint']:
            file = self.args['--file']

        init_create = dict()
        init_yml = dict()
        init_file = None
        if not build_utils.check_init(CURR_DIR):
            list_dir = build_utils.list_dir(CURR_DIR)
            for i in list_dir:
                index = i['index'].split(".")
                init_create[index[0]] = {
                    "file": i['index']
                }
            init_yml['deploy'] = init_create
            build_utils.utils.yaml_create(init_yml,CURR_DIR+"/init.ocha")
            init_file = build_utils.utils.yaml_read(CURR_DIR+"/init.ocha")
        else:
            init_file = build_utils.utils.yaml_read(CURR_DIR+"/init.ocha")

        build_utils.initialite(init_file, CURR_DIR)
        build_utils.build(CURR_DIR)