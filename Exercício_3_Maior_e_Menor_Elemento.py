def encontra_maior_menor(lista):
    if not lista:
        return None, None  # Retorna None se a lista estiver vazia

    maior = menor = lista[0]

    for elemento in lista:
        if elemento > maior:
            maior = elemento
        elif elemento < menor:
            menor = elemento

    return maior, menor

# Exemplo de uso:
lista = [4, 2, 9, 1, 7]
maior, menor = encontra_maior_menor(lista)

print(f"O maior elemento é: {maior}")
print(f"O menor elemento é: {menor}")