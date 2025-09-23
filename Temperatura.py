def promedio(lista):
    return sum(lista) / len(lista)

def main():
    dias_de_semana = [
        "Lunes", "Martes", "Miércoles", "Jueves", 
        "Viernes", "Sábado", "Domingo"
    ]
    
    temperaturas = []

    print("Ingrese las temperaturas promedio de cada día de la semana en °C:")
    
    for dia in dias_de_semana:
    
        while True:
    
            try:
    
                temp = float(input(f"Temperatura del {dia}: "))
    
                if 0 <= temp <= 60:
                
                    temperaturas.append(temp)
                
                    break

                else:
                    print(" Temperatura fuera de rango (0 a 60 °C). Intente de nuevo.")
    
            except ValueError:
                print("Por favor, ingrese un número válido (ej: 25.5).")
  
    temp_promedio = promedio(temperaturas)
    print(f"\nTemperatura promedio semanal: {temp_promedio:.2f} °C")

    temp_max = max(temperaturas)
    print(f"Temperatura máxima de la semana: {temp_max:.2f} °C")
    
    temp_min = min(temperaturas)
    print(f"Temperatura mínima de la semana: {temp_min:.2f} °C")

    dias_sobre_promedio = sum(1 for t in temperaturas if t > temp_promedio)
    print(f"Días con temperatura superior al promedio: {dias_sobre_promedio}")


if __name__ == "__main__":
    main()
