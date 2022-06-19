"""Crear un arreglo unidimensional con nombre arreglo_1 y de tamaño 10, con elementos aleatorios de números enteros del 0 al 1000, luego:
Mostrar por pantalla todos los elementos del arreglo.
Contar los elementos pares.
Sumar los elementos impares.
Emitir mensaje de cada elemento que sea primo."""

import numpy as np
arregloA = np.arange(21)

yourMom = arregloA.max()
yourMom2 = (np.where(arregloA == yourMom))
print (yourMom2[0])