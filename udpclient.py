import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("Hello Server".encode('utf-8'), ("127.0.0.1", 9988))
print(client.recvfrom(1024)[0].decode('utf-8'))
