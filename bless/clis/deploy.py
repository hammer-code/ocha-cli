from bless.clis.base import Base
from bless.libs import deploy_utils
import os


CURR_DIR = os.getcwd()

class Deploy(Base):
    """
        usage:
            deploy
            deploy docker
            deploy neo
            deploy [-S server]

        Build Project

        Options:
        -h --help                             Print usage
        -S server --server=SERVER       sequence execute object
    """

    def execute(self):
        if self.args['docker']:
            deploy_utils.docker_deploy()
        if self.args['neo']:
            bless_object = deploy_utils.utils.yaml_read(CURR_DIR+"/.deploy/bless.yml")
            deploy_utils.neo_deploy(bless_object,CURR_DIR)