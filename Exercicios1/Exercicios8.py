km = float(input("Quantos km o carro faz com 1 litro? "))
restante = float(input("Quantos litros de combustível há no momento? "))
distancia = float(input("Qual a distância que deseja percorrer? "))

if distancia / km < restante:
    print("Pode ir tranquilo que da pra chegar no destino! ")
else:
    print("Você vai precisar abastecer {:.2f} litros \n\n".format(distancia / km - restante))