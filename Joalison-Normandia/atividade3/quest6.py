produto = {"notebook": 2500, "mouse": 100, "teclado": 150, "monitor": 800}

for chave, valor in produto.items():
    print(f"Produto: {chave}, Preço: R${valor:.2f}")