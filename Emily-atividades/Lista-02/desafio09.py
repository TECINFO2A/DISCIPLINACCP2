# a) Escreva os números de 1 a 10 no arquivo
with open("numeros.txt", "w") as arquivo:
    for numero in range(1, 11):
        arquivo.write(str(numero) + "\n")


# b) Imprima na tela todos os números do arquivo
with open("numeros.txt", "r") as arquivo:
    print(arquivo.read())


# c) Substitua os números 1 a 10 pelos números 11 a 20
with open("numeros.txt", "w") as arquivo:
    for numero in range(11, 21):
        arquivo.write(str(numero) + "\n")


# d) Adicione os números 21 a 30 no final do arquivo
with open("numeros.txt", "a") as arquivo:
    for numero in range(21, 31):
        arquivo.write(str(numero) + "\n")


# e) Imprima todos os números do arquivo novamente
with open("numeros.txt", "r") as arquivo:
    print(arquivo.read())


# f) Imprima os números linha por linha
with open("numeros.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())