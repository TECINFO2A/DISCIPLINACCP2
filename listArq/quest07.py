with open("alunos.txt", "a", encoding="utf-8") as arquivo:

    quantidade = int(input("Quantos alunos deseja cadastrar? "))

    for i in range(quantidade):
        nome = input(f"Digite o nome do aluno {i + 1}: ")
        arquivo.write(nome + "\n")

print("Alunos cadastrados com sucesso!")