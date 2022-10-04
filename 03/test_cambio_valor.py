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


from cambio_valor import cambio_valor

def test_cambio_valor():
    assert cambio_valor(1,3) == (3, 1)