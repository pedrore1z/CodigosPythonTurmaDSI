produto1 = int(input("Informe o preço do primeiro produto: "))
produto2 = int(input("Informe o preço do segundo produto: "))
produto3 = int(input("Informe o preço do terceiro produto: "))


valorTotal = produto1 + produto2 + produto3
desconto = valorTotal * 0.2
valorDescontado = valorTotal - (valorTotal * 0.2)

print("\nO total das compras foi de {} + {} + {} = {}".format(produto1, produto2, produto3, valorTotal,"\n"))
print("O desconto será de :", desconto,)
print("O cliente deverá pagar: ", valorDescontado,"\n")