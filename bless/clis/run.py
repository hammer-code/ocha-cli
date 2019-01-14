from bless.clis.base import Base
from bless.libs import run_utils
import os


CURR_DIR = os.getcwd()

class Run(Base):
    """
        usage:
            run
            run [-p PATH]

        Run Project

        Options:
        -h --help                             Print usage
        -p path --path=PATH                   Build to own path
    """

    def execute(self):
        config_yml = run_utils.utils.yaml_read(CURR_DIR+"/config.ocha")
        build_yml = run_utils.utils.yaml_read(CURR_DIR+"/.deploy/build.ocha")
        run_utils.execute_project(config_yml, build_yml)