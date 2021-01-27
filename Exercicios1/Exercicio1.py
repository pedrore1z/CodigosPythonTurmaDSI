medida = float(input("Informe a base do seu terreno: "))
medida2 = float(input("Informe a altura do seu terreno: "))

print("\n\nPara cada m² o valor da construção será de R$850\n\n")
area = medida * medida2
print("Sua area é: ", area)

metros = 850

print("Você deverá pagar o valor de :", area * metros)