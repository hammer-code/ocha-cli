from bless.clis.base import Base
from bless.libs import login_utils
import os


class Logout(Base):
    """
        usage:
            logout

        Build Project

        Options:
        -h --help                             Print usage
    """

    def execute(self):
        login_utils.logout()