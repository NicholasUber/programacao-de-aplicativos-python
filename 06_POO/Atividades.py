# 1. Cachorro


class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade


    def latir(self):
        print(f"{self.nome} diz: Au au!")


    def mostrar_info(self):
        print(f"Nome: {self.nome}, Raça: {self.raca}, Idade: {self.idade} anos")




cachorro1 = Cachorro("Thor", "Yorkshire", 3)
cachorro2 = Cachorro("Tom", "Pastor Alemao", 5)


cachorro1.latir()
cachorro1.mostrar_info()




cachorro2.latir()
cachorro2.mostrar_info()


cachorro1.idade = 4
cachorro1.mostrar_info()

#2 Livro

class Livro:
    def __init__(self, titulo, autor, total_paginas):
        self.titulo = titulo
        self.autor = autor
        self.total_paginas = total_paginas
        self.paginasLidas =0

    def ler(self, paginas):
        self.paginasLidas += paginas
        if self.paginasLidas > self.total_paginas:
            self.paginasLidas = self.total_paginas

    def porcentagem_Lida(self):
        return (self.paginasLidas / self.total_paginas) * 100

    def paginas_restantes(self):
        return self.total_paginas - self.paginasLidas

    def terminou(self):
        return self.paginasLidas >= self.total_paginas

livro1=Livro("Dom Casmurro", "Machado de Assis", 256)
livro1.ler(256)
print(livro1.porcentagem_Lida())
print(livro1.paginas_restantes())
print(livro1.terminou())

livro2=Livro("O Pequeno Principe", "Augusto Jordan", 128)
livro2.ler(64)
print(livro2.porcentagem_Lida())
print(livro2.paginas_restantes())
print(livro2.terminou())

#3 Conta Bancaria

class Conta_Bancaria:
    def __init__(self,titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saldo: {self.saldo}")
        else :
            print("Saldo insuficiente")

    def extrato(self):
        print(self.titular)
        print(self.saldo)
Conta_Bancaria1 = Conta_Bancaria("Joao")
Conta_Bancaria2 = Conta_Bancaria("Maria", 500)

Conta_Bancaria1.depositar(100)
Conta_Bancaria1.depositar(50)
Conta_Bancaria1.depositar(25)
Conta_Bancaria1.extrato()

Conta_Bancaria2.depositar(200)
Conta_Bancaria2.depositar(100)
Conta_Bancaria2.depositar(50)
Conta_Bancaria2.extrato()

#4 Personagem de Videogame

class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.vida=100
        self.nivel=1

    def receber_Dano(self,valor):
        self.vida=max(0,self.vida-valor)
        if self.vida == 0:
            print(f"{self.nome}foi derrotado!")

    def curar(self, valor):
        self.vida=min(100,self.vida+valor)

    def subir_nivel(self,valor):
        self.nivel+=1
        self.vida+=100

    def status(self):
        print(f"Nome: {self.nome}")
        print(f"Classe: {self.classe}")
        print(f"Vida: {self.vida}")
        print(f"Nivel: {self.nivel}")

personagem1 = Personagem("Pedro", "Nobre")
personagem2 = Personagem("Charles", "Camponês")

personagem1.receber_Dano(50)
personagem2.curar(40)
personagem2.receber_Dano(30)
personagem2.curar(20)

personagem1.status()
personagem2.status()


#5 Lista de Compras

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self):
        return self.preco * self.quantidade


class Carrinho:
    def __init__(self):
        self.itens = []  # Usando lista [] para permitir .append()

    def adicionar(self, produto):
        self.itens.append(produto)

    def total(self):
        return sum(produto.subtotal() for produto in self.itens)

    def mostrar(self):
        print("\nLISTA DE COMPRAS")
        for produto in self.itens:
            print(f"{produto.nome} - {produto.quantidade} unidades - Subtotal: R$ {produto.subtotal():.2f}")

        # Impresso fora do loop for
        print(f"Total da compra: R$ {self.total():.2f}")


# Teste do código
produto1 = Produto("Arroz", 25.00, 2)
produto2 = Produto("Feijão", 8.00, 3)
produto3 = Produto("Leite", 5.50, 4)
produto4 = Produto("Pão", 10.00, 1)

carrinho = Carrinho()
carrinho.adicionar(produto1)
carrinho.adicionar(produto2)
carrinho.adicionar(produto3)
carrinho.adicionar(produto4)

carrinho.mostrar()
