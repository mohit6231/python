import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
server_address = ('localhost', 65432)
server_socket.bind(server_address)

print("UDP Server is listening on port 65432...")

while True:
    # Receive message from the client
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received: {data.decode()} from {client_address}")

    # Send the same message back to the client
    if data:
        server_socket.sendto(data, client_address)
