import paramiko
import os
from bless.libs import utils

CURR_DIR = os.getcwd()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
deploy_data = utils.yaml_read(CURR_DIR+"/.deploy/deploy.ocha")


def ssh_connect(host, username, port=None, password=None, key_filename=None):
    try:
        ssh.connect(host, username=username, port=port, password=password, key_filename=key_filename)
    except Exception as e:
        print(e)
        raise e
    else:
        return ssh


def sync_file(path_file, path_remote):
    host = deploy_data['ip']
    username = deploy_data['username']
    key = utils.read_value(CURR_DIR+"/.deploy/ssh_key.pem")
    ssh = ssh_connect(host, username, key_filename=key)
    ftp_client= ssh.open_sftp()
    ftp_client.put(path_file, path_remote)
    ftp_client.close()
    ssh.close()