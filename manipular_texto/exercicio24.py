#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual é o seu nome ?')).strip().title()
if "Silva" in nome:
    print('Seu Nome tem "Silva"')
else:
    print('Não tem "Silva"')
