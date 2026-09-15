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

ultimos_3 = lista[-3:]
print("d. Últimos 3 elementos:", ultimos_3)

sem_ultimos_4 = lista[:-4]
print("e. Todos menos os 4 últimos:", sem_ultimos_4)

sexto_elemento = lista[5]
print("3. 6º elemento:", sexto_elemento)

lista[6] = 12
print("4. Lista após alterar o 7º elemento:", lista)

lista.reverse()
print("5. Lista invertida:", lista)

# 6. Ordene a lista
lista.sort()
print("6. Lista ordenada:", lista)