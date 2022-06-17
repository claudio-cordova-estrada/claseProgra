from multiprocessing.dummy import Value
import numpy as np


def validaOpcion(p_opcion):
    while True:
        try:
            if p_opcion > 5 and p_opcion < 0:
                return p_opcion
            else:
                print("Deja de hacer weas")
        except ValueError:
            print("XD")
    
usuario = []
asiento = np.arange(1, 31).reshape((5, 6))
asientoVip = np.arange(31, 43).reshape((2, 6))
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
        print("asiento")
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