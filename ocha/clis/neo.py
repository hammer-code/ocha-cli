from ocha.clis.base import Base
from ocha.libs import parsing as parse
import os

class Neo(Base): 
    """
        usage:
            neo activate
            neo deactivate

        Options:
        -h --help                             Print usage
    """

    def execute(self):
        if self.args['activate']:
            print("ACTIVATED NEO SERVICE")
            exit()
        if self.args['deactivate']:
            print("DEACTIVATED NEO SERVICE")
            exit()
