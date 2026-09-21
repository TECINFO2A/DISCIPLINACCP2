with open("numeros.txt","w", encoding="UTF-8") as arquivo:
    for numero in range (1,21):
        arquivo.write (f"{numero}\n")

with open ("numeros.txt", "r", encoding="UTF-8") as arquivo:
    for numero in arquivo:
        print(numero.strip())