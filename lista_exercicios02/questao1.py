"""
Questão 1: Crie uma lista com números de 0 a 9 (em qualquer ordem) e faça as operações pedidas.
"""

# Crio uma lista com números de 0 a 9
lista = list(range(10))
print("Lista inicial:", lista)

# a. Adicionando o número 6 no final da lista
lista.append(6)
print("Depois de adicionar o 6:", lista)

# b. Inserindo o número 7 na 3ª posição (a contagem começa no índice 0,
# então a 3ª posição é o índice 2)
lista.insert(2, 7)
print("Depois de inserir o 7 na 3ª posição:", lista)

# c. Removendo o elemento de valor 3 (o remove() tira pelo VALOR, não pela posição)
lista.remove(3)
print("Depois de remover o 3:", lista)

# d. Adicionando o número 4 no final
lista.append(4)
print("Depois de adicionar o 4:", lista)

# e. Contando quantas vezes o 4 aparece na lista
qtd_quatro = lista.count(4)
print("O número 4 aparece", qtd_quatro, "vez(es) na lista")
