from bless.clis.base import Base
from bless.libs import run_utils, scp_utils
import os


CURR_DIR = os.getcwd()

class Run(Base):
    """
        usage:
            run
            run [-p PATH]
            run neo
            run neo [-a ACTION]

        Run Project

        Options:
        -h --help                             Print usage
        -p path --path=PATH                   Build to own path
        -a action --action=ACTION             start or stop neo service
    """

    def execute(self):
        deploy_data = run_utils.utils.yaml_read(CURR_DIR+"/.deploy/deploy.ocha")
        config = run_utils.utils.yaml_read(CURR_DIR+"/config.ocha")
        app_name = config['config']['app']['name']
        app_port = config['config']['app']['port']
        host = deploy_data['ip']
        username = deploy_data['username']
        key = CURR_DIR+"/.deploy/ssh_key.pem"

        if self.args['neo']:
            if self.args['--action'] == 'start':
                ssh = scp_utils.ssh_connect(host, username, key_filename=key)
                ssh.get_transport().is_active()
                ssh.exec_command("cd "+app_name+"; bless run;")
                ssh.close()
                exit()
            if self.args['--action'] == "stop":
                ssh = scp_utils.ssh_connect(host, username, key_filename=key)
                ssh.get_transport().is_active()
                ssh.exec_command("kill  $(lsof -t -i:"+str(app_port)+")")
                ssh.close()
                exit()

        config_yml = run_utils.utils.yaml_read(CURR_DIR+"/config.ocha")
        build_yml = run_utils.utils.yaml_read(CURR_DIR+"/.deploy/build.ocha")
        run_utils.execute_project(config_yml, build_yml)
