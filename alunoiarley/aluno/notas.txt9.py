
with open("notas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Ana;8.5\n")
    arquivo.write("João;7.0\n")
    arquivo.write("Maria;9.5\n")
    arquivo.write("Pedro;6.5\n")
    arquivo.write("Iarley;10.0\n")

with open("notas.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        nome, nota = linha.strip().split(";")
        print(f"Aluno: {nome} - Nota: {nota}")