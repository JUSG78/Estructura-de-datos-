import java.util.Scanner;


public class Ventas {
    private String[] departamentos = {"Ropa", "Deportes", "Juguetería"};
    private String[] meses = {"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                              "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"};
    private double[][] ventas;

    public Ventas() {
        ventas = new double[departamentos.length][meses.length];
    }

 
    public void registrarVenta(String departamento, String mes, double monto) {
        int depIndex = buscarDepartamento(departamento);
        int mesIndex = buscarMes(mes);
        if (depIndex != -1 && mesIndex != -1) {
            ventas[depIndex][mesIndex] = monto;
            System.out.println("Venta registrada: " + departamento + " en " + mes + " = " + monto);
        } else {
            System.out.println("Departamento o mes no válido.");
        }
    }

    
    public void buscarVenta(String departamento, String mes) {
        int depIndex = buscarDepartamento(departamento);
        int mesIndex = buscarMes(mes);
        if (depIndex != -1 && mesIndex != -1) {
            double valor = ventas[depIndex][mesIndex];
            System.out.println("Venta encontrada: " + valor + " en " + departamento + " - " + mes);
        } else {
            System.out.println("Departamento o mes no válido.");
        }
    }

   
    public void eliminarVenta(String departamento, String mes) {
        int depIndex = buscarDepartamento(departamento);
        int mesIndex = buscarMes(mes);
        if (depIndex != -1 && mesIndex != -1) {
            ventas[depIndex][mesIndex] = 0;
            System.out.println("Venta eliminada: " + departamento + " en " + mes);
        } else {
            System.out.println("Departamento o mes no válido.");
        }
    }

    public void mostrarVentas() {
        System.out.printf("%-12s", "Mes");
        for (String depto : departamentos) {
            System.out.printf("%-12s", depto);
        }
        System.out.println();

        for (int m = 0; m < meses.length; m++) {
            System.out.printf("%-12s", meses[m]);
            for (int d = 0; d < departamentos.length; d++) {
                System.out.printf("%-12.2f", ventas[d][m]);
            }
            System.out.println();
        }
    }


    private int buscarDepartamento(String departamento) {
        for (int i = 0; i < departamentos.length; i++) {
            if (departamentos[i].equalsIgnoreCase(departamento)) {
                return i;
            }
        }
        return -1;
    }

    private int buscarMes(String mes) {
        for (int i = 0; i < meses.length; i++) {
            if (meses[i].equalsIgnoreCase(mes)) {
                return i;
            }
        }
        return -1;
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Ventas ventas = new Ventas();

        while (true) {
            System.out.println("\nMenú de Ventas");
            System.out.println("1. Registrar venta");
            System.out.println("2. Buscar venta");
            System.out.println("3. Eliminar venta");
            System.out.println("4. Mostrar todas las ventas");
            System.out.println("5. Salir");
            System.out.print("Seleccione una opción: ");
            String opcion = sc.nextLine();

            switch (opcion) {
                case "1":
                    System.out.print("Ingrese el departamento (Ropa, Deportes, Juguetería): ");
                    String depto = sc.nextLine();
                    System.out.print("Ingrese el mes (Enero, Febrero, ..., Diciembre): ");
                    String mes = sc.nextLine();
                    try {
                        System.out.print("Ingrese el monto de la venta: ");
                        double monto = Double.parseDouble(sc.nextLine());
                        if (monto < 0) {
                            System.out.println("El monto debe ser un número positivo.");
                        } else {
                            ventas.registrarVenta(depto, mes, monto);
                        }
                    } catch (NumberFormatException e) {
                        System.out.println("Monto inválido. Debe ser un número.");
                    }
                    break;

                case "2":
                    System.out.print("Ingrese el departamento: ");
                    depto = sc.nextLine();
                    System.out.print("Ingrese el mes: ");
                    mes = sc.nextLine();
                    ventas.buscarVenta(depto, mes);
                    break;

                case "3":
                    System.out.print("Ingrese el departamento: ");
                    depto = sc.nextLine();
                    System.out.print("Ingrese el mes: ");
                    mes = sc.nextLine();
                    ventas.eliminarVenta(depto, mes);
                    break;

                case "4":
                    ventas.mostrarVentas();
                    break;

                case "5":
                    System.out.println("Saliendo del programa.");
                    sc.close();
                    return;

                default:
                    System.out.println("Opción no válida. Intente de nuevo.");
            }
        }
    }
}
