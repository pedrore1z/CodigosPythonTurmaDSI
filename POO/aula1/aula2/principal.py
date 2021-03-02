from funcionario import Funcionario

colaborador = Funcionario("Pedro","Marketeiro",4000)
colaborador.relatorio()

colaborador2 = Funcionario("Alberto","Pedreiro")

print(f"O salário de {colaborador2.nome} é R$ {colaborador2.salario}")