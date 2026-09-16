# Desafio 1 - Lista de Alunos

# Criando a lista com 5 nomes
alunos = ["Ana", "Bruno", "Carla", "Diego", "Elisa"]

# Missão 1: Imprimir a lista original
print("Lista original:", alunos)

# Missão 2: Adicionar um sexto aluno
alunos.append("Fernanda")
print("Após adicionar o sexto aluno:", alunos)

# Missão 3: Remover um aluno
alunos.remove("Bruno")
print("Após remover 'Bruno':", alunos)

# Missão 4: Alterar o aluno do índice 0 para "Otávio"
alunos[0] = "Otávio"
print("índice 0:", alunos)

# Missão 5: Fatiar a lista (primeiros 3 e últimos 2)
primeiros_tres = alunos[:3]
ultimos_dois = alunos[-2:]
print("Primeiros 3:", primeiros_tres)
print("Últimos 2:", ultimos_dois)

# Missão 6: Inverter a lista
alunos_invertidos = alunos[::-1]
print("Lista invertida:", alunos_invertidos)

# Missão 7: Ordenar a lista (ordem alfabética)
alunos_ordenados = sorted(alunos)
print("Lista ordenada:", alunos_ordenados)