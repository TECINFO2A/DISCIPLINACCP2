
# QUESTÃO 1

lista = [5, 2, 8, 0, 3, 9, 1, 7, 4, 6]
print("Lista original:", lista)

# a.
lista.append(6)
print("a. Após adicionar o 6:", lista)

# b.
lista.insert(2, 7)
print("b. Após inserir o 7 na 3ª posição:", lista)

# c.
lista.remove(3)
print("c. Após remover o elemento 3:", lista)

# d.
lista.append(4)
print("d. Após adicionar o 4:", lista)

# e.
ocorrencias = lista.count(4)
print("e. Número de ocorrências do 4:", ocorrencias)
print()

# QUESTÃO 2

print("Lista atual:", lista)

# a.
print("a. Primeiros 3 elementos:", lista[:3])

# b.
print("b. Da 3ª até a 7ª posição:", lista[2:7])

# c.
print("c. De 3 em 3 elementos:", lista[::3])

# d.
print("d. Últimos 3 elementos:", lista[-3:])

# e.
print("e. Todos menos os 4 últimos:", lista[:-4])
print()

# QUESTÃO 3, 4, 5 e 6

print("Lista atual:", lista)

# 3.
print("3. 6º elemento:", lista[5])

# 4.
lista[6] = 12
print("4. Lista após alterar o 7º elemento para 12:", lista)

# 5.
lista.reverse()
print("5. Lista invertida:", lista)

# 6.
lista.sort()
print("6. Lista ordenada:", lista)
print()

# QUESTÃO 7

tupla = (4, 1, 8, 5, 0, 9, 2, 7, 3, 6)
print("Tupla original:", tupla)

# a.
try:
    tupla[2] = 10
except TypeError as erro:
    print("a. Erro ao tentar alterar a tupla:", erro)
    print(" (Tuplas são imutáveis, não é possível alterar seus elementos)")

# b.
indice_5 = tupla.index(5)
print("b. Índice do valor 5 na tupla:", indice_5)
print()

# QUESTÃO 8

dicionario = {
    "nome": "João",
    "idade": 28,
    "cidade": "São Paulo",
    "profissao": "Engenheiro",
    "linguagem_favorita": "Python"
}

# a.
print("a. Chaves:", list(dicionario.keys()))

# b.
print("b. Valores:", list(dicionario.values()))

# c.
print("c. Itens:", list(dicionario.items()))

# d.
segundo_item = list(dicionario.items())[1]
print("d. 2º item:", segundo_item)

# e.
print("e. Dicionário completo:", dicionario)

# f.
print("f. Percorrendo o dicionário:")
for chave, valor in dicionario.items():
    print(f" {chave} tem como valor {valor}")
print()

# QUESTÃO 9

caminho_arquivo = "numeros.txt"

# a.
with open(caminho_arquivo, "w") as arquivo:
    for numero in range(1, 11):
        arquivo.write(f"{numero}\n")
print("a. Arquivo criado com os números de 1 a 10.")

# b.
with open(caminho_arquivo, "r") as arquivo:
    conteudo = arquivo.read()
print("b. Conteúdo do arquivo (1 a 10):")
print(conteudo)

# c.
with open(caminho_arquivo, "w") as arquivo:
    for numero in range(11, 21):
        arquivo.write(f"{numero}\n")
print("c. Arquivo substituído pelos números de 11 a 20.")

# d.
with open(caminho_arquivo, "a") as arquivo:
    for numero in range(21, 31):
        arquivo.write(f"{numero}\n")
print("d. Números de 21 a 30 adicionados ao final do arquivo.")

# e.
with open(caminho_arquivo, "r") as arquivo:
    conteudo = arquivo.read()
print("e. Conteúdo do arquivo (11 a 30):")
print(conteudo)

# f.
print("f. Conteúdo do arquivo, linha por linha:")
with open(caminho_arquivo, "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())