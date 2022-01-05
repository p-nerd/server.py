from utilities import Headers
import api

# This functions will be return a dict of data
# HTTP status code in str like: "200 OK"


def get(headers: Headers):
    data = {}
    if headers.path == "/home":
        data = api.home(headers)
    if headers.path == "/about":
        data = api.about(headers)
    return data


def post(headers: Headers, data: dict):
    res_data = {}
    if headers.path == "/users":
        res_data = api.users(headers, data)
    return res_data
