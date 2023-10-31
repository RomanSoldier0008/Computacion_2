import socket
import sys
import getopt

def main(argv):
    # Opciones por defecto
    server_ip = None
    port = None
    protocol = None

    try:
        opts, args = getopt.getopt(argv, "a:p:t:")
    except getopt.GetoptError:
        print("Uso: client.py -a <server_ip> -p <port> -t <tcp/udp>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-a":
            server_ip = arg
        elif opt == "-p":
            port = int(arg)
        elif opt == "-t":
            protocol = arg

    if server_ip is None or port is None or protocol is None:
        print("Faltan argumentos.")
        print("Uso: client.py -a <server_ip> -p <port> -t <tcp/udp>")
        sys.exit(2)

    try:
        if protocol == "tcp":
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif protocol == "udp":
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            print("Protocolo no válido. Debe ser tcp o udp.")
            sys.exit(2)

        client_socket.connect((server_ip, port))

        print("Cliente conectado al servidor.")
        print("Ingrese texto (Ctrl+d para terminar):")

        while True:
            try:
                line = input()
                client_socket.send(line.encode())
            except EOFError:
                break

    except KeyboardInterrupt:
        print("\nCliente detenido.")

if __name__ == "__main__":
    main(sys.argv[1:])