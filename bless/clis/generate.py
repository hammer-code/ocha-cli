from bless.clis.base import Base
from bless.libs import parsing as parse
import os

class Generate(Base): 
    """
        usage:
            generate [-f FILE]
            generate [-g GITHUB]

        Build Yaml File
        Options:
        -h --help                             Print usage
        -f file --file=FILE                   Build bless object to microservice
    """

    def execute(self):
        if self.args['--file']:
            parse.initialize(self.args['--file'])
            exit()
        if self.args['--github']:
            pass
