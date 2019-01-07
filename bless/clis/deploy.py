from bless.clis.base import Base
from bless.libs import deploy_utils
import os


CURR_DIR = os.getcwd()

class Deploy(Base):
    """
        usage:
            deploy
            deploy [-s SEQUENCE]

        Deploy Project

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
        if not deploy_utils.check_init(CURR_DIR):
            list_dir = deploy_utils.list_dir(CURR_DIR)
            for i in list_dir:
                index = i['index'].split(".")
                init_create[index[0]] = {
                    "file": i['index']
                }
            init_yml['deploy'] = init_create
            deploy_utils.utils.yaml_create(init_yml,CURR_DIR+"/init.yml")
            init_file = deploy_utils.utils.yaml_read(CURR_DIR+"/init.yml")
        else:
            init_file = deploy_utils.utils.yaml_read(CURR_DIR+"/init.yml")
        deploy_utils.initialite(init_file, CURR_DIR)
        deploy_utils.deploy(CURR_DIR)