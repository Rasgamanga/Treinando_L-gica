#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.


nome = str(input("Qual é o seu nome completo ?")).title().strip().split()
print(f"Seu primeiro nome é {nome[0]}")
print(f"E o seu ultimo nome é {nome[-1]}")
