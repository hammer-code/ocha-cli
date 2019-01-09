from bless.libs import utils
from bless.libs import parsing as parse
import os, json


def list_dir(dirname):
    listdir = list()
    for root, dirs, files in os.walk(dirname):
        for file in files:
            data = {
                "index": file,
                "file": os.path.join(root, file)
            }
            listdir.append(data)
    return listdir

def check_init(path):
    path_file = path+"/init.yml"
    check = utils.read_file(path_file)
    return check

def initialite(init, path):
    deploy_data = init['deploy']
   
    # check deploy folder
    deploy_path = path+"/.deploy"
    if utils.check_folder(deploy_path):
        utils.remove_folder(deploy_path)

    utils.create_folder(deploy_path)
    
    val = ""
    for i in deploy_data:
        val += utils.read_value(path+"/"+deploy_data[i]['file'])
        val += "\n"
    utils.create_file("bless.yml",deploy_path, val)


def deploy(path):
    deploy_path = path+"/.deploy"
    path_bless = deploy_path+"/bless.yml"
    # print(utils.read_file(path_bless))
    parse.initialize(path_bless)
