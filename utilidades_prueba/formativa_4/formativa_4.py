import os
os.system('cls||clear')

from multiprocessing.dummy import Value
import numpy as np

usuario = []
usuarioCompra = 1
pasajeComprado = []
asiento = np.arange(1, 43, dtype = str).reshape((7, 6))
opc = 0

def validaOpcion(p_opcion):
    while True:
        try:
            if p_opcion < 6 and p_opcion > 0:
                return p_opcion
            else:
                print("Deja de hacer weas")
        except ValueError:
            print("XD")

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

    # Ver asientos disponibles
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

    # Comprar asiento
    elif opc == 2:
        # Datos usuario
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
            except ValueError:
                print("Ingrese su numero telefonico")

        bancoPasajero = input("Ingrese su banco => ")
        validador_vacio(bancoPasajero)

        # Sistema de compra de boletos
        while usuarioCompra:
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
                try:
                    usuarioCompra = int(input("Ingrese cuantos boletos desee comprar (oprima 0 para salir) => "))
                except ValueError:
                    print("Tipo de valor ingresado incorrecto")
                if usuarioCompra != 0 and usuarioCompra > 0 and usuarioCompra <= 42:
                    for i in pasajeComprado:
                        if i == usuarioCompra:
                            print("Asiento ya ocupado, intentelo nuevamente")
                else:
                    print("Valor ingresado se encuentra fuera del rango de pasajes, intentelo nuevamente")

        usuarioCompra = 1
        usuario.append(rutPasajero, usuarioCompra, dv, nombrePasajero, telefonoPasajero, bancoPasajero)

    # Anular vuelo
    elif opc == 3:
        usuarioRut = int(input("Ingrese su run sin codigo verificador => "))

        for usuarioDetalle in usuario:
            if usuarioDetalle[0] != usuarioRut:
                print("Rut ingresado no se encuentra en el sistema, intentelo nuevamente")
            else:
                print("Rut validado")
                usuarioCancela = int(input("Ingrese el pasaje que desea cancelar => "))
                if usuarioDetalle[1] != usuarioCancela:
                    print("No posee el numero de pasaporte ingresado")
                else:
                    print("todo nice")

    # Modificar datos pasajero
    elif opc == 4:
        print('aaaa')
    
    # Salir
    elif opc == 5:
        print('Muchas gracias por preferirnos!')

    # Opción invalida
    else:
        print('Opción no registrada, intente con alguna opción que se encuentre en el menú')

os.system('cls||clear')

"""print("hola p")
lista1=[]
lista2=[]
x=0
for i in range(6):
    lista1=[]
    for i in range(7):
        """