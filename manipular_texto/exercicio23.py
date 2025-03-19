
#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Qual o nome da cidade ?')).title().strip().split()
if 'Santo' in cidade[0]:
    print('Sua cidade começa com a palavra "Santo"')
else:
    print('Não começa com a palavra "Santo"')
