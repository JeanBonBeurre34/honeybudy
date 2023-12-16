import socket
import threading
import logging

# Basic configuration for logging
logging.basicConfig(filename="honeypot_logs.txt", level=logging.INFO, format='%(asctime)s %(message)s')

# Function to handle each client connection
def handle_client(client_socket):
    try:
        while True:
            # Send a basic Unix command prompt
            client_socket.send(b"fakeunix$ ")
            # Receive the command from the "attacker"
            cmd = client_socket.recv(1024).decode('utf-8').strip()
            # Log the command
            logging.info(f"Received command: {cmd}")
            # Send a fake response
            client_socket.send(b"Command not found\n")
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        client_socket.close()

def start_honeypot(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    logging.info(f"Honeypot running on {ip}:{port}")

    try:
        while True:
            client_socket, addr = server.accept()
            logging.info(f"Connection from {addr}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
    except KeyboardInterrupt:
        server.close()
        logging.info("Honeypot stopped")

if __name__ == "__main__":
    IP = "0.0.0.0"  # Listen on all available interfaces
    PORT = 2222     # You can choose any non-standard port
    start_honeypot(IP, PORT)
