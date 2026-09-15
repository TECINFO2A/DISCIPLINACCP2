"""
Questão 7: Crie uma tupla com números de 0 a 9 (em qualquer ordem) e tente:
a. Alterar o valor do 3º elemento da tupla para o valor 10
b. Verificar o índice (posição) do valor 5 na tupla
"""

# Criando uma tupla com números de 0 a 9
tupla = tuple(range(10))
print("Tupla criada:", tupla)

# a. Tentando alterar o 3º elemento (índice 2) - isso não é permitido em tuplas,
# porque elas são imutáveis. Uso um try/except pra mostrar o erro sem travar o programa.
try:
    tupla[2] = 10
except TypeError as erro:
    print("Não foi possível alterar a tupla. Erro:", erro)

# b. Descobrindo em que posição (índice) está o valor 5
posicao_do_5 = tupla.index(5)
print("O valor 5 está na posição:", posicao_do_5)
