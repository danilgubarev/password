import os

def path_search(file_name):
    abs_path = __file__.split("/")
    for i in range(2):
        del abs_path[-1]
    abs_path = "/".join(abs_path)
    abs_path = os.path.join(abs_path, path_search)
    return abs_path