#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

dados = {}

while True:
    dados["nome"]= (str(input("Qual o seu nome ?"))).strip()
    nasci = int(input("Em que ano você nasceu ?"))
    idade = 2025 - nasci
    dados["Idade"] = idade
    clt = dados["ctps"]=(int(input("Carteira de trabalho (0 = não tem): ")))
    if clt == 0:
        break
    elif clt < 0:
        print("Carteira invalida")
        continue
    else:
        dados["salário"]=(int(input("Digite seu salário: ")))
        contratado =dados["contratação"]=(int(input("Ano de contratação")))
        if contratado < nasci:
            print("Idade ou contratação invalida")
            continue
        break


for k,v in dados.items():
    if k == "contratação":
        print(f"Sua aposentadoria será em {v + 35 } anos")
    print(f"{k} = {v}")