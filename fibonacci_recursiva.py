def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Número de términos que quieres imprimir
terminos = 10

# Imprimir la serie
print(f"Serie de Fibonacci recursiva con {terminos} términos:")
for i in range(terminos):
    print(fibonacci_recursivo(i), end=" ")
