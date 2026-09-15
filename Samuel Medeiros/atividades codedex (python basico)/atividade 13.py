#nessa atividade se foi criado um codigo que simula uma bola 8 magica, e foi assim que ficou

import random
question = input("question: ")
num =random.randint(1,9)
if num == 1: 
  print(f"{question}, Yes - definitely.")
elif num == 2:
  print(f"{question}, It is decidedly so.")
elif num == 3:
  print(f"{question}, Without a doubt.")
elif num == 4:
  print(f"{question}, Reply hazy, try again.")
elif num == 5:
  print(f"{question}, Ask again later.")
elif num == 6:
  print(f"{question}, Better not tell you now.")
elif num == 7:
  print(f"{question}, My sources say no.")
elif num == 8:
  print(f"{question}, Outlook not so good.")
elif num == 9:
  print(f"{question}, Very doubtful")
