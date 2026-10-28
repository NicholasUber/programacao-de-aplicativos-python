class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    def apresentar(self):
        print(f"Sou {self.nome} e ganho {self.salario:.2f}")

    def dar_aumento(self, porcentagem):
        if porcentagem <= 0:
            print(f"Aumento inválido para {self.nome}")
            return
        self.__salario = self.__salario * (1 + porcentagem / 100)
        print(f"{self.nome} recebeu {porcentagem}% de aumento")


class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor

    def apresentar(self):
        print(f"Sou {self.nome}, gerente de {self.setor} e ganho {self.salario:.2f}")


# --- Execução e Testes ---

ana = Funcionario("Ana", 3000)
ana.apresentar()
ana.dar_aumento(10)
ana.apresentar()

try:
    ana.salario = 10000
except AttributeError:
    print("Não é permitido alterar o salário diretamente.")

try:
    print(ana.__salario)
except AttributeError:
    print("O atributo __salario não pode ser acessado de fora.")

print("-" * 30)

carlos = Gerente("Carlos", 7000, "TI")
carlos.apresentar()
carlos.dar_aumento(15)
carlos.apresentar()

#2. Herança
class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario) #Super() chama construtor da classe
        self.equipe= equipe #Atributo novo

    def mostrar_equipe(self):
        print(f"{self.nome} gerencia {self.equipe} pessoas ")

class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)#Super() chama construtora
        self.curso = curso #Atributo novo

fulano = Gerente("Fulano", 8000, 5)
caio = Estagiario("Caio", 1500 , "Analise de sistema" )

fulano.apresentar()
caio.apresentar()
caio.dar_aumento(5)
caio.apresentar()