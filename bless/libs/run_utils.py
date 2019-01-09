from bless.libs import utils
import os, stat

def execute_project(cfg_object, build_yml, path=None):
    build_path = build_yml['build_path']
    app_env = cfg_object['config']['app']['environment']
    if app_env == 'production':
        st = os.stat(build_path+"/production.sh")
        os.chmod(build_path+"/production.sh", st.st_mode | stat.S_IEXEC)
        os.system("cd "+build_path)
        os.system("pwd")
        os.system("bash "+build_path+"/production.sh")
    else:
        os.system("python "+build_path+"/manage.py server")
