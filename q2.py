def criar_lista():
    lista = []
    qntd =  int(input("quantos elementos você deseja adicionar à lista? "))

    for i in range(qntd):
        nomes = input(f"Digite o nome {i + 1}: ")
        lista.append(nomes)

    return lista
    
minha_lista = criar_lista()
qtd_nomes = len(minha_lista)
print(f"A quantidade de números da sua lista é {qtd_nomes}")
