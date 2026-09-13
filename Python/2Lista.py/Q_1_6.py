# Questão 1 - Lista:
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)

# a. Adicionar o número 6
lista.insert(5, 6)
print(lista)

# b. Inserir o número 7 na 3ª posição (índice 2)
lista.insert(2, 7)
print(lista)

# c. Remover o elemento 3
lista.remove(3)
print(lista)

# d. Adicionar o número 4
lista.append(4)
print(lista)

# e. Verificar ocorrências do número 4
ocorrencias = lista.count(4)
print("O numero 4 aparece", ocorrencias, "vezes")


# Questão 2 -(fatiamento) da lista

# a. Primeiros 3 elementos
print(lista[0:3])

# b. Elementos da 3ª até a 7ª posição
print(lista[2:7])

# c. Elementos de 3 em 3
print(lista[::3])

# d. Últimos 3 elementos
print(lista[-3:])

# e. Todos menos os 4 últimos
print(lista[:-4])


# Questão 3 - Retornar o 6º elemento

print(lista[5])

# Questão 4 - Alterar o 7º elemento para 12

lista[6] = 12
print(lista)

# Questão 5 - Inverter a lista

lista.reverse()
print(lista)


# Questão 6 - Ordenar a lista

lista.sort()
print(lista)