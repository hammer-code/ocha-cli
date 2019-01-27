from ocha.clis.base import Base
from ocha.libs import modul_utils
from ocha.libs import parsing_utils
from ocha.libs import scp_utils
import os


CURR_DIR = os.getcwd()
URLS_MODULS = "https://github.com/Blesproject/ocha_moduls.git"


class Moduls(Base):
    """
        usage:
            moduls create [-f File] [-l | --libs]
            moduls sync
            moduls sync [-f File] [-s SERVICE]

        Build Project

        Options:
        -l --libs                           Sync Moduls
        -h --help                           Print usage
        -f path --file=PATH                 sequence execute object
        -s service --service=SERVICE        sequence execute object
    """

    def execute(self):
        app_path = CURR_DIR
        nm_modul = None


        if self.args['create']:
            check_file = modul_utils.utils.list_dir(CURR_DIR+"/moduls/")
            print(len(check_file))
            if len(check_file) > 0:
                modul_utils.utils.log_warn("Moduls Not Empty, All Modules Will Be Removed If Agree")
                person_agre = modul_utils.utils.question("If Agree and Not Agree : ")
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

            if self.args['--libs']:
                if modul_utils.utils.check_folder(CURR_DIR+"/moduls/app"):
                    modul_utils.utils.log_warn("Library Exist")
                    exit()
                url = URLS_MODULS
                git = modul_utils.utils.template_git(url, CURR_DIR+"/moduls/")
                if not git:
                    modul_utils.utils.log_err("Check Your Internet Connection")
                    exit()
                os.remove(CURR_DIR+"/moduls/.gitignore")
                modul_utils.utils.remove_folder(CURR_DIR+"/moduls/.git")
                modul_utils.utils.report("Library Run Moduls In Project Success Installed")
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
            exit()
        if self.args['sync']:
            config_data = modul_utils.utils.yaml_read(CURR_DIR+"/config.ocha")['config']
            app_name = config_data['app']['name']
            listsdir = modul_utils.utils.list_dir(CURR_DIR+"/moduls/")
            file = None

            if self.args['--file']:
                file = self.args['--file']

            if self.args['--service'] == 'neo':
                if not modul_utils.utils.read_file(CURR_DIR+"/.deploy/deploy.ocha"):
                    modul_utils.utils.log_err("Your Neo Service Not Activate")
                    exit()
                deploy_data = modul_utils.utils.yaml_read(CURR_DIR+"/.deploy/deploy.ocha")
                host = deploy_data['ip']
                username = deploy_data['username']
                key = CURR_DIR+"/.deploy/ssh_key.pem"
                ssh = scp_utils.ssh_connect(host, username, key_filename=key)
                ssh.get_transport().is_active()
                ftp_client= ssh.open_sftp()
                # check file
                if file:
                    modul_utils.utils.report("Syncs "+file+" To Neo Service")
                    scp_utils.sync_file(ftp_client,file, "/home/"+username+"/"+app_name+"/"+file)
                    ftp_client.close()
                    ssh.exec_command("mv /home/"+username+"/"+file+" /home/"+username+"/BLESS/"+app_name+"/app/moduls/")
                else:
                    modul_utils.utils.report("Syncs All Moduls To Neo Service")
                    for i in listsdir:
                        scp_utils.sync_file(ftp_client,i['file'], "/home/"+username+"/"+app_name+"/moduls/"+i['index'])
                    ftp_client.close()
                    for command in listsdir:
                        ssh.exec_command("mv /home/"+username+"/"+command['index']+" /home/"+username+"/BLESS/"+app_name+"/app/moduls/")
                ssh.close()

                modul_utils.utils.report("After sync moduls then build your endpoint in neo service")
                exit()

            modul_utils.utils.report("REPORT", "Sync Moduls Locals")
            if not modul_utils.utils.read_file(CURR_DIR+"/.deploy/build.ocha"):
                modul_utils.utils.log_err("To Sync Your Moduls Build Now")
                exit()
            build_data = modul_utils.utils.yaml_read(CURR_DIR+"/.deploy/build.ocha")
            build_path = build_data['build_path']
            build_path = build_path+"/app/"
            if file:
                modul_utils.utils.copyfile(file, build_path+"/"+file)
                exit()
            if modul_utils.utils.check_folder(build_path+"/moduls"):
                modul_utils.utils.remove_folder(build_path+"/moduls")
            modul_utils.utils.copy(CURR_DIR+"/moduls/", build_path+"/moduls")
            modul_utils.utils.report("Sync Moduls Success")
            modul_utils.utils.report("After sync moduls then build your endpoint")
            exit()