from bless.clis.base import Base
from bless.libs import modul_utils, parsing_utils
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
                endpoint_data = modul_utils.utils.yaml_read("endpoint.ocha")['endpoint']
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