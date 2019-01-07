from bless.libs import utils


def create_yml(path=None):
    default_path = utils.APP_HOME
    if path:
        default_path = path
    