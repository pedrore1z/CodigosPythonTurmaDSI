vPermitida = float(input("Qual a velocidade permitida? "))
vMotorista = float(input("Qual a velocidade do motorista? "))

# calcular 20% à mais
vPermitida20 = (vPermitida * 0.2) + vPermitida

# calcular 50% à mais
vPermitida50 = (vPermitida * 0.5) + vPermitida

if vMotorista <= vPermitida:
    print("Tudo certo, não precisa pagar multa")
elif vMotorista > vPermitida and vMotorista <= vPermitida20:
    print("Você cometeu uma infração média! \nAssim irá pagar R$85,00 e receber 4 pontos na carteira")
elif vMotorista > vPermitida20 and vMotorista <= vPermitida50:
    print("Você cometeu uma infração grave! \nAssim irá pagar R$127,00 e receber 5 pontos na carteira")
elif vMotorista > vPermitida50:
    print("Você cometeu uma infração gravíssima! \nAssim irá pagar R$574,00 além de receber 7 pontos na carteira \n ter carteira apreendida e\n Ter o direito de dirigir suspenso.")           