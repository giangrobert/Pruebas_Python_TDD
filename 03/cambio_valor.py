"""
TDD
Realizar un programa que lea dos numero, y que los intercambie

Entrada 
a = 2
b = 3

Salida
a = 3
b = 2
"""



def cambio_valor(a,b):
    temp = a
    a = b
    b = temp
    del temp
    return a,b