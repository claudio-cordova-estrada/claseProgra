import os
os.system("cls")

import misfunciones as fn

while True:
    os.system("cls")
    print("Programa principal")
    print("       MENU")
    print("1. Guardar patente")
    print("2. Buscar vehiculo")
    print("3. Imprimir lista")
    print("4. Salir")
    opcion = fn.menu()
    if opcion == 0:
        break
    elif opcion == 1:
        fn.ingreso()
    elif opcion == 2:
        fn.buscar()
    elif opcion == 3:
        fn.imprimir()
    elif opcion == 4:
        break
    input("Enter para continuar")

input("Enter para terminar")




