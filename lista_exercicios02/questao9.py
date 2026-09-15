"""
Questão 9: Crie um arquivo e faça as operações de escrita/leitura pedidas.
"""

nome_arquivo = "numeros.txt"

# a. Escrevendo os números de 1 a 10 no arquivo
# O modo "w" cria o arquivo (ou apaga o conteúdo se ele já existir)
with open(nome_arquivo, "w") as arquivo:
    for numero in range(1, 11):
        arquivo.write(f"{numero}\n")

# b. Lendo e mostrando tudo o que está no arquivo
with open(nome_arquivo, "r") as arquivo:
    conteudo = arquivo.read()
print("Conteúdo do arquivo (1 a 10):")
print(conteudo)

# c. Substituindo o conteúdo pelos números de 11 a 20
# Uso o modo "w" de novo, porque ele sobrescreve o que já estava lá
with open(nome_arquivo, "w") as arquivo:
    for numero in range(11, 21):
        arquivo.write(f"{numero}\n")

# d. Adicionando os números de 21 a 30 SEM apagar o que já está no arquivo
# Pra isso uso o modo "a" (append), que escreve no final
with open(nome_arquivo, "a") as arquivo:
    for numero in range(21, 31):
        arquivo.write(f"{numero}\n")

# e. Mostrando tudo de novo (agora deve aparecer de 11 até 30)
with open(nome_arquivo, "r") as arquivo:
    conteudo = arquivo.read()
print("Conteúdo do arquivo (11 a 30):")
print(conteudo)

# f. Mostrando o conteúdo linha por linha
print("Conteúdo linha por linha:")
with open(nome_arquivo, "r") as arquivo:
    for linha in arquivo:
        # uso o strip() pra tirar a quebra de linha que vem no final de cada linha lida
        print(linha.strip())
