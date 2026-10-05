#Oque é uma função

#Uma função é um bloco de código criado para realizar uma tarefa
#Ela permite organizar e reutilizar o código

#1 Criando uma função
#Utilizar a palavra def para uma função

def saudacao():
    print("olá, seja bem-vindo")
    #Para executar a saudação chamamos seu nome

saudacao()

    #2 Funcao com parametro
def saudacao(nome):
    print(f"Olá, {nome}")

saudacao("Ana")
saudacao("Carlos")

#3 Mais de um parametro
def apresentar(nome, idade):
    print(f"nome: {nome}")
    print(f" idade: {idade}")

apresentar("Ana",18)

#Função com cálculo

def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"resultado: {resultado}")

somar(10,20)

#Retornando um valor
#O return devolve um valor para o local onde a função foi chamada

def somar(numero1, numero2):
    return numero1 + numero2
resultado = somar(10,20)
print(resultado)

#Funcao com condicao
def verificarIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

#7 Parametro de um valor padrao
#Podemos definir com um valor padrao para um parametro
def saudacao(nome="Aluno"):
    print(f"Ola, {nome}")
saudacao()
saudacao("Joao")

#8 Varios parametros
def calcularMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

print(calcularMedia(8,7,9))

#9 Funcões para organizar um programa
def cadastraProduto():
    nome = input("Digite o nome do produto: ")
    preco= float(input("Digite o preco: "))
    return nome , preco

def exibirProduto():
    print("\n ===== Produto ===== ")
    print(f"nome {nome}")
    print(f"Preço: R${preco}")

nome, preco = cadastraProduto()
exibirProduto(nome, preco)
