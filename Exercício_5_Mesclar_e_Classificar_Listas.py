
lista1 = list(map(int, input("Insira a primeira lista de números \n inteiros separados por espaços: ").split()))
lista2 = list(map(int, input("Insira a segunda lista de números \n inteiros separados por espaços: ").split()))

lista_mesclada = lista1 + lista2

lista_mesclada.sort()

print("Lista classificada: ", lista_mesclada)

