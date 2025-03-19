#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

boletim = []
notas = []
while True:
    notas.append(str(input("Nome: ")))
    notas.append(float(input("1o Nota: ")))
    notas.append(float(input("2o Nota: ")))
    boletim.append(notas[:])
    notas.clear()
    pergunta = str(input("Quer continuar ?")).lower().strip()[0]
    if pergunta == 's' :
        continue
    elif pergunta not in 'n':
        if (str(input("Apenas sim ou nao, vc que continuar ?")).strip().lower()[0]) == 's':
            continue
        break
    break
print(boletim)
print("O boletim registrado é: ")
for p,nota in enumerate(boletim):
    media = (nota[1] + nota[2]) / 2
    print(f"{p}o - O aluno {nota[0]} tem na média: {media}")


while True:
    indice = int(input("Se quiser ver as notas individuais de um aluno, pressione o indice dele (para sair digite -8): "))
    if indice > -1 and indice < len(boletim):
        for pos,n in enumerate(boletim):
            if pos == indice:
                print(f"Notas: {n[1:]} de {n[0]}")
                print('-='*15)
    elif indice == -8:
        break
    else:
        print("Digite uma resposta valida")
        print('-='*15) 