class Ventas:
    def __init__(self):
        self.departamentos = ["Ropa", "Deportes", "Juguetería"]
        self.meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                      "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        self.ventas = [[0 for _ in range(len(self.meses))] for _ in range(len(self.departamentos))]

    def registrar_venta(self, departamento, mes, monto):
        dep_index = self._buscar_departamento(departamento)
        mes_index = self._buscar_mes(mes)
        if dep_index != -1 and mes_index != -1:
            self.ventas[dep_index][mes_index] = monto
            print(f"Venta registrada: {departamento} en {mes} = {monto}")
        else:
            print("Departamento o mes no válido.")

    def buscar_venta(self, departamento, mes):
        dep_index = self._buscar_departamento(departamento)
        mes_index = self._buscar_mes(mes)
        if dep_index != -1 and mes_index != -1:
            valor = self.ventas[dep_index][mes_index]
            print(f"Venta encontrada: {valor} en {departamento} - {mes}")
            return valor
        else:
            print("Departamento o mes no válido.")
            return None

    def eliminar_venta(self, departamento, mes):
        dep_index = self._buscar_departamento(departamento)
        mes_index = self._buscar_mes(mes)
        if dep_index != -1 and mes_index != -1:
            self.ventas[dep_index][mes_index] = 0
            print(f"Venta eliminada: {departamento} en {mes}")
        else:
            print("Departamento o mes no válido.")

    def mostrar_ventas(self):
        print("\nVentas mensuales por departamento:")
        print(f"{'Mes':<12}{self.departamentos[0]:<12}{self.departamentos[1]:<12}{self.departamentos[2]:<12}")
        for mes_index, mes in enumerate(self.meses):
            fila = "".join(f"{self.ventas[dep_index][mes_index]:<12}" for dep_index in range(len(self.departamentos)))
            print(f"{mes:<12}{fila}")

    def _buscar_departamento(self, departamento):
        try:
            return self.departamentos.index(departamento)
        except ValueError:
            return -1

    def _buscar_mes(self, mes):
        try:
            return self.meses.index(mes)
        except ValueError:
            return -1


def main():
    ventas = Ventas()

    while True:
        print("\nMenú de Ventas")
        print("1. Registrar venta")
        print("2. Buscar venta")
        print("3. Eliminar venta")
        print("4. Mostrar todas las ventas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            depto = input("Ingrese el departamento (Ropa, Deportes, Juguetería): ")
            mes = input("Ingrese el mes (Enero, Febrero, ..., Diciembre): ")
            try:
                monto = float(input("Ingrese el monto de la venta: "))
                if monto < 0:
                    print("El monto debe ser un número positivo.")
                    continue
            except ValueError:
                print("Monto inválido. Debe ser un número.")
                continue
            ventas.registrar_venta(depto, mes, monto)

        elif opcion == '2':
            depto = input("Ingrese el departamento (Ropa, Deportes, Juguetería): ")
            mes = input("Ingrese el mes (Enero, Febrero, ..., Diciembre): ")
            ventas.buscar_venta(depto, mes)

        elif opcion == '3':
            depto = input("Ingrese el departamento (Ropa, Deportes, Juguetería): ")
            mes = input("Ingrese el mes (Enero, Febrero, ..., Diciembre): ")
            ventas.eliminar_venta(depto, mes)

        elif opcion == '4':
            ventas.mostrar_ventas()

        elif opcion == '5':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
