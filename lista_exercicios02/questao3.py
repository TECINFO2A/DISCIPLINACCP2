"""
Questão 3: Com a lista das questões anteriores, retorne o 6º elemento da lista.
"""

# Recriando a lista com o mesmo resultado da questão 1
lista = list(range(10))
lista.append(6)
lista.insert(2, 7)
lista.remove(3)
lista.append(4)
print("Lista:", lista)

# O 6º elemento está no índice 5 (contando a partir de 0)
print("6º elemento da lista:", lista[5])
