lista = [5, 2, 8, 0, 3, 9, 1, 7, 4, ]
print(f"lista original: {lista}")

lista.append(6)
print(f"lista após o 6 ser adicionado: {lista}")

lista.insert(2, 7)
print(f"lista após o 7 ser inserido na posição 2: {lista}")

lista.remove(3)
print(f"lista após o elemento 3 ser removido: {lista}")

lista.append(4)
print(f"lista após o 4 ser adicionado: {lista}")

ocorrencias = lista.count(4)
print(f"o número 4 aparece {ocorrencias} vezes na lista")


primeiros_3 = lista[:3]
print("a. Primeiros 3 elementos:", primeiros_3)


da_3a_a_7a = lista[2:7]
print("b. Da 3ª até a 7ª posição:", da_3a_a_7a)