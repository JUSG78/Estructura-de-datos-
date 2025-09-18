def fibonacci(n):
    a, b = 0, 1
    serie = []
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    return serie


terminos = 20


print(f"Serie de Fibonacci con {terminos} términos:")
print(fibonacci(terminos))
