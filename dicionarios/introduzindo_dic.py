cartaz= []
filme1 = {}

for c in (0,3):
    filme1['titulo']=str(input("Nome do filme para expor: "))
    filme1['Ano']=int(input("Data de publicação: "))
    cartaz.append(filme1.copy())


for i in cartaz:
    for k,v in i.items():
        print(f" {k}  {v}")

