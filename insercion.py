def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > key:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

precios = [19.99, 5.99, 29.99, 15.99, 10.99]
print("Ordenado con Inserción:", ordenamiento_insercion(precios))
