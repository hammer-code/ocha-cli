from bless.clis.base import Base
from bless.libs import deploy_utils
import os


CURR_DIR = os.getcwd()

class Deploy(Base):
    """
        usage:
            deploy
            deploy docker
            deploy [-S server]

        Build Project

        Options:
        -h --help                             Print usage
        -S server --server=SERVER       sequence execute object
    """

    def execute(self):
        if self.args['docker']:
            deploy_utils.docker_deploy()