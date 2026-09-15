print("=====Exercicio1=====")

lista = list(range(10))
lista.append(6)
print(lista)

lista.insert(2,7)
print(lista)

lista.remove(3)
print(lista)

lista.append(4)
print(lista)

contagem = lista.count(4)
print(f"O número de ocorrências do número 4 é {contagem}")

#Exercicio 2
print("=====Exercicio2=====")

print(lista[:3])
print(lista[2:7])
print(lista[::3])
print(lista[-3:])
print(lista[:-4])

#Exercicio 3
print("=====Exercicio3=====")
print(lista[5])

#Exercício 4
print("=====Exercicio4=====")
lista[6] = 12
print(lista)

#Exercício 5
print("=====Exercicio5=====")
lista.reverse()
print(lista)

#Exercício 6
print("=====Exercicio6=====")
lista.sort()
print(lista)