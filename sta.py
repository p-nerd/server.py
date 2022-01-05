from utilities import Headers
import api


# This functions will be return a dict of data
# HTTP status code in str like: "200 OK"

def not_found(e):
    return {
        "status": "not found",
        "error": f"{e.__doc__}"
    }, "404 Not Found"


def get(headers: Headers):
    try:
        fnc = api.get_urls[headers.path]
        data = fnc(headers)
    except Exception as e:
        data = not_found(e)

    return data


def post(headers: Headers, data: dict):
    try:
        fnc = api.post_urls[headers.path]
        res_data = fnc(headers, data)
    except Exception as e:
        res_data = not_found(e)

    return res_data
