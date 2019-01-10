import docker, requests


# deploying in docker
def check_image(bless_object):
    print(bless_object)


def docker_deploy():
    client = docker.from_env()
    list_image = client.images.list()
    print(list_image)


# Deploying in neo service
def neo_deploy(bless_object, app_path):
    files = {'upload_file': open('file.txt','rb')}
    values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}
    url = ""
    r = requests.post(url, files=files, data=values)
    return r