import socket
import threading
import logging
import io
import sys

# Basic configuration for logging
logging.basicConfig(filename="honeypot_logs.txt", level=logging.INFO, format='%(asctime)s %(message)s')

# Simple Unix System with help class
class SimpleUnixSystemWithHelp:
    # [Class implementation remains the same as provided]

def handle_client(client_socket, unix_system):
    try:
        while True:
            # Send a basic Unix command prompt
            client_socket.send(f"{unix_system.current_directory}$ ".encode())
            # Receive the command from the "attacker"
            cmd = client_socket.recv(1024).decode('utf-8').strip()
            if not cmd:
                continue

            # Log the command
            logging.info(f"Received command: {cmd}")

            # Redirect stdout to capture the output of the command
            old_stdout = sys.stdout
            sys.stdout = io.StringIO()

            # Process the command using the Unix system
            unix_system.run_command(cmd.split())

            # Get the output and restore stdout
            output = sys.stdout.getvalue()
            sys.stdout = old_stdout

            # Send the captured output to the client
            client_socket.sendall(output.encode())
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        client_socket.close()

def start_honeypot(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    logging.info(f"Honeypot running on {ip}:{port}")

    # Create an instance of the Unix system
    unix_system = SimpleUnixSystemWithHelp()

    try:
        while True:
            client_socket, addr = server.accept()
            logging.info(f"Connection from {addr}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket, unix_system))
            client_handler.start()
    except KeyboardInterrupt:
        server.close()
        logging.info("Honeypot stopped")

if __name__ == "__main__":
    IP = "0.0.0.0"  # Listen on all available interfaces
    PORT = 2222     # You can choose any non-standard port
    start_honeypot(IP, PORT)
