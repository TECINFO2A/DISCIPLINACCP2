ARQUIVO = "alunos.txt"


def cadastrar_aluno():
    print("\n--- CADASTRAR ALUNO ---")

    nome = input("Nome: ")
    idade = input("Idade: ")
    curso = input("Curso: ")
    nota = input("Nota: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "nota": nota
    }

    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"{aluno['nome']};"
            f"{aluno['idade']};"
            f"{aluno['curso']};"
            f"{aluno['nota']}\n"
        )

    print("Aluno cadastrado com sucesso!")

def listar_alunos():

    print("\n--- LISTA DE ALUNOS ---")

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

            alunos = arquivo.readlines()

            if not alunos:
                print("Nenhum aluno cadastrado.")
                return

            for numero, linha in enumerate(alunos, start=1):

                dados = linha.strip().split(";")

                # Verifica se a linha possui exatamente 4 informações
                if len(dados) != 4:
                    print(f"\nLinha {numero} inválida:")
                    print(linha.strip())
                    print("Esperado: nome;idade;curso;nota")
                    continue

                nome, idade, curso, nota = dados

                print(f"\nAluno {numero}")
                print(f"Nome: {nome}")
                print(f"Idade: {idade}")
                print(f"Curso: {curso}")
                print(f"Nota: {nota}")

    except FileNotFoundError:
        print("Nenhum aluno cadastrado.")


def pesquisar_aluno():
    print("\n--- PESQUISAR ALUNO ---")

    nome_pesquisa = input("Digite o nome do aluno: ")

    encontrado = False

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

            for linha in arquivo:

                nome, idade, curso, nota = linha.strip().split(";")

                if nome.lower() == nome_pesquisa.lower():

                    print("\nAluno encontrado!")
                    print("Nome:", nome)
                    print("Idade:", idade)
                    print("Curso:", curso)
                    print("Nota:", nota)

                    encontrado = True
                    break

        if not encontrado:
            print("Aluno não encontrado.")

    except FileNotFoundError:
        print("Nenhum aluno cadastrado.")


def alterar_aluno():
    print("\n--- ALTERAR ALUNO ---")

    nome_pesquisa = input("Digite o nome do aluno que deseja alterar: ")

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        encontrado = False

        for i in range(len(linhas)):

            nome, idade, curso, nota = linhas[i].strip().split(";")

            if nome.lower() == nome_pesquisa.lower():

                print("\nAluno encontrado.")

                novo_nome = input(f"Novo nome [{nome}]: ")
                nova_idade = input(f"Nova idade [{idade}]: ")
                novo_curso = input(f"Novo curso [{curso}]: ")
                nova_nota = input(f"Nova nota [{nota}]: ")

                if novo_nome == "":
                    novo_nome = nome

                if nova_idade == "":
                    nova_idade = idade

                if novo_curso == "":
                    novo_curso = curso

                if nova_nota == "":
                    nova_nota = nota

                linhas[i] = (
                    f"{novo_nome};"
                    f"{nova_idade};"
                    f"{novo_curso};"
                    f"{nova_nota}\n"
                )

                encontrado = True
                break

        if encontrado:

            with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                arquivo.writelines(linhas)

            print("Aluno alterado com sucesso!")

        else:
            print("Aluno não encontrado.")

    except FileNotFoundError:
        print("Nenhum aluno cadastrado.")


def remover_aluno():
    print("\n--- REMOVER ALUNO ---")

    nome_pesquisa = input("Digite o nome do aluno que deseja remover: ")

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        novas_linhas = []
        encontrado = False

        for linha in linhas:

            nome, idade, curso, nota = linha.strip().split(";")

            if nome.lower() == nome_pesquisa.lower():

                encontrado = True

            else:
                novas_linhas.append(linha)

        if encontrado:

            with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                arquivo.writelines(novas_linhas)

            print("Aluno removido com sucesso!")

        else:
            print("Aluno não encontrado.")

    except FileNotFoundError:
        print("Nenhum aluno cadastrado.")


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

while True:

    print("\n================================")
    print("        SISTEMA DE ALUNOS")
    print("================================")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Pesquisar aluno")
    print("4 - Alterar aluno")
    print("5 - Remover aluno")
    print("6 - Sair")
    print("================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        pesquisar_aluno()

    elif opcao == "4":
        alterar_aluno()

    elif opcao == "5":
        remover_aluno()

    elif opcao == "6":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")