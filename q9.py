
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

numeros_comuns = list(set(lista1) & set(lista2))

print("Números presentes em ambas as listas:", numeros_comuns)
