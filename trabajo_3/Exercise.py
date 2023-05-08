import os
import sys
import argparse

class ExcersiceTp3:
    def __init__(self):
        self.__args = ""

    def sum_even_numbers(self, n):
        return sum(i for i in range(0, n+1, 2))

    def child_process(self):
        pid = os.getpid()
        ppid = os.getppid()
        if self.__args.v:
            print(f"Starting process {pid}")
            result = sum_even_numbers(pid)
            print(f"{pid} - {ppid}: {result}")
            print(f"Ending process {pid}")

    def add_argument(self):
        parser = argparse.ArgumentParser(description="Suma números pares hasta PID<proceso hijo>")
        parser.add_argument("-n", type=int, help="Números de procesos hijos que se van a crear")
        parser.add_argument("-v", action="store_true", help="Habilitar el modo verbo")
        self.__args = parser.parse_args()

        for _ in range(self.__args.n):
            pid = os.fork()
            if pid == 0:
                child_process(self.__args.v)
                sys.exit(0)

        for _ in range(self.__args.n):
            os.wait()

excercise = ExcersiceTp3()
print(excercise.add_argument())
