#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.

lista=[[],[]]

for c in range(1,8):
    num=int(input(f"Digite o {c}o valor: "))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)
    else:
        print("Número inválido")


lista[0].sort()
lista[1].sort()

print(f"Os valores pares digitados foram: {lista[0]}")
print(f"Os valores inpares digitados foram: {lista[1]}")