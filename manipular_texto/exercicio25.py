#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

nome = str(input('Digite uma frase: ')).strip().lower()
nome =''.join(nome.split())
nome = nome.replace('á','a')
print(f"Sua frase tem {nome.count('a')} letras A")
print(f"Sendo a primeira na posição {nome.find('a')+1}")
print(f"E a ultima na {nome.rfind('a')+1}")
