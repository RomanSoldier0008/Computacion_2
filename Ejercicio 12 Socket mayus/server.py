import argparse
import socket

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, required=True, help="Port to listen on")
    args = parser.parse_args()

    host = "0.0.0.0"  # Listen on all interfaces
    port = args.port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen()
        print(f"Waiting for connections on port {port}...")

        while True:
            client_socket, client_addr = server.accept()

            with client_socket:
                print(f"Connection established from {client_addr}")
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    text = data.decode()
                    text_upper = text.upper()
                    client_socket.send(text_upper.encode())

if __name__ == "__main__":
    main()
