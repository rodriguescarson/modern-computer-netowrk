import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9918))

server.listen()
while True:
    client, address = server.accept()
    print(f"Connect to {address}")
    print(client.recv(1024).decode('utf-8'))
    client.send("Server:Hello world".encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))
    client.send("Server: Bye!".encode('utf-8'))
    client.close()
