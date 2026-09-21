with open("numeros.txt","w", encoding="UTF-8") as arquivo:
    for numero in range (1,21):
        arquivo.write (f"{numero}\n")

with open ("numeros.txt", "r", encoding="UTF-8") as arquivo:
    for numero in arquivo:
        print(numero.strip())

with open("numeros.txt", "a", encoding="utf-8") as arquivo:
    for numero in range(21, 31):
        arquivo.write(f"{numero}\n")

with open("numeros.txt", "r", encoding="utf-8") as arquivo:

    for numero in arquivo:
        print(numero.strip())