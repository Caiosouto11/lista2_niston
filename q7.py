def criar_lista():
    lista = []
    qntd = int(input("quantos elementos você deseja adicionar à lista? "))
    pares = []

    for i in range(qntd):
        numero = int(input(f"Digite o número {i + 1}: "))
        lista.append(numero)
        
        if numero % 2 == 0:
            pares.append(numero)    
    print(f'Os numeros pares são {pares} ')  
            

    return lista,pares

lista_de_numeros, lista_de_pares = criar_lista()
    
