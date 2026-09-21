arquivo = open("alunos.txt" , "w")

arquivo.write("ana\n")
arquivo.write("lucas\n")
arquivo.write("mateus\n")
arquivo.write("isis\n")
arquivo.write("robson\n")

with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    for nome in arquivo:
        print("Aluno:", nome.strip())