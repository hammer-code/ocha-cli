from app.libs import utils
from app.helpers.rest import response
from importlib import import_module

def endpoint_parser(command, data):
    func_name = None
    func_attr = None
    func_params = None
    for i in data:
        if i == "moduls":
            if data[i] != None:
                for a in data[i]:
                    func_name = data[i][a]['action']
                    func_moduls = import_module("app.moduls."+a)
                    if data[i][a]['parameters'] != None:
                        func_params = data[i][a]['parameters']
                        data_params = dict()
                        for e in func_params:
                            if func_params[e].find("$") == -1:
                                data_params[e] = func_params[e]
                            else:
                                keys_data = func_params[e].split("$")[1]
                                data_params[e] = data['data'][0][keys_data]
                        func_attr = getattr(func_moduls, func_name)(data_params)
                    else: 
                        func_attr = getattr(func_moduls, func_name)()
    return func_attr


def get_paramsdata(tags):
    pass
