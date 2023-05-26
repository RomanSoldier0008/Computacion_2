import os
import sys

def invertir_linea(linea):
    return linea[::-1]

def main():
    if len(sys.argv) != 3 or sys.argv[1] != '-f':
        print("Uso: {} -f ARCHIVO".format(sys.argv[0]))
        sys.exit(1)

    archivo = sys.argv[2]
    with open(archivo, 'r') as f:
        lineas = f.readlines()

    pipes = []
    for linea in lineas:
        r, w = os.pipe()
        pipes.append((r, w))
        pid = os.fork()
        if pid == 0:
            os.close(r)
            w = os.fdopen(w, 'w')
            w.write(invertir_linea(linea))
            w.close()
            sys.exit(0)
        else:
            os.close(w)

    for r, _ in pipes:
        r = os.fdopen(r)
        print(r.read().strip())
        r.close()

if name == "__main__":
    main()
