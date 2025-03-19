#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista=[13, 12]
while True:
    num = int(input("Digite um número: "))
    if num in lista:
        print(f"Este número ja está na lista")
        if str(input("Quer continuar digitando ?").strip().lower()[0]) == 's':
            continue
        break
    elif num not in lista:
        lista.append(num)
        print(f"Número adicionado!")
        if str(input("Quer continuar digitando ?").strip().lower()[0]) == 's':
            continue
        break
    else:
        print("Digite um número válido")
        continue

print(f"A lista em ordem crescente fica: {sorted(lista)}")
