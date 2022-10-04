"""
    Un numero primo debe ser mayor 1 y que divisible por si mismo
    Debe tomar la función un numero y debe retornar True si es primo o False en caso contrario

"""
from primos import es_primo, suma_de_primos
# ./test_primos

def test_primos_numero_bajo():
    assert es_primo(1) == False
    assert es_primo(0) == False
    assert es_primo(-1) == False

def test_numero_primo():
    assert es_primo(29) == True

#def test_numero_compuesto():
#    assert es_primo(15) == False




"""
    [] = 0
    [1,2,15,11] = 13
"""

def test_suma_primos_vacio():
    assert suma_de_primos([]) == 0


def test_suma_de_numeros_mixtos_primos():
    assert suma_de_primos([1,2,15,11]) == 26
