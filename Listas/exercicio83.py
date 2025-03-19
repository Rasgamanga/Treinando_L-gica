
#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


lista=[]

expressao=str(input("Digite uma expressão(com parenteses): ")).strip()
#expressao=' '.join(expressao) (eu pensando que tinha que separar os elementos dentro da lista para o for ler, mas precisava fazer nada, mas vou deixar ai pq é legal)
#expressao = expressao.split()
for elemen in expressao:
    if elemen == '(':
        lista.append(')')
    if elemen == ')':
        lista.pop()

if len(lista)==0:
    print("Expressão valida")

else:
    print("Expressão invalida")
