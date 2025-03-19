#Exercício Python 022 Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.
#CURSO EM VIDEO

nome = str(input("Qual é o seu nome ?"))
print(f'Seu nome todo maiusculo é {nome.upper()}')
print(f'Seu nome todo minusculo fica {nome.lower()}')
print(f"Seu nome tem {len(nome) - nome.count(' ')} letras")
print(f"Tendo {nome.find(' ')} letras em seu primeiro nome")

