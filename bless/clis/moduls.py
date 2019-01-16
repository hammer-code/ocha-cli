from bless.clis.base import Base
from bless.libs import modul_utils
from bless.libs import parsing_utils
from bless.libs import scp_utils
import os


CURR_DIR = os.getcwd()

class Moduls(Base):
    """
        usage:
            moduls create [-f File]
            moduls sync
            moduls sync [-f File] [-s SERVER]

        Build Project

        Options:
        -m --moduls               Sync Moduls
        -h --help                             Print usage
        -f PATH --file=PATH       sequence execute object
    """

    def execute(self):
        app_path = CURR_DIR
        nm_modul = None
        if self.args['create']:
            check_file = modul_utils.utils.list_dir(CURR_DIR+"/moduls/")
            print(len(check_file))
            if len(check_file) > 0:
                print("Warning: Moduls Not Empty, All Modules Will Be Removed If Agree ")
                person_agre = input("Press |Y| If Agree : ")
                if person_agre == "Y" or person_agre == "y":
                    modul_utils.utils.remove_folder(CURR_DIR+"/moduls/")
                    modul_utils.utils.create_folder(CURR_DIR+"/moduls/")
                else:
                    exit()
            endpoint_data = None
            if self.args['--file']:
                file = self.args['--file']
                endpoint_data = modul_utils.utils.yaml_read(file)['endpoint']
            else:
                endpoint_data = modul_utils.utils.yaml_read(CURR_DIR+"/endpoint.ocha")['endpoint']
            for key_i in endpoint_data:
                for end_i in endpoint_data[key_i]:
                    modules_data = None
                    try:
                        modules_data = endpoint_data[key_i][end_i]['moduls']
                    except Exception:
                        modules_data = None
                    if modules_data:
                        for nm_moduls in modules_data:
                            if nm_modul == nm_moduls:
                                parsing_utils.add_function_moduls(nm_modul,modules_data, app_path, sync_md=True)
                                nm_modul = nm_moduls
                            else:
                                parsing_utils.create_moduls(nm_moduls,modules_data, app_path, sync_md=True)
                                nm_modul = nm_moduls
        if self.args['sync']:
            config_data = modul_utils.utils.yaml_read(CURR_DIR+"/config.ocha")['config']
            app_name = config_data['app']['name']
            listsdir = modul_utils.utils.list_dir(CURR_DIR+"/moduls/")
            deploy_data = modul_utils.utils.yaml_read(CURR_DIR+"/.deploy/deploy.ocha")
            host = deploy_data['ip']
            username = deploy_data['username']
            key = CURR_DIR+"/.deploy/ssh_key.pem"

            ssh = scp_utils.ssh_connect(host, username, key_filename=key)
            ssh.get_transport().is_active()
            ftp_client= ssh.open_sftp()

            for i in listsdir:
                scp_utils.sync_file(ftp_client,i['file'], "/home/"+username+"/"+i['index'])
            ftp_client.close()
            for command in listsdir:
                # ssh.exec_command("sudo cp /home/"+username+"/"+i['index']+" /root/BLESS/"+app_name+"/app/moduls/")
                ssh.exec_command("sudo mv /home/"+username+"/"+command['index']+" /root/")
            ssh.close()
            exit()