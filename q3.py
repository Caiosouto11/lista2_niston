def criar_lista():
    lista = []
    qtd = int(input("quantos elementos você deseja adicionar à lista? "))
    for i in range(qtd):
     elementos = int(input(f"Digite o número {i + 1}: "))
     lista.append(elementos)
    return lista

minha_lista = criar_lista()
tmh_lista = len(minha_lista)
soma = sum(minha_lista)
print(soma)