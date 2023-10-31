import socket
import sys
import getopt

def main(argv):
    # Opciones por defecto
    port = None
    protocol = None
    file_name = None

    try:
        opts, args = getopt.getopt(argv, "p:t:f:")
    except getopt.GetoptError:
        print("Uso: server.py -p <port> -t <tcp/udp> -f <file>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-p":
            port = int(arg)
        elif opt == "-t":
            protocol = arg
        elif opt == "-f":
            file_name = arg

    if port is None or protocol is None or file_name is None:
        print("Faltan argumentos.")
        print("Uso: server.py -p <port> -t <tcp/udp> -f <file>")
        sys.exit(2)

    try:
        if protocol == "tcp":
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif protocol == "udp":
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            print("Protocolo no válido. Debe ser tcp o udp.")
            sys.exit(2)

        server_socket.bind(("0.0.0.0", port))
        server_socket.listen(1)

        print(f"Server listening on port {port} ({protocol})...")

        while True:
            conn, addr = server_socket.accept()
            with open(file_name, "ab") as file:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    file.write(data)
            conn.close()

    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == "__main__":
    main(sys.argv[1:])