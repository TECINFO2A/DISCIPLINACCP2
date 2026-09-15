#nessa atividade se foi criado um codigo que calcula o IMC de uma pessoa

weight = float(input("Digite o seu peso em KG "))
height = float(input("Digite a sua altura em M "))
imc = weight / height ** 2
print(f"Seu IMC é: {imc:.2f}")