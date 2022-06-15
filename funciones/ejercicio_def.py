def validador_vacio(p_algo):
    while True:
        if p_algo:
            print('Todo nice')
            break
        else:
            print('Campo vacío, intente ingresar algo')
            p_algo = input('Ingrese algo')

while True:
    try:
        opc = int(input('''Bienvenido a su super preferido! Seleccione aquello que desea hacer
1.- Calcular IVA
2.- Descuento
3.- Calcular IMC
==> '''))
    except ValueError:
        print('Tipo de valor ingresado invalido, intentelo nuevamente')
    if opc == 1:
        print('uwu')
    elif opc == 2:
        print('a')
    elif opc == 3:
        print('aaa')
    else:
        print('Opción no registrada, intente con alguna opción que se encuentre en el menú')