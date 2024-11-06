def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

precios = [19.99, 5.99, 29.99, 15.99, 10.99]
print("Ordenado con Burbuja:", ordenamiento_burbuja(precios))
