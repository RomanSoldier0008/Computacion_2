import argparse
import socket

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--server_address", required=True, help="Server IP address")
    parser.add_argument("-p", "--port", type=int, required=True, help="Server port")
    args = parser.parse_args()

    host = args.server_address
    port = args.port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        text = input("Enter a text string: ")
        client_socket.send(text.encode())
        data = client_socket.recv(1024)
        uppercase_text = data.decode()
        print("Uppercase text received from the server:", uppercase_text)

if __name__ == "__main__":
    main()