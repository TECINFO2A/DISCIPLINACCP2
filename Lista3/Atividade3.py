# QUESTÃO 1
alunos = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda"]

# a
print("Alunos iniciais:", alunos)

# b
alunos.append("Fernando")

# c
alunos.remove("Bruno")

# d
alunos[2] = "Gabriela"

# e
primeiros_3 = alunos[:3]
ultimos_2 = alunos[-2:]
print("Primeiros 3:", primeiros_3)
print("Últimos 2:", ultimos_2)

# f
alunos.reverse()
print("Invertidos:", alunos)

# g
alunos.sort()
print("Ordenados:", alunos)
print()

# QUESTÃO 2
notas = [7.5, 8.0, 6.5, 9.0, 5.5]

# a
maior_nota = max(notas)
menor_nota = min(notas)

# b
quantidade = len(notas)

# c
soma = sum(notas)

# d
media = soma / quantidade

# e
notas.sort()

# f
tres_maiores = sorted(notas, reverse=True)[:3]

print("--- Resultado da Análise de Notas ---")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
print(f"Quantidade de notas: {quantidade}")
print(f"Soma total: {soma}")
print(f"Média: {media:.2f}")
print(f"Notas ordenadas: {notas}")
print(f"As 3 maiores notas: {tres_maiores}")