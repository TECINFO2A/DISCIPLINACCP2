
numeros = [0, 8, 2, 5, 1, 9, 3, 4]

# a
numeros.append(6)

# b
numeros.insert(2, 7)

# c
numeros.remove(3)

# d
numeros.append(4)

# e
ocorrencias_quatro = numeros.count(4)

print("Lista final:", numeros)
print("Ocorrências do número 4:", ocorrencias_quatro)