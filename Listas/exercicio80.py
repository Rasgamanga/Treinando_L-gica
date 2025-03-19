
#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela.


lista = []

for n in range(0,5):
    num = int(input("Digite um número: "))
    if n == 0:
        lista.append(num)
    else:
        for pos in range (len(lista)):
            if num < lista[pos]:
                lista.insert(pos,num)
                break
        if num > max(lista):
            lista.append(num)
            break
print((lista))
