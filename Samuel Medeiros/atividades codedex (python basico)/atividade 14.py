#nessa atividade se foi criado um codigo que verifica se a pessoa pode andar na montanha russa, e foi assim que ficou

height = int(input("digite a sua altura. "))
credits = int(input("digite quantos creditos você tem. "))
if height >= 137 and credits >= 10:
  print("aproveitem a viagem!. ")
elif height < 137 and credits >= 10:
  print("você não é alto o suficiente para andar. ")
elif height >= 137 and credits < 10:
  print("você não tem creditos para pagar. ")
else:
  print("voce não compriu nenhum dos requisitos. ")
