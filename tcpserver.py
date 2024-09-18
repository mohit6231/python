import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = ('localhost', 65432)
server_socket.bind(server_address)

# Listen for incoming connections (allow only 1 connection at a time)
server_socket.listen(1)
print("Server is listening on port 65432...")

# Wait for a connection
connection, client_address = server_socket.accept()

try:
    print(f"Connection established with {client_address}")

    # Receive the data in small chunks
    while True:
        data = connection.recv(1024)
        if data:
            print("Received:", data.decode())
            # Echo the data back to the client
            connection.sendall(data)
        else:
            break

finally:
    # Clean up the connection
    connection.close()
