#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
matriz=[[0],[0],[0],[0],[0],[0]]
verificar = []
jogos=int(input("Quantos jogos vc quer sortear ? "))
for c in range(1,jogos+1):
    for p in range(0,6):
        valor = randint(1,60)
        matriz[p][0]= (valor)

        if valor in verificar:
            a =verificar.index(valor)
            verificar.pop(a)
            continue
        verificar.append(valor)
    matriz.sort()
    print(f"Seu {c}o jogo esta aqui: {matriz}")
    verificar.clear()