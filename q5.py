def criar_lista():
    lista = []
    qntd = int(input("Quantos elementos você deseja adicionar à lista? "))
    nomes_com_A = []

    for i in range(qntd):
        nome = input(f"Digite o nome {i + 1}: ")
        lista.append(nome)
    
  
    for nome in lista:
        if nome.startswith('A') or nome.startswith('a'):
                nomes_com_A.append(nome)
    
    return nomes_com_A


nomes_com_A = criar_lista()
print(f'Os nomes que começam com "A" são: {nomes_com_A}')
