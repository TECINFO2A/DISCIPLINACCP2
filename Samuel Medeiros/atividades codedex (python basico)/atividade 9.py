#nessa atividade se foi criado um codigo que converte moedas para dolares, e foi assim que ficou

CO = int(input("quantos Pesos colombianos você tem? "))
PE = int(input("quantas Solas peruanas você tem? "))
BR = int(input("Quantos Reais brasileiros você tem "))
USD = (CO*0.00026) + (PE*0.29) + (BR*0.20)
print("Vocês possuem",USD,"dolares")