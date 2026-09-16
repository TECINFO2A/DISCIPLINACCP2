notas=[7.5, 8.0, 6.5, 9.0, 7.0]
print('maior nota:',max(notas))
print('menor nota:', min(notas))
print('quantidade de notas:',len(notas))
print('soma das notas:', sum(notas))
print('media das notas:', sum (notas)/len(notas))
notas.sort()
print('notas em ordem:',(notas))
print('as tres maiores notas:', (notas[-3:]))
