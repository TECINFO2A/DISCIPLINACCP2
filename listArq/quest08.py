# Cadastro dos produtos
with open("compras.txt", "w", encoding="utf-8") as arquivo:

    for i in range(5):
        produto = input(f"Digite o produto {i + 1}: ")
        arquivo.write(produto + "\n")


# Leitura dos produtos
with open("compras.txt", "r", encoding="utf-8") as arquivo:

    produtos = arquivo.readlines()


# Apresentação numerada
print("\nLISTA DE COMPRAS")

for i, produto in enumerate(produtos, start=1):
    print(f"{i} - {produto.strip()}")