produtos={
    "televisão": 2500,  
    "Notebook": 1800,
    "Teclado": 150,
    "Mouse": 80,
    "sofá": 900
}


print("Produtos:")
for produto in produtos.keys():
    print(produto)

print("\nPreços:")
for preco in produtos.values():
    print(preco)


print("\nProduto e preço:")
for produto, preco in produtos.items():
    print(produto, "-> R$", preco)

produto_mais_caro = max(produtos, key=produtos.get)

print("\nProduto mais caro:")
print(produto_mais_caro, "-> R$", produtos[produto_mais_caro])