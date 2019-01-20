from ocha.clis.base import Base
from ocha.libs import build_utils
from ocha.libs import database
from ocha.libs import parsing_utils
from ocha.libs import scp_utils
import os


CURR_DIR = os.getcwd()

class Build(Base):
    """
        usage:
            build [-m | --moduls]
            build database [-f File]
            build endpoint [-s SERVICE]

        Build Project

        Options:
        -h --help                                   Print usage
        -m --moduls                                 Sync Moduls
        -s service --service=SERVICE                Sync Moduls
        -f file --file=FILE                         sequence execute object
    """

    def execute(self):
        if self.args['database']:
            file = self.args['--file']
            config = build_utils.utils.yaml_read("config.ocha")['config']
            database_obj = build_utils.utils.yaml_read(file)['database']
            config = config['database']
            if config['host'] == "localhost" or config['host'] == "127.0.0.1":
                database.database_parse(config, database_obj,
                                            security = None, auth_config = None)
            build_utils.utils.report("Database Build")
            exit()

        if self.args['endpoint']:
            if self.args['--service']=='neo':
                config = build_utils.utils.yaml_read("config.ocha")['config']
                app_name = config['app']['name']
                if not build_utils.utils.read_file(CURR_DIR+"/.deploy/deploy.ocha"):
                    build_utils.utils.report("WARNING", "Your Neo Serice Not Activate")
                    exit()
                endpoint_file = CURR_DIR+"/endpoint.ocha"
                deploy_data = build_utils.utils.yaml_read(CURR_DIR+"/.deploy/deploy.ocha")
                host = deploy_data['ip']
                username = deploy_data['username']
                key = CURR_DIR+"/.deploy/ssh_key.pem"
                ssh = scp_utils.ssh_connect(host, username, key_filename=key)
                ssh.get_transport().is_active()
                ftp_client= ssh.open_sftp()
                scp_utils.sync_file(endpoint_file,file, "/home/"+username+"/"+app_name+"/endpoint.ocha")
                ftp_client.close()
                _,stdout,_ = ssh.exec_command("cd /home/"+username+"/"+app_name+"; ocha build endpoint")
                status = stdout.read().decode("utf8")
                build_utils.utils.report("SYNC ENDPOINT TO NEO SERVICE")
                build_utils.utils.log_warn(status)
                ssh.close()
                exit()
            endpoint_data = build_utils.utils.yaml_read("endpoint.ocha")['endpoint']
            config = build_utils.utils.yaml_read("config.ocha")['config']
            build_data = build_utils.utils.yaml_read(CURR_DIR+"/.deploy/build.ocha")
            app_path = build_data['build_path']
            if not build_utils.utils.check_folder(app_path):
                build_utils.utils.log_err("Failed Build Your App Now")
                exit()
            if build_utils.utils.read_file(app_path+"/app/static/templates/endpoint.yml"):
                os.remove(app_path+"/app/static/templates/endpoint.yml")
            parsing_utils.set_endpoint_template(endpoint_data, app_path)
            security = None
            for i in endpoint_data:
                try:
                    security = endpoint_data[i]['auth']
                except Exception:
                    security = None
                if build_utils.utils.read_file(app_path+"/app/controllers/api/"+i+".py"):
                    os.remove(app_path+"/app/controllers/api/"+i+".py")
                parsing_utils.create_file_controller(i, app_path, security)
            parsing_utils.create_routing(endpoint_data, app_path)
            exit()

        init_create = dict()
        init_yml = dict()
        init_file = None
        if not build_utils.check_init(CURR_DIR):
            list_dir = build_utils.utils.list_dir(CURR_DIR)
            for i in list_dir:
                index = i['index'].split(".")
                init_create[index[0]] = {
                    "file": i['index']
                }
            init_yml['deploy'] = init_create
            build_utils.utils.yaml_create(init_yml,CURR_DIR+"/init.ocha")
            init_file = build_utils.utils.yaml_read(CURR_DIR+"/init.ocha")
        else:
            init_file = build_utils.utils.yaml_read(CURR_DIR+"/init.ocha")

        build_utils.initialite(init_file, CURR_DIR)
        moduls_check = self.args['--moduls']
        build_utils.build(CURR_DIR, md_check=moduls_check)