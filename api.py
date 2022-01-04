from classes import Request


def main(header: Request) -> dict:
    data = {
        "title": "server.py",
        "programmer": "Shihab Mahamud",
        "http_method": header.http_method,
        "path": header.path
    }

    return data
