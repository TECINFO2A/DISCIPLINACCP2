#Calculadora Completa em Python
print("==========================================")
print("========== CALCULADORA COMPLETA ==========")
print("==========================================")

while True:
    print("\n Escolha uma operação: ")
    print("1 - ADIÇÃO")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    print("5 - POTENCIAÇÃO")
    print("6 - RAIZ QUADRADA")
    print("7 - PORCENTAGEM")
    print("8 - MÉDIA")
    print("9 - TABUADA")
    print("0 - SAIR")
    break 
opção = input("\n Escolha uma opção: ")

#SOMA 
if opção == "1":
    n1 = float(input("digite o primeiro numero: "))
    n2 = float(input("digite o segundo numero: "))

    resultado = n1 + n2

    print(" Seu Resultado é:", resultado)

#SUBTRAÇÃO
elif opção == "2":
    n1 = float(input("digite o primeiro numero: "))
    n2 = float(input("digite o segundo numero: "))

    resultado = n1 - n2

    print(" Seu Resultado é:", resultado)

#MULTIPLICAÇÃO
elif opção == "3":
    n1 = float(input("digite o primeiro numero: "))
    n2 = float(input("digite o segundo numero: "))

    resultado = n1 * n2

    print(" Seu Resultado é:", resultado)

#DIVISÃO
elif opção == "4":
    n1 = float(input("digite o primeiro numero: "))
    n2 = float(input("digite o segundo numero: "))
    if n2 == 0:
        print(" Erro ! Não existe divisão por 0")
    else:
        resultado = n1 / n2
        print(" Seu Resultado é:", resultado)

#POTENCIAÇÃO
elif opção == "5":
    n1 = float(input("digite o primeiro numero: "))
    n2 = float(input("digite o segundo numero: "))

    resultado = n1 ** n2

    print(" Seu Resultado é:", resultado)

#RAIZ QUADRADA
elif opção == "6":
    n1 = float(input("digite o primeiro numero: "))
   
    if n1 < 0:
        print(" Não existe raiz de um numero negativo !")
    else:
        resultado = n1 * 0.5
    print(" Seu Resultado é:", resultado)

#PORCENTAGEM
elif opção == "7":
    n1 = float(input("digite o primeiro numero: "))
    porcentagem= float(input("digite o segundo numero: "))

    resultado = ( n1 * porcentagem) /100

    print(f"{porcentagem}% de {n1} é igual a: {resultado}")

#MÉDIA
elif opção == "8":
    quantidade = int(input("Quantas notas deseja inserir? "))

    soma = 0

    for i in range(quantidade):
      nota = float(input(f"Digite a nota {i+1}: "))
    soma += nota

    media = soma / quantidade

    print("Média:", media)

#TABUADA
elif opção == "9":
    n1 = int(input("digite um numero: "))

    print(" \n TABUADA DO", n1)

    for i in range(1, 11):
     print(f"{n1} x {i} = {n1 * i}")

#SAIR
elif opção == "0":
    print("Encerrando calculadora...")
    
#OPÇÃO INVÁLIDA
else:
    print("Opção inválida")


print("\n===================================")






