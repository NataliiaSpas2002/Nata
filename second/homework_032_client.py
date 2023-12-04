# Topic 32
# Task 2 client

import socket
import pickle


def send_message(text, key):
    message = {"text": text, "key": key}
    return pickle.dumps(message)


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    plaintext = "Hello, World!"
    key = 5

    message = send_message(plaintext, key)
    client_socket.sendall(message)

    data = client_socket.recv(1024)
    response = pickle.loads(data)
    encrypted_text = response["encrypted_text"]

    print("Encrypted text:", encrypted_text)

    client_socket.close()

