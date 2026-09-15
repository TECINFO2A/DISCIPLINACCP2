"""
Questão 2: Ainda com a lista da questão 1, faça as operações de fatiamento pedidas.
"""

# Recriando a lista já com as alterações da questão 1, pra esse arquivo funcionar sozinho
lista = list(range(10))
lista.append(6)
lista.insert(2, 7)
lista.remove(3)
lista.append(4)
print("Lista de partida (resultado da questão 1):", lista)

# a. Pegando os 3 primeiros elementos
print("3 primeiros elementos:", lista[:3])

# b. Elementos da 3ª até a 7ª posição (índices 2 até 6)
print("Da 3ª à 7ª posição:", lista[2:7])

# c. Pegando de 3 em 3 elementos
print("De 3 em 3 elementos:", lista[::3])

# d. Os 3 últimos elementos
print("3 últimos elementos:", lista[-3:])

# e. Todos os elementos menos os 4 últimos
print("Todos menos os 4 últimos:", lista[:-4])
