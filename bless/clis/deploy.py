from bless.clis.base import Base
import os


CURR_DIR = os.getcwd()

class Build(Base):
    """
        usage:
            deploy
            deploy [-S server]

        Build Project

        Options:
        -h --help                             Print usage
        -S server --server=SERVER       sequence execute object
    """

    def execute(self):
        print(self.args)