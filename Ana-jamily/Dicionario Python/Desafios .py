#Desáfio 01

arquivo = open("alunos.txt", "w", encoding="utf-8")
arquivo.write("Ana\nDedé\nDidi\nMussum\nZacarias\n")
arquivo.close()

print("Ficheiro criado!!!")

#Desáfio 02
arquivo = open("alunos.txt", "r", encoding="utf-8")
print(arquivo.read())
arquivo.close()

#Desáfio 03
arquivo = open("alunos.txt", "r", encoding="utf-8")
for linha in arquivo:
    print("Aluno:", linha.strip())
arquivo.close()

#Desáfio 04
arquivo = open("numeros.txt", "w", encoding="utf-8")
for i in range(1, 21):
    arquivo.write(str(i) + "\n")
arquivo.close()


arquivo = open("numeros.txt", "r", encoding="utf-8")
print(arquivo.read())
arquivo.close()

#Desáfio 05

arquivo = open("numeros.txt", "a", encoding="utf-8")
for i in range(21, 31):
    arquivo.write(str(i) + "\n")
arquivo.close()

#Desáfio 06

arquivo = open("mensagem.txt", "w", encoding="utf-8")
arquivo.write("Primeira mensagem\n")
arquivo.close()

arquivo = open("mensagem.txt", "w", encoding="utf-8")
arquivo.write("Nova mensagem\n")
arquivo.close()

#Desafio 07

arquivo = open("alunos.txt", "a", encoding="utf-8")
nome = input("Digite o nome do aluno: ")
arquivo.write(nome + "\n")
arquivo.close()