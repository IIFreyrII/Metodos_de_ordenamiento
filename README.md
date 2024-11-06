# Metodos_de_ordenamiento

Ejercicio 1: Ordenar una lista de precios de productos en una tienda en línea
Explicación
Supongamos que tienes una lista de precios de diferentes productos en una tienda en línea y quieres ordenarlos en orden ascendente. Utilizarás tres métodos de ordenamiento distintos para comparar su eficiencia.

Ejercicio 2: Ordenar nombres de estudiantes en un aula
Explicación
Este ejercicio consiste en ordenar una lista de nombres de estudiantes en orden alfabético, lo que puede ser útil al organizar listas de asistencia o asignar asientos en un aula.

Los métodos de ordenamiento utilizados (Burbuja, Inserción y Selección) son algoritmos simples y directos con una complejidad de O(n^2), lo que significa que el número de comparaciones crece cuadráticamente conforme aumenta el tamaño de la lista. Esto se debe a que cada elemento debe ser comparado y, en muchos casos, intercambiado o insertado, lo cual se vuelve costoso a medida que hay más elementos.

Burbuja: Este método es ineficiente porque necesita múltiples pasadas para colocar cada elemento en su lugar, incluso si una gran parte de la lista ya está ordenada. Esto implica hacer intercambios innecesarios, que incrementan el número de operaciones.

Inserción: Aunque es más eficiente en listas parcialmente ordenadas (ya que minimiza desplazamientos), la necesidad de insertar cada elemento en la posición correcta mediante comparaciones sucesivas lo hace menos práctico en listas grandes, donde la búsqueda de la posición adecuada y el desplazamiento de elementos se vuelven lentos.

Selección: Este método es menos eficiente porque busca el valor mínimo de toda la lista en cada iteración, incluso cuando no es necesario en listas que ya están parcialmente ordenadas. Esto incrementa el número de comparaciones, sin optimización alguna para listas parcialmente organizadas.

Por estas razones, en listas extensas, los algoritmos 𝑂(𝑛 log 𝑛), como MergeSort o QuickSort, que dividen las comparaciones, son más adecuados al reducir significativamente el número de operaciones necesarias para ordenar la lista completa.
