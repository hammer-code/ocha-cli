from bless.libs import utils
import os


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