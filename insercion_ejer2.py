def ordenamiento_insercion_nombres(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > key:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

nombres = ["Carlos", "Ana", "Luis", "Beatriz", "Diego"]
print("Ordenado con Inserción:", ordenamiento_insercion_nombres(nombres))
