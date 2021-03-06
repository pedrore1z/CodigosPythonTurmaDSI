#Trabalhando com Herança simples.
class Pessoa:#Superclasse
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__

    def mostraClasse(self):
        print(f"{self.nomeClasse} = Seu nome é {self.nome}")

class Aluno(Pessoa):#Subclasse
    def __init__(self,nome,idade,matricula):
        Pessoa.__init__(self,nome,idade)
        self.matricula = matricula

    def mostraAluno(self):
        print(f"{self.nomeClasse}= sou estudante e meu nome é {self.nome}")


class Professor(Pessoa):
    def mostraProfessor(self):
        print(f"{self.nomeClasse} = sou professor e meu nome é {self.nome}")