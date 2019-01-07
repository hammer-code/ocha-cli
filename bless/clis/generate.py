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
        -p path --path=PATH                   Build to own path
    """

    def execute(self):
        if self.args['--file']:
            parse.initialize(self.args['--file'])
            exit()
        if self.args['--path']:
            parse.initialize(file = self.args['--file'], path= self.args['--path'])
            exit()
