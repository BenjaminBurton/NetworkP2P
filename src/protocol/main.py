import socket
import threading

# List of connected peers
peers = []

# Function to handle incoming connections


def handle_connection(connection, address):
    while True:
        data = connection.recv(1024)
        if data:
            print(f"Received message from {address[0]}: {data.decode()}")
            # Broadcast the message to all connected peers
            for peer in peers:
                if peer != connection:
                    peer.send(data)
        else:
            print(f"{address[0]} disconnected.")
            peers.remove(connection)
            connection.close()
            break

# Function to start the server and accept incoming connections


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5000))
    server.listen(5)
    print("Server started. Waiting for connections...")

    while True:
        connection, address = server.accept()
        peers.append(connection)
        print(f"Connected to {address[0]}")
        threading.Thread(target=handle_connection,
                         args=(connection, address)).start()

# Function to connect to a remote peer


def connect_to_peer(peer_ip):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((peer_ip, 5000))
        peers.append(client)
        print(f"Connected to {peer_ip}")
        threading.Thread(target=handle_connection, args=(
            client, (peer_ip, 5000))).start()
    except ConnectionRefusedError:
        print(f"Connection to {peer_ip} refused.")

# Main function


def main():
    threading.Thread(target=start_server).start()

    while True:
        choice = input(
            "1. Connect to a peer\n2. Send message\n3. Quit\nEnter your choice: ")
        if choice == '1':
            peer_ip = input("Enter peer IP address: ")
            threading.Thread(target=connect_to_peer, args=(peer_ip,)).start()
        elif choice == '2':
            message = input("Enter message to send: ")
            for peer in peers:
                peer.send(message.encode())
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

    print("Exiting...")
    for peer in peers:
        peer.close()


if __name__ == '__main__':
    main()
