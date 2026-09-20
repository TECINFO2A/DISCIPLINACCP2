#Questão 1- Cadastro do Aluno
Aluno={"Nome" : "Pedro",
    "Idade": "18",
    "cidade" : "Lagoa Seca",
    "Curso" : "C.C."}
print(Aluno)
print(Aluno["Nome"])
print(Aluno["Curso"])

#Questão 2- Alteração
Aluno["Idade"]="19"
Aluno["Curso"]="Direito"
print(Aluno)

#Questão 3- Nova informação
Aluno["Email"]="pedrin23candido@gmail.com"
Aluno["Telefone"]="839123940"
print(Aluno)

#Questão 4- Remoção
Aluno.pop("Telefone")
print(Aluno)

#Questão 5- Verificação
if "Email" in Aluno:
    print("O Email existe!")

#Questão 6- Percorrendo o dicionário 
for chave, valor in Aluno.items():
    print(valor)
