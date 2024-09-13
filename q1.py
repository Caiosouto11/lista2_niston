def criar_lista():
    lista = []
    qntd = int(input("quantos elementos você deseja adicionar à lista? "))

    for i in range(qntd):
        numero = int(input(f"Digite o número {i + 1}: "))
        lista.append(numero)

    return lista
    
minha_lista = criar_lista()
maior_numero = max(minha_lista)
print(f"O maior número da sua lista é {maior_numero}")





