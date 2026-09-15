#nessa atividade se foi criado um codigo que simula o lançamento de uma moeda, e foi assim que ficou

import random

num = random.randint(0, 1) 

if num > 0.5: 
  print('heads')
else:
  print("tails")