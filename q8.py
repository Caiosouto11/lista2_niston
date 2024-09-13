def criar_lista():
    lista = []
    qntd = int(input("quantos elementos você deseja adicionar à lista? "))
    impares = []

    for i in range(qntd):
        numero = int(input(f"Digite o número {i + 1}: "))
        lista.append(numero)
        
        if numero % 2 != 0:
            impares.append(numero)    
    print(f'Os numeros impares são {impares} ')  
            

    return lista,impares

lista_de_numeros, lista_de_impares = criar_lista()