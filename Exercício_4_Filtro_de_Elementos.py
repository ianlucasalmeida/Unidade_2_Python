def filtrar_pares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    return pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = filtrar_pares(numeros)

print(pares)
