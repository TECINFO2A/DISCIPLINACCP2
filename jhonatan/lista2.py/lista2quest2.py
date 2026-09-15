# Continuando com a lista manipulada na questão anterior:
# numeros = [0, 8, 7, 2, 5, 1, 9, 4, 6, 4]


primeiros_tres = numeros[:3]


terceiro_ao_setimo = numeros[2:7]

# c
de_tres_em_tres = numeros[::3]

# d
ultimos_tres = numeros[-3:]

# e
menos_quatro_ultimos = numeros[:-4]


print("a. Primeiros 3 elementos:", primeiros_tres)
print("b. Da 3ª à 7ª posição:", terceiro_ao_setimo)
print("c. De 3 em 3 elementos:", de_tres_em_tres)
print("d. Últimos 3 elementos:", ultimos_tres)
print("e. Todos menos os 4 últimos:", menos_quatro_ultimos)