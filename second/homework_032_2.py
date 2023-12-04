# Topic 32
# Task 2

import socket
import pickle


def caesar_cipher(text, key):
    user_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                shifted = (ord(char) + key - 65) % 26 + 65
                user_text += chr(shifted)
            elif char.islower():
                shifted = (ord(char) + key - 97) % 26 + 97
                user_text += chr(shifted)
        else:
            user_text += char
    return user_text


def handle_client(client_socket):
    data = client_socket.recv(1024)
    message = pickle.loads(data)
    text = message["text"]
    key = message["key"]
    encrypted_text = caesar_cipher(text, key)
    client_socket.sendall(pickle.dumps({"encrypted_text": encrypted_text}))

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        handle_client(client_socket)
        client_socket.close()