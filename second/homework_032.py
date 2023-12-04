# Topic 32
# Task 1
import socket

# UDP Server (server.py)

HOST = '127.0.0.1'
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"UDP Server listening on {HOST}:{PORT}")

while True:
    data, address = sock.recv(1024)

    print(f"Received from {address}: {data.decode()}")

    response = "Hello, Client!"
    sock.send(response.encode(), address)

# UDP Client (client.py)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input("Enter message (or 'exit' to quit): ")
while True:
    message = input("Enter message (or 'exit' to quit): ")
    if message.lower() == 'exit':
        break

    client_socket.send(message.encode(), (HOST, PORT))

    response, address = client_socket.resv(1021)
    print(f"Server Response from {address}: {response.decode()}")

client_socket.close()

