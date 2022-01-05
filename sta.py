from utilities import Headers


def get(header: Headers):

    data = {
        "title": "server.py",
        "programmer": "Shihab Mahamud",
        "http_method": header.http_method,
        "path": header.path
    }
    return data, "201 OK"


def post(header: Headers, sented: dict):
    data = {
        "title": "server.py",
        "programmer": "Shihab Mahamud",
        "http_method": header.http_method,
        "path": header.path,
        "seated_data": sented
    }
    return data, "200 OK"
