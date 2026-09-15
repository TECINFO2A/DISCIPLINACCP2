lista_aleatoria = ["bruna", "joao", "maria", "pedro", "ana", "carlos", "joalison"]

print("Lista original:", lista_aleatoria)

lista_aleatoria.append("Fernanda")
print("Lista após adicionar um elemento:", lista_aleatoria)

lista_aleatoria.remove("joao")
print("Lista após remover um elemento:", lista_aleatoria)

lista_aleatoria[2] = "Lucas"
print("Lista após alterar um elemento:", lista_aleatoria)

primeiros_tres = lista_aleatoria[:3]
print("Primeiros três elementos da lista:", primeiros_tres)
ultimos_dois = lista_aleatoria[-2:]
print("Últimos dois elementos da lista:", ultimos_dois)

lista_aleatoria.sort()
print("Lista ordenada:", lista_aleatoria)

lista_aleatoria.reverse()
print("Lista invertida:", lista_aleatoria)

