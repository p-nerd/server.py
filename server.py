import json
import os
import socket
import sys

from utilities import Headers, to_params_dict
import sta


def handle_request(client: socket, client_address):
    request: list[str] = client.recv(1024).decode("utf-8").split("\n")

    first_row: list[str] = request[0].split(" ")
    request_headers = Headers(first_row[0], first_row[1])

    response = None
    if request_headers.http_method == "GET":
        response = sta.get(request_headers)

    elif request_headers.http_method == "POST":
        params_body: dict = to_params_dict(request)
        response = sta.post(request_headers, params_body)

    print(f"{Headers.count_request}: {request_headers.http_method}", end="")
    print(f"\t-> {client_address}")

    response_status = response[1] + "\n\n"
    response_body = json.dumps(response[0])
    final_response = "HTTP/1.1 " + response_status + response_body

    client.sendall(bytes(final_response, encoding="utf-8"))


def server(host: str, port: int):
    server_address = host, port

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(3)
    print(f"Serving on {server_address}...\n")

    while True:
        client_socket, client_address = server_socket.accept()
        pid = os.fork()
        if pid == 0:
            server_socket.close()
            handle_request(client_socket, client_address)
            client_socket.close()
            os._exit(os.EX_OK)
        else:
            client_socket.close()


if __name__ == "__main__":
    server("192.168.0.4", int(sys.argv[1]))
