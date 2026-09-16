nome = input('Digite seu nome:')
print(f'É um prazer te conhecer, {nome}!')
media=input('informe sua media: ')

if int(media)>=8:
    print(f'Excelente {nome}! Você foi aprovado!')
elif int(media)==7:
    print(f'Otimo {nome}! Você está na media!')
else:
    print(f"Infelismente {nome}, você foi reprovado!")

