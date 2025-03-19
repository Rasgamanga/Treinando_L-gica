#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

lista = []
maximo=[]
minimo=[]
for cont in range(0,5):
    lista.append(int(input(f"Digite um valor para a posição {cont + 1}: ")))

maxi = max(lista)
mini = min(lista)
for pos,valores in enumerate(lista):
    if maxi == valores:
        maximo.append(pos+1)
    if mini == valores:
        minimo.append(pos+1)

print(f"O maior valor foi {maxi} e aparecendo nas posições", end=' ')
for pos_max in maximo:
    print(pos_max,end='...')

print(f"\nO menor valor foi {mini} e está nas posições ",end=' ')
for pos_min in minimo:
    print(pos_min,end='...')