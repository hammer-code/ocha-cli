from bless.clis.base import Base
from bless.libs import parsing as parse

class Generate(Base): 
    """
        usage:
            generate [-f FILE]

        Build Yaml File
        Options:
        -h --help                             Print usage
        -f file --file=FILE                   Build yaml file
    """

    def execute(self):
        parse.initialize(self.args['--file'])
        exit()
