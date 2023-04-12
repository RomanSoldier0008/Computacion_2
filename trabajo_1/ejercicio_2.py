#!/usr/bin/python3

import argparse

class Excersice_2:
    def __init__(self):
        self.__args = ''
        self.__content = ''

    def add_argument(self):
        parser = argparse.ArgumentParser(description='Ejercicio 2 de computación')
        parser.add_argument('-i', type=str, default='None', help='Nombre del archivo')
        parser.add_argument('-o', type=str, default='None', help='Nuevo/sobreescribir archivo de destino')
       
        self.__args = parser.parse_args()

    def verificate_if_file_exist(self):
        try:
            file = open(self.__args.i, 'r')
            self.__content = file.read()
            print(self.__content)
            file.close()
        except FileNotFoundError:
            print(f"El archivo remitente {self.__args.i} no existe")

    def copy_content_to_new_file(self):
            if self.__content != "":
                new_file = open(self.__args.o, 'w')
                new_file.write(self.__content)
                new_file.close()
                return 'Archivo escrito o sobreescrito con éxito'
            return 'Error, el archivo remitente esta vacío'

excersice_2 = Excersice_2()
excersice_2.add_argument()
excersice_2.verificate_if_file_exist()
print(excersice_2.copy_content_to_new_file())
