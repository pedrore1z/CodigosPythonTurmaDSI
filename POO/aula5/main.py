from agregacao import Cliente, Conta

c1 = Cliente("Madruga", "98 91234-5678", "784.458.997-87", "Rua das Patativas 35, bairro ilhinha")


cc1 = Conta(1234,c1,1100,2000)

print(f"\n\nO cliente {cc1.titular.nome} possui um saldo de {cc1.saldo} e mora no endereço {cc1.titular.endereco} e possui telefone {cc1.titular.telefone} e um limite para compras de {cc1.limite}")