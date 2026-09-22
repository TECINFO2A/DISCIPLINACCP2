# a) Adicionar os números de 21 a 30
with open("numeros.txt", "a", encoding="utf-8") as arquivo:
    for numero in range(21, 31):
        arquivo.write(f"{numero}\n")

# b) Ler o arquivo
with open("numeros.txt", "r", encoding="utf-8") as arquivo:
    numeros = arquivo.readlines()

# c) Mostrar todos os números
for numero in numeros:
    print(numero.strip())