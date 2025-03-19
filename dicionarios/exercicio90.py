#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.
boletim = {}
boletim["Nome"]=str(input("Qual o nome do aluno? ").strip())
while True:
    boletim["Media"]=float(input("Qual é a sua média? "))
    if 0 < boletim["Media"] <= 10:
        break
    else:
        print("nota invalida, digite novamente")
        continue

print(f"O aluno {boletim['Nome']}")
print(f"Teve de média {boletim['Media']} , Logo:")
if boletim["Media"] >= 7:
    boletim["Situação"] = "Aprovado"
    print("Aprovado")
elif 5 <= boletim["Media"] < 7:
    boletim["Situação"] = "Recuperação"
    print("Recuperação")
else:
    boletim["Situação"] = "Reprovado"
    print("Reprovado!")