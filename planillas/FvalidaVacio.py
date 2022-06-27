def validador_vacio(p_algo):
    while True:
        if p_algo:
            print('Todo nice')
            return p_algo
        else:
            print('Campo vacío, intente ingresar algo')
            p_algo = input('Ingrese algo => ')