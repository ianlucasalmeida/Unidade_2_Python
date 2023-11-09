'''numeros = []

for i in range(5):
    numeros.append(int(input()))

soma = 0
##acessa os valores armazenados na lista pelo índice
for i in range(5):
    soma = soma + numeros[i]
print(soma)

soma = 0
##acessa os valores aramzenados na lista diretamente
for e in numeros:
    soma = soma + e
print(soma)

media = soma/5
print(media)'''

def calcular_media(numeros):
    return sum(numeros) / len(numeros)

# Lista de números inteiros
numeros = [1, 2, 3, 4, 5]

# Calcular a média
media = calcular_media(numeros)

print("A média é", media)
