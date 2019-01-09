from bless.clis.base import Base
from bless.libs import build_utils
import os


CURR_DIR = os.getcwd()

class Build(Base):
    """
        usage:
            build
            build [-s SEQUENCE]

        Build Project

        Commands :

        Options:
        -h --help                             Print usage
        -s sequence --sequence=SEQUENCE       sequence execute object
    """

    def execute(self):
        if self.args['--sequence']:
            execute_arg = self.args['--sequence']
            exit()
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
            build_utils.utils.yaml_create(init_yml,CURR_DIR+"/init.yml")
            init_file = build_utils.utils.yaml_read(CURR_DIR+"/init.yml")
        else:
            init_file = build_utils.utils.yaml_read(CURR_DIR+"/init.yml")
        build_utils.initialite(init_file, CURR_DIR)
        build_utils.build(CURR_DIR)