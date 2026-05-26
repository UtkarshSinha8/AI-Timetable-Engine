import json


def load_json_file(file_path: str):

    with open(file_path, "r") as file:

        return json.load(file)