#!/usr/bin/python3
import socket
import json


HOST = "127.0.0.1"
PORT = 65432


def start_server():
    """
    Starts a server that listens for a client connection,
    receives serialized JSON data, deserializes it,
    and prints the received dictionary.
    """
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)

        conn, addr = server_socket.accept()
        data = conn.recv(4096)

        if data:
            received_dict = json.loads(data.decode("utf-8"))
            print("Received Dictionary from Client:")
            print(received_dict)

        conn.close()
        server_socket.close()

    except (socket.error, json.JSONDecodeError):
        pass


def send_data(data):
    """
    Connects to the server, serializes a dictionary using JSON,
    and sends it over the network.
    """
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))

        serialized_data = json.dumps(data).encode("utf-8")
        client_socket.sendall(serialized_data)

        client_socket.close()

    except socket.error:
        pass
