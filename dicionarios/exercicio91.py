#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
rank= {}
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6),}

for k,v in jogo.items():
    print(f"O {k} tirou no dado {v}")
rank =sorted(jogo.items(), key=lambda item: item[1], reverse=True)

for i,t in enumerate(rank):
    print(f"\n{i}o Lugar:O jogador{i} com o valor de: {t[1]}")
