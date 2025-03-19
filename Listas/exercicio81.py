#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    pergunta = str(input("Quer continuar ?").lower().strip()[0])
    if  pergunta == 's':
        continue
    elif pergunta == 'n':
        break
    else:
        print("Resposta invalida")
        print('-='*15)
        if str(input("Voce quer continuar ? (sim ou não)").lower().strip()[0]):
            continue
        else:
            break

print(f"Foi digitado no total {len(lista)} números")
lista.sort(reverse=True)
print(f"A lista dos valores em ordem descrecente fica: {lista}")
if lista.index(5) == True:
    print("Tem um número 5 em sua lista")
else:
    print("O número 5 não está presente em sua lista")
