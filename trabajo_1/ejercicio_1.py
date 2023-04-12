#!/usr/bin/python3

import argparse

class Excersice_1:
    def __init__(self):
        self.__resultado = 0

    def add_argument(self):
        parser = argparse.ArgumentParser(description='Ejercicio 1 de computación')
        parser.add_argument('-o', type=str,default="+",help='Ingresar operador: +,-,*,/(por defecto suma)')
        parser.add_argument('-n', type=int,default=0, help='Ingresar primer número(por defecto vale 0)')
        parser.add_argument('-m', type=int,default=0, help='Ingresar segundo número(por defecto vale 0)')

        args = parser.parse_args()
        return args

    def calculator(self, args_object):
        if (args_object.o == "+"):
            self.__resultado = args_object.n + args_object.m
        elif (args_object.o == "-"):
            self.__resultado = args_object.n - args_object.m
        elif (args_object.o == "*"):
            self.__resultado = args_object.n * args_object.m
        elif (args_object.o == "/"):
            self.__resultado = args_object.n / args_object.m
        else:
            print("Operador invalido")
            return
        return self.__resultado

excersice_1 = Excersice_1()
print(excersice_1.calculator(excersice_1.add_argument()))
