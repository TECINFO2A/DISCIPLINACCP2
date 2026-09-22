# Criando o arquivo
with open("numeros.txt", "w", encoding="utf-8") as arquivo:
    for numero in range(1, 21):
        arquivo.write(f"{numero}\n")

# Lendo o arquivo
with open("numeros.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())