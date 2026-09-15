#nessa atividade se foi criado um codigo que verifica se o ph é acido, basico ou neutro, e foi assim que ficou

ph = int(input("digite o valor do ph. "))
if ph > 7:
  print("Basic")
elif ph < 7:
  print("Acid")
else:
  print("neutro")

