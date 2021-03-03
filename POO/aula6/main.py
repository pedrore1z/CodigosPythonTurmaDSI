from heranca import Pessoa, Aluno, Professor

#Instanciando objeto

p1 = Pessoa("Joaquim", 56)
a1 = Aluno("Patricia", 23)
prof1 = Professor("Tertuliano", 48)

print(f"\nPessoa: {p1.nome}")
print(f"\nAluno: {a1.nome}")
print(f"\nProfessor: {prof1.nome}\n")

p1.mostraClasse()

a1.mostraAluno()

prof1.mostraProfessor()