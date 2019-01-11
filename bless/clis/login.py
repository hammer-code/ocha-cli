from bless.clis.base import Base
from bless.libs import login_utils
from getpass import getpass
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
        username = input("Username: ")
        password = getpass("Password: ")
        login_utils.login(username , password)