aluno = {
    "nome" : "Ana",
    "idade": 19,
    "curso" : "Ciência da Computação",
    "periodo" : 2,
    "nota" : 8.5
    }

print(aluno ["nome"])
print(aluno ["curso"])

aluno["idade"] = 22
print("Idade alterada:", aluno["idade"])

aluno["cidade"] = "Boqueirão"
print("Cidade adicionada:", aluno["cidade"])

for chave in aluno.keys():
    print(chave)

for valor in aluno.values():
    print(valor)

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

print("\n8. Dicionário completo:")
print(aluno)