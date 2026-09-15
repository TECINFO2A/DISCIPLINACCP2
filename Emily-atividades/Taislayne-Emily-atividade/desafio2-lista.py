notas = [7.5, 8.0, 6.5, 9.0, 5.5]
maior = max(notas)
menor = min(notas)

quantidade = len(notas)
soma = sum(notas)

media = soma / quantidade
notas_ordenadas = sorted(notas)

tres_maiores = notas_ordenadas[-3:]
tres_maiores.reverse()

print("Notas:", notas)
print("Maior nota:", maior)
print("Menor nota:", menor)
print("Quantidade de notas:", quantidade)
print("Soma:", soma)
print("Média:", media)
print("Notas ordenadas:", notas_ordenadas)
print("3 maiores notas:", tres_maiores)