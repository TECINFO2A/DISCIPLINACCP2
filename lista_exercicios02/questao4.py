"""
Questão 4: Altere o valor do 7º elemento da lista para o valor 12.
"""

# Recriando a lista com o mesmo resultado da questão 1
lista = list(range(10))
lista.append(6)
lista.insert(2, 7)
lista.remove(3)
lista.append(4)
print("Lista antes:", lista)

# O 7º elemento está no índice 6
lista[6] = 12
print("Lista depois de alterar o 7º elemento para 12:", lista)
