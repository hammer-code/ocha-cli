from passlib.hash import pbkdf2_sha256
from bless.libs import utils
import os, docker

APP_HOME = utils.APP_HOME
DEFAULT_PROJECT = "http://103.93.53.46"
DEFAULT_PORT = "6969"

def create_env_file(username, password, auth_url = None, port = None):
    url_a = port
    port_a = auth_url
    if auth_url is None:
        url_a = DEFAULT_PROJECT

    if port is None:
        port_a = DEFAULT_PORT

    try:
        env_file = open("{}/.bless.env".format(APP_HOME), "w+")
        env_file.write("OS_USERNAME=%s\n" % username)
        env_file.write("OS_PASSWORD=%s\n" % password)
        env_file.write("OS_PROJECT_URL=%s\n" % url_a)
        env_file.write("OS_PROJECT_PORT=%s\n" % port_a)
        env_file.close()
        return True
    except Exception as e:
        print(e)
        return False


def login_neo(username, password, auth_url = None, port=None):
    if os.path.exists(APP_HOME+"/.bless.env"):
        print("Environment Exists Do You remove :")
        checks = input("Y/N")
        if checks == 'Y' or checks == 'y':
            os.remove(APP_HOME+"/.bless.env")
            create_env_file(username, password, auth_url, port)
        else:
            env = utils.get_env_values()
            print(env['username'])

    create_env_file(username, password, auth_url, port)


def login(username, password):
    pasword_hash = pbkdf2_sha256.hash(password)
    login_neo(username, pasword_hash)


def login_docker():
    os.system("docker login")


def logout():
    if os.path.exists(APP_HOME+"/.bless.env"):
        os.remove(APP_HOME+"/.bless.env")
    else:
        print("Not Current Sessions")


