#1 Encapsulamento
#Proteger o salário para que ele so mude seguindo regras

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario #Privado:Dois sublinhados

    def apresentar(self):
        print(f"Sou {self.nome} e ganho {self.__salario}")

    @property
    def salario(self):
        return self.__salario

    def dar_aumento(self, porcentagem):
        if porcentagem <= 0:
            print(f"Aumento invalido para {self.nome}")
            return
        self.__salario = self.salario * (1+porcentagem/100)
        print(f"{self.nome} recebeu {porcentagem}% de aumento")


# o Try/except é um bloco usado em programação para tratar um erro

try:
    ana.salario = 10000
except AttributeError:
    print("Não é possivel alterar um produto o salario diretamente")

ana = Funcionario('Ana', 3000)
ana.apresentar()




