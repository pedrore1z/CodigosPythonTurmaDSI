from datetime import date

anoAtual = date.today().year
while True:
    nascimento = int(input("Informe o seu ano do seu nascimento: "))

    idade = anoAtual - nascimento

    if idade >= 18:
        print(f"Você possui {idade} anos, prossiga com a inscrição\n")
        break
    else:
        print(f"Você possui {idade} anos, você ainda não pode se inscrever\n")