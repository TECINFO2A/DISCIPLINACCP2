Lista=[0,1,2,3,4,5,6,7,8,9]

Lista.append(6)
Lista.insert(2,7)
Lista.remove(3)
Lista.append(4)
ocorrencias = Lista.count(4)

print("lista final:", Lista)
print("O número 4 aparece", ocorrencias, "vezes.")
