lista_inicial = [0 , 1 , 2, 3 , 4 , 5 , 6 , 7 , 8 , 9]
print("Lista inicial: ", lista_inicial)

lista_inicial.append(6)
print("adicionei o 6", lista_inicial)

lista_inicial.insert(2 , 7)
print("adicionei o 7 na posição 3", lista_inicial)

lista_inicial.remove(3)
print("removi o 3", lista_inicial)

lista_inicial.append(4)
print("adicionei o 4", lista_inicial)

n_ocorrencias = lista_inicial.count(4)
print("o número 4 aparece", n_ocorrencias, "vezes na lista")