#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.

matriz=[[0,0,0],[0,0,0],[0,0,0]]
for p in range(0,3):
    for ps in range (0,3):
        #matriz[p].append(int(input("Digite um numero para a posição ({p},{ps}): ")))
        matriz[p][ps]=int(input(f"Digite um numero para a posição ({p},{ps}): "))

for l in range(0,3):
    for c in range(0,3):
        print(f"{matriz[l][c]}", end=' ,')
    print( )
