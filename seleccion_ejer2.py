def ordenamiento_seleccion_nombres(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

nombres = ["Carlos", "Ana", "Luis", "Beatriz", "Diego"]
print("Ordenado con Selección:", ordenamiento_seleccion_nombres(nombres))
