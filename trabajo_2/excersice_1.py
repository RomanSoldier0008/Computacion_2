#!/usr/bin/python3

import argparse
import subprocess
from datetime import datetime

class Excersice_1:
    def __init__(self):
        self.__args = ''

    def add_argument(self):
        parser = argparse.ArgumentParser(description='Ejercicio 1 de computación')
        parser.add_argument('-c','--command', type=str, help='Comando')
        parser.add_argument('-f','--out_file', type=str, help='Archivo donde irá la salida del comando')
        parser.add_argument('-l','--log_file', type=str, help='Archivo donde dirá si el comando fue ejecutado o no')
        self.__args = parser.parse_args()

    def start(self):
        try:
            output = subprocess.check_output(self.__args.command, shell=True, stderr=subprocess.STDOUT)
            f = open(self.__args.out_file, 'w')
            f.write(output.decode('utf-8'))
            f.close()
            f= open(self.__args.log_file, 'w')
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Comando {self.__args.command} ejecutado correctamente")
            f.close()
        except subprocess.CalledProcessError as e:
            f = open(self.__args.log_file, "w")
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {e.output.decode('utf-8')}")
            f.close()

excersice_1 = Excersice_1()
excersice_1.add_argument()
excersice_1.start()
