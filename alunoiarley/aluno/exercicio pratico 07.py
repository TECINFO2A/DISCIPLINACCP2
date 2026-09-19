aluno = {"nome": "João",
        "nota1": 8, 
        "nota2": 6
}

media = (aluno["nota1"] + aluno["nota2"]) / 2
print("media", media)

if media >=7:
    print("aprovado")
else:
    print("reprovado")
