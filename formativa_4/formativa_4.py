import os
os.system('cls||clear')

from multiprocessing.dummy import Value
import numpy as np

def validaOpcion(p_opcion):
    while True:
        try:
            if p_opcion < 6 and p_opcion > 0:
                return p_opcion
            else:
                print("Deja de hacer weas")
        except ValueError:
            print("XD")

usuario = []
pasajeComprado = []
asiento = np.arange(1, 43).reshape((7, 6))
opc = 0

def validador_vacio(p_algo):
    while True:
        if p_algo:
            print('Todo nice')
            return p_algo
        else:
            print('Campo vacío, intente ingresar algo')
            p_algo = input('Ingrese algo => ')

while opc != 5:
    try:
        opc = validaOpcion(int(input('''Bienvenido a su super preferido! Seleccione aquello que desea hacer
1.- Ver asientos disponibles
2.- Comprar asiento
3.- Anular vuelo
4.- Modificar datos de pasajero
5.- Salir
==> ''')))
    except ValueError:
        print('Tipo de valor ingresado invalido, intentelo nuevamente')
    if opc == 1:
        print("\nSe encuentran disponibles todos los asientos que no tengan x:\n")
        for i in range(7):
            for c in range(6):
                if c == 0:
                    print("|", asiento[i][c], end = " ")
                elif c == 3:
                    print("\t", asiento[i][c], end = " ")
                else:
                    print("", asiento[i][c], end = " ")
            print("|")
            print("\n")
    elif opc == 2:
        nombrePasajero = input('Ingrese su nombre => ')
        validador_vacio(nombrePasajero)
        while True:
            try:
                rutPasajero = int(input('Ingrese su run sin codigo verificador => '))
                break
            except ValueError:
                print("todo mal")
        dv = input('Ingrese su digito verificador => ')
        validador_vacio(dv)
        while True:
            try:
                telefonoPasajero = int(input('Ingrese su número telefónico => '))
                break
            except:
                print("por la xuxa hermano")
        bancoPasajero = input("Ingrese su banco => ")
        validador_vacio(bancoPasajero)
        try:
            usuarioCompra = int(input("Ingrese el boleto que desea comprar"))
            pasajeComprado.append(usuarioCompra)
        except ValueError:
            print("Ingrese solo valores numericos")
    elif opc == 3:
        print('aaa')
    elif opc == 4:
        print('aaaa')
    elif opc == 5:
        print('Muchas gracias por preferirnos!')
    else:
        print('Opción no registrada, intente con alguna opción que se encuentre en el menú')


"""print("hola putos")
lista1=[]
lista2=[]
x=0
for i in range(6):
    lista1=[]
    for i in range(7):
        """