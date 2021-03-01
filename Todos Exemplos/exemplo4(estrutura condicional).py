nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media > 7:
    print("Você passou, parabéns")
elif media == 7 :
    print("Passou arrastado . Estude mais !")
else:
    print("Você reprovou!!!! Se prepara pro chiclete")         
