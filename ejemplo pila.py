import tkinter as tk
from tkinter import messagebox, font

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        return self.items

class Aplicacion:
    def __init__(self, master):
        self.master = master
        self.master.title("Pila Gráfica")
        self.master.geometry("400x400")
        self.master.configure(bg="#f0f0f0")

        self.pila = Pila()
        self.pila_visible = True  # Controla la visibilidad de la pila

        # Estilo de fuente
        self.custom_font = font.Font(family="Helvetica", size=12)

        # Widgets
        self.label = tk.Label(master, text="Elemento:", bg="#f0f0f0", font=self.custom_font)
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=self.custom_font, width=30)
        self.entry.pack(pady=5)

        # Frame para los botones
        self.button_frame = tk.Frame(master, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        # Botones
        button_color = "#ADD8E6"  # Azul claro
        self.apilar_button = tk.Button(self.button_frame, text="Apilar", command=self.apilar_elemento, bg=button_color, fg="black", font=self.custom_font)
        self.apilar_button.pack(side=tk.LEFT, padx=5)

        self.desapilar_button = tk.Button(self.button_frame, text="Desapilar", command=self.desapilar_elemento, bg=button_color, fg="black", font=self.custom_font)
        self.desapilar_button.pack(side=tk.LEFT, padx=5)

        self.cima_button = tk.Button(self.button_frame, text="Ver Cima", command=self.ver_cima, bg=button_color, fg="black", font=self.custom_font)
        self.cima_button.pack(side=tk.LEFT, padx=5)

        self.mostrar_button = tk.Button(self.button_frame, text="Mostrar Pila", command=self.mostrar_pila, bg=button_color, fg="black", font=self.custom_font)
        self.mostrar_button.pack(side=tk.LEFT, padx=5)

        self.toggle_button = tk.Button(self.button_frame, text="Ocultar/Mostrar Pila", command=self.toggle_pila, bg=button_color, fg="black", font=self.custom_font)
        self.toggle_button.pack(side=tk.LEFT, padx=5)

        self.result_label = tk.Label(master, text="", bg="#f0f0f0", font=self.custom_font)
        self.result_label.pack(pady=10)

        # Frame para la pila
        self.pila_frame = tk.Frame(master, bg="#D3E6F9", bd=2, relief=tk.RAISED)
        self.pila_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.pila_label = tk.Label(self.pila_frame, text="Pila: []", bg="#D3E6F9", font=self.custom_font)
        self.pila_label.pack(pady=10)

    def apilar_elemento(self):
        elemento = self.entry.get()
        if elemento:
            self.pila.apilar(elemento)
            self.result_label.config(text=f"✓ Apilado: {elemento}")
            self.entry.delete(0, tk.END)
            self.actualizar_pila_label()
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un elemento.")

    def desapilar_elemento(self):
        elemento = self.pila.desapilar()
        if elemento is not None:
            self.result_label.config(text=f"✗ Desapilado: {elemento}")
            self.actualizar_pila_label()
        else:
            self.result_label.config(text="La pila está vacía")

    def ver_cima(self):
        elemento = self.pila.cima()
        if elemento is not None:
            self.result_label.config(text=f"Elemento en cima: {elemento}")
        else:
            self.result_label.config(text="Pila vacía")

    def mostrar_pila(self):
        self.actualizar_pila_label()

    def actualizar_pila_label(self):
        elementos = self.pila.mostrar()
        pila_visual = "\n".join(reversed(elementos))  # Invertir el orden para mostrar la pila
        self.pila_label.config(text=f"Pila:\n{pila_visual}")

    def toggle_pila(self):
        self.pila_visible = not self.pila_visible  # Cambia el estado de visibilidad
        if self.pila_visible:
            self.pila_label.pack(pady=10)  # Muestra la pila
            self.toggle_button.config(text="Ocultar Pila")  # Cambia el texto del botón
        else:
            self.pila_label.pack_forget()  # Oculta la pila
            self.toggle_button.config(text="Mostrar Pila")  # Cambia el texto del botón

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
