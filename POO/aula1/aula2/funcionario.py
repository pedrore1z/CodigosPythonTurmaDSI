class Funcionario:
    def __init__(self,nome,cargo,salario = 1100):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    
    def relatorio(self):
        print(f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: {self.salario}")

