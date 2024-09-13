def criar_lista_e_imprimir_mais_longa():
    lista = []
    qntd = int(input("Quantos elementos você deseja adicionar à lista? "))

    for i in range(qntd):
        nome = input(f"Digite o nome {i + 1}: ")
        lista.append(nome)

        palavra_mais_longa = max(lista, key=len)
        print(f'A palavra mais longa é: {palavra_mais_longa}')

criar_lista_e_imprimir_mais_longa()
