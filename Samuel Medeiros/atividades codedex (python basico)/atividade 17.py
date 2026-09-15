#nessa atividade se foi criado um codigo que simula um jogo de adivinhação, e foi assim que ficou

guess = 0
tries = 0

while guess != 6:
    guess = int(input("Guess the number:  "))
    tries += 1
    
    if tries == 4 and guess != 6:
        break

if guess == 6:
    print("You got it!")
else:
    print("Game over! You ran out of tries.")