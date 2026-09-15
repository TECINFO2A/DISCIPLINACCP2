"""
Questão 8: Crie um dicionário com 5 entradas e suas respectivas chaves e valores.
"""

# Criando um dicionário com 5 entradas (chave: valor)
dicionario = {
    "nome": "Gustavo",
    "idade": 20,
    "curso": "Sistemas de Informação",
    "cidade": "Campina Grande",
    "linguagem_favorita": "Python"
}

# a. Todas as chaves
print("Chaves:", dicionario.keys())

# b. Todos os valores
print("Valores:", dicionario.values())

# c. Todos os itens (pares chave-valor)
print("Itens:", dicionario.items())

# d. O 2º item do dicionário
# Como dicionário não tem índice direto, transformo os itens em lista pra pegar pela posição
segundo_item = list(dicionario.items())[1]
print("2º item do dicionário:", segundo_item)

# e. O dicionário completo
print("Dicionário completo:", dicionario)

# f. Percorrendo o dicionário e mostrando cada chave com seu valor
print("Percorrendo o dicionário:")
for chave, valor in dicionario.items():
    print(f"{chave} tem como valor {valor}")
