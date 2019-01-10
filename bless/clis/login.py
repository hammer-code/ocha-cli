from bless.clis.base import Base
from bless.libs import login_utils
import os


CURR_DIR = os.getcwd()

class Login(Base):
    """
        usage:
            login

        Build Project

        Options:
        -h --help                             Print usage
    """

    def execute(self):
        login_utils.login("user","pass")