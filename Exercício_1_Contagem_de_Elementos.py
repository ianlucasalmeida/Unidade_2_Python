def conta_repeticao(lista, elemento):
    contagem = 0

    for item in lista:
        if item == elemento:
            contagem += 1

    return contagem

lista = [1, 2, 3, 1, 4, 1, 5]

elemento_procurado = 1

repeticoes = conta_repeticao(lista, elemento_procurado)

print(f"O elemento {elemento_procurado} aparece {repeticoes} vezes na lista.")