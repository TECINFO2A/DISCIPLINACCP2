#nessa atividade se foi criado um codigo que simula o sistema de casas de harry potter, e foi assim que ficou

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

Q1 = int(input("Do you like Dawn or Dusk? 1. Dawn, 2. Dusk "))
Q2 = int(input("When I’m dead, I want people to remember me as: 1. The Good, 2. The Great, 3. The Wise, 4. The Bold "))
Q3 = int(input("Which kind of instrument most pleases your ear? 1. The violin, 2. The trumpet, 3. The piano, 4. The drum ")) 

if Q1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif Q1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input")

if Q2 == 1:
    hufflepuff += 2
elif Q2 == 2:
    slytherin += 2 
elif Q2 == 3: 
    ravenclaw += 2
elif Q2 == 4:
    gryffindor += 2
else:
    print("Wrong input")

if Q3 == 1:
    slytherin += 4
elif Q3 == 2:
    hufflepuff += 4
elif Q3 == 3:
    ravenclaw += 4
elif Q3 == 4:
    gryffindor += 4
else:
    print("Wrong input")

print(f"Gryffindor: {gryffindor}")
print(f"Ravenclaw: {ravenclaw}")
print(f"Hufflepuff: {hufflepuff}")
print(f"Slytherin: {slytherin}")
