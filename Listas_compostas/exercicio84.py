#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

lista = []
dados = []
listagem_menor = []
listagem_maior = []
pessoas= 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    pessoas+=1
    lista.append(dados[:])
    dados.clear()
    pergunta = str(input("Quer continuar ?").strip().lower()[0])
    if pergunta in 'n':
        break
    elif pergunta in 's':
        continue
    else:
        print("Resposta inválida.", end= '')
        if str(input("Voce quer continuar ? (sim ou nao)").lower().strip()[0]) == 's':
            continue
        break
peso_menor = 0
peso_maior = 0
c = 0
for p in lista:
    if c > 0:
        if p[1] <= peso_menor:
            listagem_menor.append(p)
            peso_menor = p[1]
            continue

        elif p[1] >= peso_maior:
            listagem_maior.append(p)
            peso_maior = p[1]
            continue
    listagem_menor.append(p)
    listagem_maior.append(p)
    peso_menor = peso_maior = p[1]
    c+=1
    continue

maximo = max(listagem_maior)
minimo = min(listagem_menor)
print(f"Você cadastrou {pessoas} pessoas")
print(f"O maior peso foi {maximo[1]} de ", end= '')
for posM in listagem_maior:
    if posM[1] == peso_maior:
        print(f"{posM[0]}", end= ' ')

print(f"\nO menor peso foi {minimo[1]} de ", end= '')
for posm in listagem_menor:
    if posm[1] == peso_menor:
        print(f"{posm[0]}", end=' ')
