"""
Questão 5: Inverta a ordem dos elementos na lista.
"""

# Recriando a lista com o mesmo resultado da questão 1
lista = list(range(10))
lista.append(6)
lista.insert(2, 7)
lista.remove(3)
lista.append(4)
print("Lista antes de inverter:", lista)

# Invertendo a ordem da lista
lista.reverse()
print("Lista invertida:", lista)
