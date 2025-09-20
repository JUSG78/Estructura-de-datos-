# Programa de Ventas - Python y Java

Este proyecto implementa un sistema para registrar, buscar, eliminar y mostrar ventas mensuales de tres departamentos: **Ropa, Deportes y Juguetería**.  
Se desarrolla en **Python** y en **Java**, utilizando un **arreglo bidimensional** para almacenar los datos.

---

## Funcionalidad del Programa

1. **Registrar Venta**  
   Inserta un monto de venta en el departamento y mes indicados.  
   - Python: `registrar_venta(departamento, mes, monto)`  
   - Java: `registrarVenta(String departamento, String mes, double monto)`  

2. **Buscar Venta**  
   Permite consultar la venta registrada de un departamento en un mes específico.  
   - Python: `buscar_venta(departamento, mes)`  
   - Java: `buscarVenta(String departamento, String mes)`  

3. **Eliminar Venta**  
   Establece el valor de una venta en `0` para un departamento y mes determinados.  
   - Python: `eliminar_venta(departamento, mes)`  
   - Java: `eliminarVenta(String departamento, String mes)`  

4. **Mostrar Ventas**  
   Despliega en formato tabular todas las ventas mensuales por departamento.  

---

## Cómo funciona
- Se utiliza un **arreglo bidimensional** donde cada fila representa un departamento y cada columna un mes.  
- Ejemplo en Python:  
  ```python
  self.ventas = [[0 for _ in range(len(self.meses))] for _ in range(len(self.departamentos))]
