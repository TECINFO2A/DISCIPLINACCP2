#Questão 1
lista= list(range(0,10))
print(lista)
#a)
lista.append(6)
print(lista)
#b)
lista.insert(3,7)
print(lista)
#c)
lista.remove(3)
print(lista)
#d)
lista.append(4)
print(lista)
#e)
print(lista.count(4))

#Questão 2
#a)
print(lista[:3])
#b)
print(lista[2:7])
#c)
print(lista[::3])
#d)
print(lista[-3:])
#e)
print(lista[0:8])

#Questão 3
print(lista[5:6])

#Questão 4
lista[6] = 12
print(lista)

#Questão 5
lista.reverse()
print(lista)

#Questão 6
lista.sort()
print (lista)

#Questão 7
tupla=tuple(range(0,10))
print(tupla)
#a)tupla é imutavel, ou seja, não é possivel alterar seus valores
#b)
print(lista.index(5) +1)
