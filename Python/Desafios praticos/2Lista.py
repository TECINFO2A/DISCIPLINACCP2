
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
 
# Questão 7 - Tupla (imutável)

tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tupla)
 
# a. Tupla é imutavel 


# b. Verificar o índice (posição) do valor 5
print(tupla.index(5))

# Questão 8 - Crie um dicionário com 5 entradas
dicionario={
    "nome": "Pedro",
    "idade": "18",
    "curso": "C.C.",
    "time": "palmeiras",
    "apelido": "Raio"
}
# a. Imprima todas as chaves do dicionário 
print(dicionario)

# b. Imprima todos os valores do dicionário 
print(dicionario.values())

# c. Imprima todos os itens do dicionário 
print(dicionario.items())

# d. Imprima o 2º item do dicionário
itens = list(dicionario.items())
print(itens[1])

# e. Imprima o dicionário completo
for chave, valor in dicionario.items():
    print(chave, " :", valor)

# f.  Percorra o dicionário
for chave, valor in dicionario.items():
    print(f"({chave}) tem como valor ({valor})")


