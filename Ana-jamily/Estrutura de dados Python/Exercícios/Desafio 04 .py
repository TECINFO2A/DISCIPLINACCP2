
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Carlos", "nota": 7.0},
    {"nome": "Maria", "nota": 9.2},
    {"nome": "João", "nota": 6.5}
]


print("--- Lista de Alunos ---")
for aluno in alunos:
    print(f"Nome: {aluno["nome"]} - Nota: {aluno["nota"]}")


soma_notas = sum(aluno["nota"] for aluno in alunos)
media = soma_notas / len(alunos)

print(f"Média da turma: {media:.2f}")