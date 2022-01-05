from utilities import Headers
import json

# This functions will be return a dict of data
# HTTP status code in str like: "200 OK"


def home(headers: Headers):
    print(headers)
    return {"State": "In Home"}, "200 OK"


def about(headers: Headers):
    print(headers)
    return {"State": "In About"}, "200 OK"


def users(headers: Headers, data: dict):
    print(headers)
    name: str = data["user_name"]
    data = json.dumps(data, indent=4)
    with open(f"data/{name}.json", "wt") as file:
        file.write(data)
    return {"status": "users created"}, "201 Created"


get_urls = {
    "/home": home,
    "/about": about
}

post_urls = {
    "/users": users
}
