calificaciones = [0] * 5

for i in range(5):
    while True:
        calificacion = int(input(f"Ingresa la calificación {i+1} (0-10): "))
        if 0 <= calificacion <= 10:
            calificaciones[i] = calificacion
            break
        else:
            print("La calificación debe estar entre 0 y 10.")

for i, calificacion in enumerate(calificaciones):
    print(f"Calificación {i+1} = {calificacion}")

