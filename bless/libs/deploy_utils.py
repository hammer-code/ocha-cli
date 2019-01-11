import docker, requests
from passlib.hash import pbkdf2_sha256
from bless.libs import utils
from getpass import getpass


# deploying in docker
def check_image(bless_object):
    print(bless_object)


def docker_deploy():
    client = docker.from_env()
    list_image = client.images.list()
    print(list_image)


# Deploying in neo service
def neo_deploy(bless_object, app_path):
    env_data = utils.get_env_values()
    password = getpass("Your Neo Password: ")
    password_unhash = pbkdf2_sha256.verify(password, env_data['password'])
    head_url = env_data['project_url']+":"+env_data['project_port']
    auth = None
    if not password_unhash:
        print("Password Wrong")
        exit()
    else:
        url_login = head_url+"/api/sign"
        auth = utils.sign_to_project(url_login,env_data['username'], password) 
    auth = auth['data']['token']
    files = {'bless_file': open(app_path+"/.deploy/bless.yml",'rb')}

    headers = {
        "Authorization": auth
    }
    values = {
        'app_name': bless_object['config']['app']['name'],
        'app_port': bless_object['config']['app']['port'],
        'username': env_data['username'],
    }

    respons = requests.post(head_url+"/api/project", files=files, data=values, headers=headers)
    return respons.json()