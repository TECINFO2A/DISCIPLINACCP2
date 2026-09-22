with open("alunos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Ana\n")
    arquivo.write("João\n")
    arquivo.write("Maria\n")
    arquivo.write("Pedro\n")
    arquivo.write("Carlos\n")

print("Arquivo criado com sucesso!")

with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)