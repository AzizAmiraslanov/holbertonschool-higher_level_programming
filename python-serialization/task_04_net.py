#!/usr/bin/python3
import socket
import json


HOST = "127.0.0.1"
PORT = 65432


def start_server():
    """
    Starts a server that receives a serialized dictionary from a client,
    deserializes it, and prints it.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))
            server_socket.listen(1)

            conn, addr = server_socket.accept()
            with conn:
                data = conn.recv(4096)
                if data:
                    received_dict = json.loads(data.decode("utf-8"))
                    print("Received Dictionary from Client:")
                    print(received_dict)

    except (socket.error, json.JSONDecodeError):
        pass


def send_data(data):
    """
    Acts as a client: serializes a dictionary and sends it to the server.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            serialized_data = json.dumps(data).encode("utf-8")
            client_socket.sendall(serialized_data)

    except socket.error:
        pass
