"""
    Un numero primo debe ser mayor 1 y que divisible por si mismo
    Debe tomar la función un numero y debe retornar True si es primo o False en caso contrario

    sumar a todos los numero primos

"""
import math

def es_primo(num):
    #numeros menores que no son primos
    if num < 2:
        return False
    
    for n in range(2, math.floor(math.sqrt(num)+1)):
        if num % n == 0:
            return False
        return True

def suma_de_primos(nums):
    primos = []
    for i in nums:
        if es_primo(i):
            primos.append(i)
    print(primos)
    return sum(primos)