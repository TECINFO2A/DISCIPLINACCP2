nome=input('Digite seu nome:')
idade=int(input('Digite sua idade:'))
nota=float(input('Digite sua nota:'))

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Nota: {nota}')
if idade >= 18:
    print('Situação: Maior de idade')
else: 
    print('Situação: Menor de idade')
if nota >= 7:
    print('Resultado: Aprovado!')
else:
    print('Resultado: Reprovado')