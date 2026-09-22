# Primeira gravação
with open("mensagem.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira mensagem")

# Substituição
with open("mensagem.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Nova mensagem")

# Leitura
with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
    mensagem = arquivo.read()

print(mensagem)