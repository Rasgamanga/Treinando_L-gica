
#Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz=[[],[],[]]
total_par = total_col = maior = 0
for p in range(0,3):
    for ps in range (0,3):
        num =int(input(f"Digite o número para a casa ({p},{ps}): "))
        matriz[p].append(num)
        if num % 2 == 0:
            total_par+=num
        if p == 2:
            total_col+=num
        if ps == 1 and not maior == 0:
            maior= num
        maior=num

print(f"A soma dos valores par é {total_par}")
print(f"A soma dos valores da terceira coluna é {total_col}")
print(f"E o maior valor da segunda linha é {maior}")