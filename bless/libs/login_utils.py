from passlib.hash import pbkdf2_sha256
from bless.libs import utils
import os

APP_HOME = utils.APP_HOME


def create_env_file(username, password, auth_url = None):
    url_a = None
    if not auth_url:
        url_a = auth_url

    try:
        env_file = open("{}/.bless.env".format(APP_HOME), "w+")
        env_file.write("OS_USERNAME=%s\n" % username)
        env_file.write("OS_PASSWORD=%s\n" % password)
        env_file.write("OS_AUTH_URL=%s\n" % url_a)
        env_file.close()
        return True
    except Exception as e:
        print(e)
        return False


def login_neo(username, password, auth_url = None):
    create_env_file(username, password, auth_url)

def login(username, password):
    login_neo(username, password)

def logout():
    print("LOGOUT")


