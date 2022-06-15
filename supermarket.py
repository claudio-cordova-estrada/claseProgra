producto = [[1, 'caramelo', '24-04-2022'], [2, 'frito', '28-05-2022'], [3, 'Dulce', '29-05-2022']]
id_encontrado = False
nom_encontrado = False
fecha_encontrada = False

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
1: Buscar por id
2: Buscar por tipo de producto (string)
3: Buscar de acuerdo a fecha de vencimiento
4: Insertar nuevo elemento
==> '''))
    except ValueError:
        print('Tipo de valor ingresado invalido, intentelo nuevamente')
    if opc == 1:
        while not id_encontrado:
            try:
                id_buscado = int(input('Ingrese el id del valor que se encuentra buscando\n==>\t'))
            except ValueError:
                print('Tipo de valor ingresado no valido, intentelo nuevamente')
            for producto_especifico in producto:
                if producto_especifico[0] == id_buscado:
                    print(f'Estos son los datos de su producto\n{producto_especifico}')
                    id_encontrado = True
                    break
                else:
                    pass
            if not id_encontrado:
                print("Producto no encontrado.")
        id_encontrado = False
    elif opc == 2:
        while not nom_encontrado:
            nom_buscado = input('Ingrese el nombre del producto que se encuentra buscando')
            validador_vacio(nom_buscado)
            while not nom_encontrado:
                for producto_especifico in producto:
                    if producto_especifico[1] == nom_encontrado:
                        print(f'Estos son lso datos de su producto\n{producto_especifico}')
                        nom_encontrado = True
                        break
                    else:
                        pass
                if not nom_encontrado:
                    print('Producto no encontrado')
    elif opc == 3:
        print('aaa')
    elif opc == 4:
        print('aaaa')
    else:
        print('Opción no registrada, intente con alguna opción que se encuentre en el menú')