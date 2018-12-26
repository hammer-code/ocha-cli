from bless.libs import utils


def initialize(file=None):
    obj_data = utils.yaml_parser(file)
    # Create APP
    app_name =  obj_data['config']['app']['name']
    app_framework =  obj_data['config']['app']['framework']

    if not utils.read_app(app_name):
        create_app = utils.create_app(app_name, app_framework)
    # create environment
    app_path = utils.read_app(app_name)
    if not utils.read_file(app_path+"/.env"):
        utils.create_env(obj_data['config'], app_path)

    # setup endpoint
    endpoint_data = obj_data['endpoint']
    utils.set_endpoint_template(endpoint_data, app_path)
    for i in endpoint_data:
        utils.create_file_controller(i, app_path)

    utils.create_routing(endpoint_data, app_path)