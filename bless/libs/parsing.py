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
    security = None
    for i in endpoint_data:
        try:
            security = endpoint_data[i]['auth']
        except Exception:
            security = None
        utils.create_file_controller(i, app_path, security)

    # setup routing
    utils.create_routing(endpoint_data, app_path)

    # create moduls
    nm_modul = None
    for key_i in endpoint_data:
        for end_i in endpoint_data[key_i]:
            modules_data = None
            try:
                modules_data = endpoint_data[key_i][end_i]['moduls']
            except Exception as e:
                modules_data = None
            if modules_data:
                for nm_moduls in modules_data:
                    if nm_modul == nm_moduls:
                        utils.add_function_moduls(nm_modul,modules_data, app_path)
                        nm_modul = nm_moduls
                    else:
                        utils.create_moduls(nm_moduls,modules_data, app_path)
                        nm_modul = nm_moduls