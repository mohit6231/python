import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server_address = ('localhost', 65432)

# Send data to the server
message = "Hello, UDP Server!"
client_socket.sendto(message.encode(), server_address)

# Receive response from the server
data, server = client_socket.recvfrom(1024)
print(f"Received: {data.decode()}")

# Close the socket
client_socket.close()
