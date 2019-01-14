from bless.libs import utils
from bless.libs import parsing as parse
import os, json


def check_init(path):
    path_file = path+"/init.ocha"
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
    utils.create_file("bless.ocha",deploy_path, val)


def build(path, md_check= None):
    deploy_path = path+"/.deploy"
    path_bless = deploy_path+"/bless.ocha"
    app_path = parse.initialize(path_bless, sync_md=md_check)
    run_path = {
        "source_path": "",
        "build_path": app_path
    }
    utils.yaml_writeln(run_path,deploy_path+"/build.ocha")
    file = utils.list_dir(path)
    utils.yaml_writeln(file,deploy_path+"/listdir.ocha")
