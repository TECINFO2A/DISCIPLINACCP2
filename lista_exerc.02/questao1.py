"""
Questão 1: Crie uma lista com números de 0 a 9 (em qualquer ordem) e faça as operações pedidas.
"""

# Crio uma lista com números de 0 a 9
lista = list(range(10))
print("Lista inicial:", lista)

lista.append(6)
print("Depois de adicionar o 6:", lista)


lista.insert(2, 7)
print("Depois de inserir o 7 na 3ª posição:", lista)

print("Depois de remover o 3:", lista)

lista.append(4)
print("Depois de adicionar o 4:", lista)

qtd_quatro = lista.count(4)
print("O número 4 aparece", qtd_quatro, "vez(es) na lista")
