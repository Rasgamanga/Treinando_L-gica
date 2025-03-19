#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    pergunta = str(input("Quer continuar ?")).lower().strip()[0]
    if pergunta in 'n':
        break
    elif pergunta in 's':
        continue
    else:
        print("Resposta invalida!")
        print('-='*15)
        if str(input("Quer continuar ?(Sim ou Não) ").strip().lower()[0]) == 's':
            continue
        break

for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)

print(f"Você digitou esses valores: {lista}")
print(f"Listas de pares: {pares}")
print(f"Lista de impares: {impares} ")
