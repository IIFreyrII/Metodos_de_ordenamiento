def ordenamiento_seleccion(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

precios = [19.99, 5.99, 29.99, 15.99, 10.99]
print("Ordenado con Selección:", ordenamiento_seleccion(precios))
