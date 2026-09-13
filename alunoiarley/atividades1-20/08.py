Aluno = {
"nome": "iarley",
"idade": 18,
"curso": "Computação",
"cidade": "mogeiro",
"ano":2026
}

print("Chaves:")
print(Aluno.keys())

print("Valores:")
print(Aluno.values())

print("Itens:")
print(Aluno.items())

print("item dois:")
print(list(Aluno.items())[1])

print("Dicionário completo:")
print(Aluno)

for chave, valor in Aluno.items():
    print(f"{chave} tem como valor {valor}")


