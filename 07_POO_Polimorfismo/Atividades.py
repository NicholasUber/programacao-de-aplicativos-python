class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = 0
        self.definir_nota(nota)

    @property
    def nota(self):
        return self.__nota

    def definir_nota(self, valor):
        if 0 <= valor <= 10:
            self.__nota = valor
        else:
            print("Nota inválida!")

    def situacao(self):
        if self.__nota >= 7:
            return "Aprovado"
        return "Reprovado"


aluno1 = Aluno("Marina", 6.5)
print(aluno1.situacao())

aluno1.definir_nota(15)
aluno1.definir_nota(8)
print(aluno1.nota)
print(aluno1.situacao())

aluno2 = Aluno("Carlos", 4.0)
print(aluno2.situacao())

try:
    aluno2.nota = 10
except AttributeError:
    print("Erro: Não é permitido alterar a nota diretamente!")

#2 Cofre com senha

class Cofre:
    def __init__(self, senha, nota):
        self.__senha = senha
        self.__lista


    def