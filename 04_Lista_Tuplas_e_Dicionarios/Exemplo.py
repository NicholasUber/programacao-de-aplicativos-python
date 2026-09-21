#Listas, Tuplas e Dicionarios
from operator import index

#1 Listas

#Listas são utilizadas para armazenar vários valores
#Dentro de uma variável

nomes=["Ana" , "Carlos" , "João" , "Maria"]
print(nomes)

#2 Acessando elementos da Lista

print(nomes[0])
print(nomes[1])

#Podemos acessar o ultimo elemento usando -1
print(nomes[-1])

#3 Alterando elementos

#As listas são mutáveis, ou seja, os elementos podem ser alterados
nomes[0] = "Pedro"
print(nomes)

#4 Adicionando elementos no final da lista
nomes.append("Lucas")
print(nomes)

#Insert() adiciona um elemento em uma posição
nomes.insert(1, "Mariana")
print(nomes)

#Removendo Elementos
#remove() remove o elemento pelo seu valor
nomes.remove("Lucas")
print(nomes)

#pop() remove um elemento pelo indice
nomes.pop(0)
print(nomes)
