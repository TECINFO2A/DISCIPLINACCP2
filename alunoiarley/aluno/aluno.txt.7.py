while True:
    nome=input ("digite o nome do aluno ( ou 'exit'para finalizar):")

    if nome.lower() == "sair" :
        break
    with open("alunos.txt", "a", encoding="UTF-8") as arquivo:
        arquivo.write(nome+"\n")
    print("cadastro finalizado.")   