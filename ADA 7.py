import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.image as mpimg
import networkx as nx

# ==== Estados y posiciones aproximadas (coordenadas normalizadas 0–1, refinadas con coordenadas geográficas) ====
posiciones = {
    "Aguascalientes": (0.500, 0.421),      # Centro aproximado: Aguascalientes
    "Baja California": (0.094, 0.842),      # Centro aproximado: Tijuana
    "Baja California Sur": (0.219, 0.579), # Centro aproximado: La Paz
    "Campeche": (0.859, 0.263),            # Centro aproximado: Campeche
    "Chiapas": (0.797, 0.105),             # Centro aproximado: Tuxtla Gutiérrez
    "Chihuahua": (0.375, 0.737),           # Centro aproximado: Chihuahua
    "CDMX": (0.591, 0.284),                # Centro aproximado: Ciudad de México
    "Coahuila": (0.500, 0.684),            # Centro aproximado: Saltillo
    "Colima": (0.453, 0.263),              # Centro aproximado: Colima
    "Durango": (0.438, 0.526),             # Centro aproximado: Durango
    "Guanajuato": (0.531, 0.368),          # Centro aproximado: Guanajuato
    "Guerrero": (0.578, 0.184),            # Centro aproximado: Chilpancingo
    "Hidalgo": (0.594, 0.342),             # Centro aproximado: Pachuca
    "Jalisco": (0.438, 0.316),             # Centro aproximado: Guadalajara
    "México": (0.572, 0.279),              # Centro aproximado: Toluca
    "Michoacán": (0.500, 0.263),           # Centro aproximado: Morelia
    "Morelos": (0.587, 0.247),             # Centro aproximado: Cuernavaca
    "Nayarit": (0.406, 0.421),             # Centro aproximado: Tepic
    "Nuevo León": (0.563, 0.632),          # Centro aproximado: Monterrey
    "Oaxaca": (0.672, 0.158),              # Centro aproximado: Oaxaca
    "Puebla": (0.625, 0.263),              # Centro aproximado: Puebla
    "Querétaro": (0.563, 0.368),           # Centro aproximado: Querétaro
    "Quintana Roo": (0.938, 0.289),        # Centro aproximado: Chetumal
    "San Luis Potosí": (0.563, 0.421),     # Centro aproximado: San Luis Potosí
    "Sinaloa": (0.344, 0.579),             # Centro aproximado: Culiacán
    "Sonora": (0.250, 0.789),              # Centro aproximado: Hermosillo
    "Tabasco": (0.797, 0.211),             # Centro aproximado: Villahermosa
    "Tamaulipas": (0.625, 0.526),          # Centro aproximado: Ciudad Victoria
    "Tlaxcala": (0.619, 0.279),            # Centro aproximado: Tlaxcala
    "Veracruz": (0.672, 0.289),            # Centro aproximado: Xalapa
    "Yucatán": (0.906, 0.342),             # Centro aproximado: Mérida
    "Zacatecas": (0.500, 0.474),           # Centro aproximado: Zacatecas
}

ESTADOS = sorted(posiciones.keys())  # Orden alfabético

# Abreviaturas para los estados (usando abreviaturas comunes de 2-4 letras)
abreviaturas = {
    "Aguascalientes": "Ags",
    "Baja California": "BC",
    "Baja California Sur": "BCS",
    "Campeche": "Camp",
    "Chiapas": "Chis",
    "Chihuahua": "Chih",
    "CDMX": "CDMX",
    "Coahuila": "Coah",
    "Colima": "Col",
    "Durango": "Dgo",
    "Guanajuato": "Gto",
    "Guerrero": "Gro",
    "Hidalgo": "Hgo",
    "Jalisco": "Jal",
    "México": "Mex",
    "Michoacán": "Mich",
    "Morelos": "Mor",
    "Nayarit": "Nay",
    "Nuevo León": "NL",
    "Oaxaca": "Oax",
    "Puebla": "Pue",
    "Querétaro": "Qro",
    "Quintana Roo": "QR",
    "San Luis Potosí": "SLP",
    "Sinaloa": "Sin",
    "Sonora": "Son",
    "Tabasco": "Tab",
    "Tamaulipas": "Tamps",
    "Tlaxcala": "Tlax",
    "Veracruz": "Ver",
    "Yucatán": "Yuc",
    "Zacatecas": "Zac",
}


# ==== Clase principal ====
class GrafoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grafo de Estados de México con Mapa")
        self.root.geometry("1100x750")

        self.G = nx.Graph()
        self.aristas = []  # Lista para rastrear aristas: [(origen, destino, costo), ...]

        # Frame principal
        frame = ttk.Frame(root, padding=10)
        frame.pack(fill="both", expand=True)

        # --- Panel izquierdo: controles ---
        control_frame = ttk.Frame(frame)
        control_frame.pack(side="left", fill="y", padx=10, pady=10)

        ttk.Label(control_frame, text="Agregar conexión", font=("Arial", 12, "bold")).pack(pady=5)

        ttk.Label(control_frame, text="Origen:").pack()
        self.origen_cb = ttk.Combobox(control_frame, values=ESTADOS, state="readonly", width=25)
        self.origen_cb.pack(pady=2)

        ttk.Label(control_frame, text="Destino:").pack()
        self.destino_cb = ttk.Combobox(control_frame, values=ESTADOS, state="readonly", width=25)
        self.destino_cb.pack(pady=2)

        ttk.Label(control_frame, text="Costo:").pack()
        self.costo_entry = ttk.Entry(control_frame, width=10)
        self.costo_entry.pack(pady=2)

        ttk.Button(control_frame, text="Agregar Arista", command=self.agregar_arista).pack(pady=10)

        ttk.Label(control_frame, text="Aristas agregadas:", font=("Arial", 11, "bold")).pack(pady=5)
        self.lista = tk.Listbox(control_frame, width=35, height=15)
        self.lista.pack(pady=5)

        ttk.Button(control_frame, text="Eliminar Arista", command=self.eliminar_arista).pack(pady=5)

        ttk.Label(control_frame, text="Eliminar Vértice:", font=("Arial", 11, "bold")).pack(pady=5)
        self.vertice_cb = ttk.Combobox(control_frame, values=ESTADOS, state="readonly", width=25)
        self.vertice_cb.pack(pady=2)
        ttk.Button(control_frame, text="Eliminar Vértice", command=self.eliminar_vertice).pack(pady=5)

        ttk.Button(control_frame, text="Limpiar Grafo", command=self.limpiar_grafo).pack(pady=10)

        # --- Panel derecho: gráfico ---
        self.fig, self.ax = plt.subplots(figsize=(7, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.get_tk_widget().pack(side="right", fill="both", expand=True)

        try:
            self.img = mpimg.imread("mapa_mexico.png")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar 'mapa_mexico.png'\n{e}")
            self.img = None

        self.dibujar_grafo()

    # ==== Métodos principales ====
    def agregar_arista(self):
        origen = self.origen_cb.get()
        destino = self.destino_cb.get()
        costo = self.costo_entry.get()

        if not origen or not destino or not costo:
            messagebox.showwarning("Campos incompletos", "Selecciona origen, destino y costo.")
            return
        if origen == destino:
            messagebox.showwarning("Error", "Un estado no puede conectarse consigo mismo.")
            return

        try:
            costo = float(costo)
        except ValueError:
            messagebox.showerror("Error", "El costo debe ser numérico.")
            return

        # Verificar si la arista ya existe
        if self.G.has_edge(origen, destino):
            messagebox.showwarning("Arista duplicada", "Esta conexión ya existe.")
            return

        self.G.add_edge(origen, destino, weight=costo)
        self.aristas.append((origen, destino, costo))
        self.lista.insert("end", f"{abreviaturas[origen]} ↔ {abreviaturas[destino]}  ({costo} km)")
        self.costo_entry.delete(0, tk.END)
        self.dibujar_grafo()

    def eliminar_arista(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showwarning("Selección requerida", "Selecciona una arista de la lista para eliminar.")
            return

        indice = seleccion[0]
        texto = self.lista.get(indice)
        # Parsear el texto: "abreviatura_origen ↔ abreviatura_destino  (costo km)"
        try:
            partes = texto.split(" ↔ ")
            abreviatura_origen = partes[0]
            resto = partes[1].split("  (")
            abreviatura_destino = resto[0]
            costo_str = resto[1].rstrip(" km)")
            costo = float(costo_str)
        except (IndexError, ValueError):
            messagebox.showerror("Error", "No se pudo parsear la arista seleccionada.")
            return

        # Encontrar el origen y destino reales usando las abreviaturas
        origen = next((k for k, v in abreviaturas.items() if v == abreviatura_origen), None)
        destino = next((k for k, v in abreviaturas.items() if v == abreviatura_destino), None)
        if not origen or not destino:
            messagebox.showerror("Error", "No se encontraron los estados correspondientes.")
            return

        # Verificar y eliminar del grafo
        if self.G.has_edge(origen, destino) and self.G[origen][destino]['weight'] == costo:
            self.G.remove_edge(origen, destino)
            self.aristas.remove((origen, destino, costo))
            self.lista.delete(indice)
            self.dibujar_grafo()
        else:
            messagebox.showerror("Error", "La arista no coincide con el grafo actual.")

    def eliminar_vertice(self):
        estado = self.vertice_cb.get()
        if not estado:
            messagebox.showwarning("Selección requerida", "Selecciona un vértice para eliminar.")
            return

        if estado not in self.G.nodes:
            messagebox.showwarning("Vértice no encontrado", "El vértice no existe en el grafo.")
            return

        # Remover todas las aristas que involucren este vértice
        aristas_a_remover = [arista for arista in self.aristas if estado in arista[:2]]
        for arista in aristas_a_remover:
            self.aristas.remove(arista)
            # Remover de la lista visual
            for i in range(self.lista.size()):
                texto = self.lista.get(i)
                if f"{abreviaturas[arista[0]]} ↔ {abreviaturas[arista[1]]}" in texto:
                    self.lista.delete(i)
                    break

        self.G.remove_node(estado)
        self.dibujar_grafo()

    def limpiar_grafo(self):
        self.G.clear()
        self.aristas.clear()
        self.lista.delete(0, "end")
        self.dibujar_grafo()

    def dibujar_grafo(self):
        self.ax.clear()
        if self.img is not None:
            self.ax.imshow(self.img, extent=[0, 1, 0, 1])

        self.ax.set_title("Mapa de México - Grafo de Estados", fontsize=14)
        self.ax.axis("off")

        if len(self.G.nodes) > 0:
            nx.draw(
                self.G,
                pos=posiciones,
                ax=self.ax,
                with_labels=False,  # Quitar las etiquetas (abreviaturas)
                nodelist=self.G.nodes,  # Dibujar solo los nodos que están en el grafo
                node_color="lightblue",
                node_size=300,  # Tamaño reducido de los puntos
                font_size=8,
                font_weight="bold",
                edge_color="darkblue",
            )

            labels = nx.get_edge_attributes(self.G, "weight")
            nx.draw_networkx_edge_labels(self.G, posiciones, edge_labels=labels, font_size=7)

        self.canvas.draw()


# ==== Ejecutar aplicación ====
if __name__ == "__main__":
    root = tk.Tk()
    app = GrafoApp(root)
    root.mainloop()
