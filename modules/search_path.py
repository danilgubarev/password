import json
import os


def path_search(name_file):
    abs_path = __file__.split("/")
    del abs_path[-1]
    abs_path = "/".join(abs_path)
    abs_path = os.path.join(abs_path, name_file)
    return name_file

def create_json(file_to_path, name_dict):
    with open(path_search(file_to_path),"w") as file:
        json.dump(name_dict, file, ensure_ascii= False, indent= 4)

def read_json(name_dict):
    with open(path_search(name_dict["name"],"r")) as file:
        json.load(file)
