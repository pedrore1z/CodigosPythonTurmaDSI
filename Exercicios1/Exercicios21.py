valores = list()

for cont in range(0,10):
    valores.append(int(input(f"Informe o valor {cont+1}: ")))

print(valores)

for indice,cont in range(0,10):
    if valores[itens] % 2 == 0:
        valores.pop(itens)
        #valores remove (cont)

print(f"Lista sem os valores pares: {valores}\n\n")