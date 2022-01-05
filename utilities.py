import json
import os


class Headers:
    def __init__(self, http_method: str, path: str):
        self.http_method = http_method
        self.path = path


def to_params_dict(data: list) -> dict:
    index = -1
    if '\n' in data:
        index = data.index('\n')
    elif '\r' in data:
        index = data.index('\r')
    data = data[index + 1:]

    st_data = ""
    for i in data:
        st_data += i

    with open("blablabla.json", "wt") as file:
        file.write(st_data)
    with open("blablabla.json", "rt") as file:
        data = json.load(file)
    os.remove("blablabla.json")
    return data
