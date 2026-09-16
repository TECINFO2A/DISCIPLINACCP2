# QUESTÃO 1
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# a
lista.append(6)

# b
lista.insert(2, 7)

# c
lista.remove(3)

# d
lista.append(4)

# e
ocorrencias_4 = lista.count(4)
print("1e. Ocorrências do número 4:", ocorrencias_4)
print()

# QUESTÃO 2
# a
print("2a. Primeiros 3 elementos:", lista[:3])

# b
print("2b. Da 3ª até a 7ª posição:", lista[2:7])

# c
print("2c. De 3 em 3 elementos:", lista[::3])

# d
print("2d. Últimos 3 elementos:", lista[-3:])

# e
print("2e. Todos menos os 4 últimos:", lista[:-4])
print()

# QUESTÃO 3
print("3. 6º elemento:", lista[5])

# QUESTÃO 4
lista[6] = 12
print("4. Lista com o 7º elemento alterado:", lista)

# QUESTÃO 5
lista.reverse()
print("5. Lista invertida:", lista)

# QUESTÃO 6
lista.sort()
print("6. Lista ordenada:", lista)
print()

# QUESTÃO 7
tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# a
try:
    tupla[2] = 10
except TypeError as e:
    print("7a. Erro ao tentar alterar a tupla:", e)

# b
print("7b. Índice do valor 5 na tupla:", tupla.index(5))
print()

# QUESTÃO 8
dicionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1969,
    "cor": "Vermelho",
    "motor": "V8"
}

# a
print("8a. Chaves:", list(dicionario.keys()))

# b
print("8b. Valores:", list(dicionario.values()))

# c
print("8c. Itens:", list(dicionario.items()))

# d
print("8d. 2º item:", list(dicionario.items())[1])

# e
print("8e. Dicionário completo:", dicionario)

# f
print("8f. Percorrendo o dicionário:")
for chave, valor in dicionario.items():
    print(f"{chave} tem como valor {valor}")
print()

# QUESTÃO 9
nome_arquivo = "exercicio9.txt"

# a
with open(nome_arquivo, "w") as f:
    for i in range(1, 11):
        f.write(f"{i}\n")

# b
with open(nome_arquivo, "r") as f:
    print("9b. Conteúdo inicial do arquivo (1 a 10):")
    print(f.read())

# c
with open(nome_arquivo, "w") as f:
    for i in range(11, 21):
        f.write(f"{i}\n")

# d
with open(nome_arquivo, "a") as f:
    for i in range(21, 31):
        f.write(f"{i}\n")

# e
with open(nome_arquivo, "r") as f:
    print("9e. Conteúdo atualizado (11 a 30):")
    print(f.read())

# f
print("9f. Conteúdo linha por linha:")
with open(nome_arquivo, "r") as f:
    for linha in f:
        print(linha.strip())