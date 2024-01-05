"""
Nombre: Rosa
Fecha: 05/01/24
1. Define tres listas de 20 números enteros cada uno, con nombres number, square y cube. 
Carga las lista number con valores aleatorios entre 0 y 100. 
En la lista square se deben almacenar los cuadrados de los valores que hay en number. 
En la lista cube se deben almacenar los cubos de los valores que hay en number. 
A continuación, muestra el contenido de las tres listas dispuesto en tres columnas.

"""

import random

number = [random.randint(0, 100) for _ in range(20)]
"""
Lo de arriba sería lo mismo que:
number = []
for _ in range(20):
    number.append(random.randint(0, 100))
"""

square = [i**2 for i in number]
"""
Lo de arriba sería lo mismo que:
square = []
for i in number:
    square.append(i ** 2)
"""
cube = [i**3 for i in number]

print(f"{"Number":<10} {"Square":<10} {"Cube":<10}")
print("-"*30)
for i in range(len(number)):
    print(f"{number[i]:<10} {square[i]:<10} {cube[i]:<10}")
    print("\n")