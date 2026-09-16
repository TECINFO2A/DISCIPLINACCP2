lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.append(6)
lista.insert(2, 7)
lista.remove(3)
lista.append(4)

print("Lista:", lista)
print("O número 4 aparece", lista.count(4), "vezes")


print("Primeiros 3:", lista[:3])
print("Da posição 3 até a 7:", lista[2:7])
print("De 3 em 3:", lista[::3])
print("Últimos 3:", lista[-3:])
print("Sem os últimos 4:", lista[:-4])


print("Sexto elemento:", lista[5])


lista[6] = 12
print("Lista com o sétimo elemento alterado:", lista)


lista.reverse()
print("Lista invertida:", lista)


lista.sort()
print("Lista ordenada:", lista)


tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print("Tupla:", tupla)
print("Posição do número 5:", tupla.index(5))


dados = {
    "nome": "Jose",
    "idade": 18,
    "curso": "Ciencia da Computacao",
    "cidade": "Campina Grande",
    "periodo": 2
}

print("Chaves:", dados.keys())
print("Valores:", dados.values())
print("Itens:", dados.items())

itens = list(dados.items())
print("Segundo item:", itens[1])

print("Dicionário:", dados)

for chave, valor in dados.items():
    print(chave, "tem como valor", valor)


arquivo = open("numeros.txt", "w")

for i in range(1, 11):
    arquivo.write(str(i) + "\n")

arquivo.close()


arquivo = open("numeros.txt", "r")
print(arquivo.read())
arquivo.close()


arquivo = open("numeros.txt", "w")

for i in range(11, 21):
    arquivo.write(str(i) + "\n")

arquivo.close()


arquivo = open("numeros.txt", "a")

for i in range(21, 31):
    arquivo.write(str(i) + "\n")

arquivo.close()


arquivo = open("numeros.txt", "r")
print(arquivo.read())
arquivo.close()


arquivo = open("numeros.txt", "r")

for linha in arquivo:
    print(linha.strip())

arquivo.close()