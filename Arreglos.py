import random
import time

Alumnos = 500
Materias = 6


random.seed(0)

calificaciones_list = [
    [random.randint(0, 100) for _ in range(Materias)]
    for _ in range(Alumnos)
]

nombres_materias = [f"Materia {i+1}" for i in range(Materias)]


def buscar_calificacion_list(matriz, alumno, materia):
    return matriz[alumno - 1][materia - 1]


inicio = time.time()
calificacion_list = buscar_calificacion_list(calificaciones_list, 321, 5)
fin = time.time()


print("Tabla completa de calificaciones:\n")
print(f"{'Alumno':<8} " + " ".join([f"{nombre:<10}" for nombre in nombres_materias]))
print("-" * (8 + 11 * Materias))

print(f"\nCalificación (lista) del alumno 321 en la materia 5: {calificacion_list}")
print(f"Tiempo de ejecución (lista): {fin - inicio:.10f} segundos\n")

for i, fila in enumerate(calificaciones_list, start=1):
    print(f"{i:<8} " + " ".join([f"{nota:<10}" for nota in fila]))

