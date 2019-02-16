# Trabalhando com uma lista no tamanho 10
# Ou seja, um vetor vazio com 10 posições
list = [""]*10

# Trabalando com listas sem identificar tamanho
lista = []

# Adicionar um elemento na lista
# O vetor nao tem um tipo definido, vc pode ter valores inteiro como strings em posicoes diferentes de um mesmo vetor
lista.append(5)
lista.append(4)
lista.append(2)
lista.append(8)
lista.append(2)

# Manipulando valores da lista
lista[0] = 2

# Obtendo o tamanho da lista
t = len(lista)

# Exibindo uma lista
print("Resultado da lista: ", lista)

i = 0
while i < t:
    print("Na posição", i, "tem o valor", lista[i])
    i+=1

while i < t:
    print("Na posição {} tem o valor {}".format(i, lista[i]))
    i+=1

print("-----------------------")

# Usando for na maneira foreach
for x in lista:
    print(x)

print("-----------------------")

# Usando for normal
# O range serve para criar um alcance baseado em um numero. Nada mais é do que comecar a contar de 0 a n-1
for x in range(len(lista)):
    print(x)

# Criando uma funcao em python
def dobro():
    print("Teste")

def dobro(a,b,c):
    print("Teste 2")

def dobro(a,b):
    return a+b

# Usando função com dois retornos
def dobroComRetornoDuplo(a,b):
    return a,b

a, b = dobroComRetornoDuplo(10,15)
