arquivo = open("numeros.txt", "w")

for numero in range(1, 11):
    arquivo.write(str(numero) + "\n")

arquivo.close()

arquivo = open("numeros.txt", "r")

conteudo = arquivo.read()
print("Números de 1 a 10:")
print(conteudo)

arquivo.close()

arquivo = open("numeros.txt", "w")

for numero in range(11, 21):
    arquivo.write(str(numero) + "\n")

arquivo.close()

arquivo = open("numeros.txt", "a")

for numero in range(21, 31):
    arquivo.write(str(numero) + "\n")

arquivo.close()

arquivo = open("numeros.txt", "r")

print("Números de 11 a 30:")
print(arquivo.read())

arquivo.close()

arquivo = open("numeros.txt", "r")

print("Números linha por linha:")

for linha in arquivo:
    print(linha.strip())

arquivo.close()
