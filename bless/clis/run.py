from bless.clis.base import Base
from bless.libs import run_utils, scp_utils
import os


CURR_DIR = os.getcwd()

class Run(Base):
    """
        usage:
            run
            run [-p PATH]
            run neo [-a ACTION]

        Run Project

        Options:
        -h --help                             Print usage
        -p path --path=PATH                   Build to own path
        -a action --action=ACTION             start, stop and status neo service
    """

    def execute(self):
        if self.args['neo']:
            deploy_data = run_utils.utils.yaml_read(CURR_DIR+"/.deploy/deploy.ocha")
            config = run_utils.utils.yaml_read(CURR_DIR+"/config.ocha")
            app_name = config['config']['app']['name']
            app_port = config['config']['app']['port']
            host = deploy_data['ip']
            username = deploy_data['username']
            key = CURR_DIR+"/.deploy/ssh_key.pem"
            
            if self.args['--action'] == 'start':
                ssh = scp_utils.ssh_connect(host, username, key_filename=key)
                ssh.get_transport().is_active()
                _,stdout,_ = ssh.exec_command("cd "+app_name+"; bless run;")
                status = stdout.read().decode("utf8")
                print("###################################################")
                print("REPORT: Neo Service Started")
                print("###################################################")
                print(status)
                print("###################################################")
                ssh.close()
                exit()

            if self.args['--action'] == "stop":
                ssh = scp_utils.ssh_connect(host, username, key_filename=key)
                ssh.get_transport().is_active()
                ssh.exec_command("kill  $(lsof -t -i:"+str(app_port)+")")
                _,stdout,_ = status = stdout.read().decode("utf8")
                print("###################################################")
                print("REPORT: Neo Service Stopped")
                print("###################################################")
                print(status)
                print("###################################################")
                ssh.close()
                exit()

            if self.args['--action'] == "status":
                ssh = scp_utils.ssh_connect(host, username, key_filename=key)
                ssh.get_transport().is_active()
                _,stdout,_ = ssh.exec_command("lsof -i -P -n | grep "+str(app_port))
                status = stdout.read().decode("utf8")
                if status:
                    print("###################################################")
                    print("REPORT: Your Neo Service Started")
                    print("###################################################")
                    print(status)
                    print("###################################################")
                else:
                    print("###################################################")
                    print("REPORT: Your Neo Not Started")
                    print("###################################################")
                ssh.close()
                exit()
            print("REPORT: run neo -a <action>  | action : status | start | stop")
            exit()

        config_yml = run_utils.utils.yaml_read(CURR_DIR+"/config.ocha")
        build_yml = run_utils.utils.yaml_read(CURR_DIR+"/.deploy/build.ocha")
        run_utils.execute_project(config_yml, build_yml)
