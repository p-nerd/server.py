from classes import Request
import socket
import os
import sys
import api
import json


HTTP_HEADER = b"HTTP/1.1 200 OK\n\n"


def handle_request(client: socket) -> None:
    request_header: list[str] = client.recv(1024).decode("utf-8").split("\n")

    http_method, path, request_type = request_header[0].split(" ")

    if request_type[:4] == "HTTP":
        print("Got HTTP request!")
        data = json.dumps(api.main(Request(http_method, path)))
        client.sendall(HTTP_HEADER + bytes(data, encoding="utf-8"))


def server(host: str, port: int) -> None:
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
