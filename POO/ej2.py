"""
Nombre: Rosa
Fecha: 12/01/24
Ejercicio 2

Crea una clase, y pruébala, que modele fracciones. Debe permitir:

Crear fracciones indicando numerador y denominador.
 Ejemplo: f = Fraction(2, 3)
Ojo!!! No se puede tener un denominador cero.
Las fracciones pueden operar entre sí.
Sumar, multiplicar, dividir, restar.
Ojo!!! esto se puede hacer: f + 1, 5 * f
Las fracciones se pueden comparar.
==, <, <=, >, >=, !=
Ojo!!! estas dos fracciones son iguales: 1/2 y 2/4
Ojo!!! esto se puede hacer 1 < 1/2
"""

from typeguard import typechecked
import math

@typechecked
class Fraction:

    def __init__(self, numerator:int, denominator:int):    
        self.__numerator = numerator
        self.denominator = denominator


    @property
    def numerator(self):
        return self.__numerator
    
    @numerator.setter
    def numerator(self, numerator:int):
        gcd = math.gcd(numerator, self.denominator)
        self.__numerator = numerator // gcd
        self.__denominator = self.__denominator // gcd

    @property
    def denominator(self):
        return self.__denominator
    
    @denominator.setter
    def denominator(self, denominator:int):
        if denominator == 0:
            raise ZeroDivisionError(f"Error en el denominador, no puede ser 0 y tiene que ser un entero")
        gcd = math.gcd(denominator, self.numerator)
        self.__numerator = self.__numerator // gcd
        self.__denominator = denominator // gcd    
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__numerator, self.__denominator})"

f = Fraction(2, 4)

print(f"{f}")
