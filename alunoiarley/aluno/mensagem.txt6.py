
with open("mensagem.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("olá, mundo")

with open("mensagem.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("estou praticando")

with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
    mensagem = arquivo.read()
    print(mensagem)