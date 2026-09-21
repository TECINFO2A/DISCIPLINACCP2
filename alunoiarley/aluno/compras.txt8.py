
with open("compras.txt", "w", encoding="utf-8") as arquivo:
    for i in range(5):
        produto = input(f"Digite o {i + 1}º produto: ")
        arquivo.write(produto + "\n")

with open("compras.txt", "r", encoding="utf-8") as arquivo:
    produtos = arquivo.readlines()

print("\nLista de compras:")

for i, produto in enumerate(produtos, start=1):
    print(f"{i}. {produto.strip()}")