meu_dicionario = {

    "key1": "Joalison",
    "key2": "Josias",
    "key3": "João",
    "key4": "Maria",
    "key5": "Pedro",
    "key6": "Ana",
}

print("Keys do dicionário: ", meu_dicionario.keys())

print("Values do dicionário: ", meu_dicionario.values())

print("Items do dicionário: ", meu_dicionario.items())

segunda_chave = "key2"
print("O valor da segunda chave é: ", meu_dicionario[segunda_chave])

print("Dicionário completo: ", meu_dicionario)

print("Percorendo o dicionário com for:")
for key, value in meu_dicionario.items():
    print(key, ":", value)

    