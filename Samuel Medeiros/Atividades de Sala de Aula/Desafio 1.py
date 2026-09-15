#ASS: Samuel Dantas de Araújo Medeiros  /  Gustavo da Silva Nascimento
nome1 = 'gustavo'
nome2 = "gabriel"
nome3 = 'joão'
nome4 = "maria"
nome5 = 'ana'

print("Nomes cadastrados: ")
print(nome1)
print(nome2)
print(nome3)
print(nome4)
print(nome5)

comando = input("Digite o comando: (Imprimir, Adicionar, Remover, Alterar, Inverter, Fatiar e Ordenar) ")

if comando == "Imprimir":
    print(nome1)
    print(nome2)
    print(nome3)
    print(nome4)
    print(nome5)

elif comando == "Adicionar":
    nome6 = input("Digite o nome que deseja adicionar: ")
    print(nome1)
    print(nome2)
    print(nome3)
    print(nome4)
    print(nome5)
    print(nome6)

elif comando == "Remover":
    nome_remover = input("Digite o nome que deseja remover: ")
    if nome_remover == nome1:
        print(nome2)
        print(nome3)
        print(nome4)
        print(nome5)
    elif nome_remover == nome2:
        print(nome1)
        print(nome3)
        print(nome4)
        print(nome5)
    elif nome_remover == nome3:
        print(nome1)
        print(nome2)
        print(nome4)
        print(nome5)
    elif nome_remover == nome4:
        print(nome1)
        print(nome2)
        print(nome3)
        print(nome5)
    elif nome_remover == nome5:
        print(nome1)
        print(nome2)
        print(nome3)
        print(nome4)

elif comando == "Alterar":
    nome_alterar = input("Digite o nome que deseja alterar: ")
    if nome_alterar == nome1:
        novo_nome = input("Digite o novo nome: ")
        print(novo_nome)
        print(nome2)
        print(nome3)
        print(nome4)
        print(nome5)
    elif nome_alterar == nome2:
        novo_nome = input("Digite o novo nome: ")
        print(nome1)
        print(novo_nome)
        print(nome3)
        print(nome4)
        print(nome5)
    elif nome_alterar == nome3:
        novo_nome = input("Digite o novo nome: ")
        print(nome1)
        print(nome2)
        print(novo_nome)
        print(nome4)
        print(nome5)
    elif nome_alterar == nome4:
        novo_nome = input("Digite o novo nome: ")
        print(nome1)
        print(nome2)
        print(nome3)
        print(novo_nome)
        print(nome5)
    elif nome_alterar == nome5:
        novo_nome = input("Digite o novo nome: ")
        print(nome1)
        print(nome2)
        print(nome3)
        print(nome4)
        print(novo_nome)

elif comando == "Inverter":
    print(nome5)
    print(nome4)
    print(nome3)
    print(nome2)
    print(nome1)

elif comando == "Fatiar":
    print("Digite o índice inicial e final para fatiar os nomes: ")
    indice_inicial = int(input("Índice inicial: "))
    indice_final = int(input("Índice final: "))
    nomes = [nome1, nome2, nome3, nome4, nome5]
    nomes_fatiados = nomes[indice_inicial:indice_final]
    for nome in nomes_fatiados:
        print(nome)

elif comando == "Ordenar":
    nomes = [nome1, nome2, nome3, nome4, nome5]
    nomes.sort()
    for nome in nomes:
        print(nome)

