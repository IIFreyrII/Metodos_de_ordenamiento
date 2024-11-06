def ordenamiento_burbuja_nombres(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

nombres = ["Carlos", "Ana", "Luis", "Beatriz", "Diego"]
print("Ordenado con Burbuja:", ordenamiento_burbuja_nombres(nombres))
