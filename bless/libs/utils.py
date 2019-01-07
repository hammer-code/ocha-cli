import yaml
import os
import shutil
import git

APP_HOME = os.path.expanduser("~")
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def check_keys(obj, keys):
    chek = None
    try:
        chek = obj[keys]
    except Exception:
        return False
    else:
        return True


def template_git(url, dir):
    try:
        chk_repo = os.path.isdir(dir)
        if chk_repo:
            shutil.rmtree(dir)
        git.Repo.clone_from(url, dir)
        return True
    except Exception as e:
        print(e)
        return False


def yaml_parser(file):
    with open(file, 'r') as stream:
        try:
            data = yaml.load(stream)
            return data
        except yaml.YAMLError as exc:
            print(exc)

def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        print('Directory not copied. Error: %s' % e)


def read_file(file):
    if os.path.isfile(file):
        return True
    else:
        return False

def read_app(app_name, path=None):
    if path is None:
        app_path = APP_HOME+"/BLESS/"+app_name
    else:
        app_path = path+"/"+app_name
    if not os.path.exists(app_path):
        return None
    else:
        return app_path




