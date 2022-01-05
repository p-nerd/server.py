from utilities import Headers, to_params_dict
import sta
import json
import os
import socket
import sys


def handle_request(client: socket):
    request: list[str] = client.recv(1024).decode("utf-8").split("\n")

    first_row: list[str] = request[0].split(" ")
    request_headers = Headers(first_row[0], first_row[1])

    response = None
    if request_headers.http_method == "GET":
        response = sta.get(request_headers)

    elif request_headers.http_method == "POST":
        params_body: dict = to_params_dict(request)
        response = sta.post(request_headers, params_body)

    response_status = response[1] + "\n\n"
    response_body = json.dumps(response[0])
    final_response = "HTTP/1.1 " + response_status + response_body

    client.sendall(bytes(final_response, encoding="utf-8"))


def server(host: str, port: int):
    count_request = 0
    server_address = host, port

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(3)
    print(f"Serving on {server_address}...\n")

    while True:
        client_socket, client_address = server_socket.accept()
        count_request += 1
        print(f"{count_request}: -> {client_address}")

        pid = os.fork()
        if pid == 0:
            server_socket.close()
            handle_request(client_socket)
            client_socket.close()
            os._exit(os.EX_OK)
        else:
            client_socket.close()


if __name__ == "__main__":
    server("127.0.0.1", int(sys.argv[1]))
