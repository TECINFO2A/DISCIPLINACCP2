"""
Questão 6: Ordene a lista.
"""

# Recriando a lista com o mesmo resultado da questão 1
lista = list(range(10))
lista.append(6)
lista.insert(2, 7)
lista.remove(3)
lista.append(4)
print("Lista antes de ordenar:", lista)

# Colocando a lista em ordem crescente
lista.sort()
print("Lista ordenada:", lista)
