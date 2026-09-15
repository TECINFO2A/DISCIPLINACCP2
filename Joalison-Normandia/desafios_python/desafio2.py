notas = [7.5 , 8.5 , 9, 6.5, 10, 4, 7.5, 8, 9.5]

maior_nota = max(notas)
menor_nota = min(notas)

print("A maior nota é:", maior_nota)
print("A menor nota é:", menor_nota)

contar_quantidade = len(notas)
print("A quantidade de notas é:", contar_quantidade)

soma_notas = sum(notas)
print("A soma das notas é:", soma_notas)

media_notas = soma_notas / contar_quantidade
print("A média das notas é:", media_notas)

notas_ordenadas = sorted(notas)
print("As notas em ordem crescente são:", notas_ordenadas)

menores_notas = sorted(notas)[:3]
print("As 3 menores notas são:", menores_notas)

maiores_notas = sorted(notas)[-3:]
print("As 3 maiores notas são:", maiores_notas)
