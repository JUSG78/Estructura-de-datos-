import tkinter as tk
from tkinter import messagebox

# =====================================
#           CLASE NODO
# =====================================
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

# =====================================
#           CLASE ÁRBOL BINARIO
# =====================================
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def esVacio(self):
        return self.raiz is None

    # [1] Insertar elemento
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar(nodo.der, valor)

    # [2] Mostrar árbol acostado
    def mostrar_acostado(self):
        if self.raiz is None:
            return "Árbol vacío"
        return self._mostrar_acostado(self.raiz, 0)

    def _mostrar_acostado(self, nodo, nivel):
        if nodo is None:
            return ""
        result = self._mostrar_acostado(nodo.der, nivel + 1)
        result += "   " * nivel + str(nodo.valor) + "\n"
        result += self._mostrar_acostado(nodo.izq, nivel + 1)
        return result

    # [4] Buscar elemento
    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar(nodo.izq, valor)
        else:
            return self._buscar(nodo.der, valor)

    # [5] PreOrden
    def preorden(self):
        return self._preorden(self.raiz)

    def _preorden(self, nodo):
        if nodo is None:
            return []
        return [nodo.valor] + self._preorden(nodo.izq) + self._preorden(nodo.der)

    # [6] InOrden
    def inorden(self):
        return self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo is None:
            return []
        return self._inorden(nodo.izq) + [nodo.valor] + self._inorden(nodo.der)

    # [7] PostOrden
    def postorden(self):
        return self._postorden(self.raiz)

    def _postorden(self, nodo):
        if nodo is None:
            return []
        return self._postorden(nodo.izq) + self._postorden(nodo.der) + [nodo.valor]

    # [8] Eliminar nodo por PREDECESOR
    def eliminar_predecesor(self, valor):
        self.raiz, eliminado = self._eliminar_predecesor(self.raiz, valor)
        return eliminado

    def _eliminar_predecesor(self, nodo, valor):
        if nodo is None:
            return nodo, False
        if valor < nodo.valor:
            nodo.izq, eliminado = self._eliminar_predecesor(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der, eliminado = self._eliminar_predecesor(nodo.der, valor)
        else:
            if nodo.izq and nodo.der:
                predecesor = self._maximo(nodo.izq)
                nodo.valor = predecesor.valor
                nodo.izq, _ = self._eliminar_predecesor(nodo.izq, predecesor.valor)
                eliminado = True
            elif nodo.izq:
                nodo = nodo.izq
                eliminado = True
            elif nodo.der:
                nodo = nodo.der
                eliminado = True
            else:
                nodo = None
                eliminado = True
        return nodo, eliminado

    # [9] Eliminar nodo por SUCESOR
    def eliminar_sucesor(self, valor):
        self.raiz, eliminado = self._eliminar_sucesor(self.raiz, valor)
        return eliminado

    def _eliminar_sucesor(self, nodo, valor):
        if nodo is None:
            return nodo, False
        if valor < nodo.valor:
            nodo.izq, eliminado = self._eliminar_sucesor(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der, eliminado = self._eliminar_sucesor(nodo.der, valor)
        else:
            if nodo.izq and nodo.der:
                sucesor = self._minimo(nodo.der)
                nodo.valor = sucesor.valor
                nodo.der, _ = self._eliminar_sucesor(nodo.der, sucesor.valor)
                eliminado = True
            elif nodo.izq:
                nodo = nodo.izq
                eliminado = True
            elif nodo.der:
                nodo = nodo.der
                eliminado = True
            else:
                nodo = None
                eliminado = True
        return nodo, eliminado

    def _minimo(self, nodo):
        while nodo.izq:
            nodo = nodo.izq
        return nodo

    def _maximo(self, nodo):
        while nodo.der:
            nodo = nodo.der
        return nodo

    # [10] Recorrido por niveles (Amplitud)
    def por_niveles(self):
        if self.raiz is None:
            return []
        cola = [self.raiz]
        resultado = []
        while cola:
            actual = cola.pop(0)
            resultado.append(actual.valor)
            if actual.izq:
                cola.append(actual.izq)
            if actual.der:
                cola.append(actual.der)
        return resultado

    # [11] Altura
    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura(nodo.izq), self._altura(nodo.der))

    # [12] Cantidad de hojas
    def cantidad_hojas(self):
        return self._hojas(self.raiz)

    def _hojas(self, nodo):
        if nodo is None:
            return 0
        if nodo.izq is None and nodo.der is None:
            return 1
        return self._hojas(nodo.izq) + self._hojas(nodo.der)

    # [13] Cantidad de nodos
    def cantidad_nodos(self):
        return self._nodos(self.raiz)

    def _nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._nodos(nodo.izq) + self._nodos(nodo.der)

    # [15] Árbol completo
    def es_completo(self):
        if self.raiz is None:
            return False
        cola = [self.raiz]
        vacio = False
        while cola:
            actual = cola.pop(0)
            if actual is None:
                vacio = True
            else:
                if vacio:
                    return False
                cola.append(actual.izq)
                cola.append(actual.der)
        return True

    # [16] Árbol lleno
    def es_lleno(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return True
        if nodo.izq is None and nodo.der is None:
            return True
        if nodo.izq and nodo.der:
            return self.es_lleno(nodo.izq) and self.es_lleno(nodo.der)
        return False

    # [17] Eliminar todo el árbol
    def eliminar_arbol(self):
        self.raiz = None

    # [3] Graficar árbol
    def graficar(self, canvas, x, y, dx, dy, nodo):
        if nodo is None:
            return
        color = "#AED581" if nodo == self.raiz else "#FFF176"
        canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=color, outline="black")
        canvas.create_text(x, y, text=str(nodo.valor), font=("Arial", 11, "bold"))
        if nodo.izq:
            canvas.create_line(x, y, x - dx, y + dy, arrow=tk.LAST)
            self.graficar(canvas, x - dx, y + dy, dx / 2, dy, nodo.izq)
        if nodo.der:
            canvas.create_line(x, y, x + dx, y + dy, arrow=tk.LAST)
            self.graficar(canvas, x + dx, y + dy, dx / 2, dy, nodo.der)

# =====================================
#          INTERFAZ VISUAL
# =====================================
class Interfaz:
    def __init__(self, root):
        self.arbol = ArbolBinario()
        self.root = root
        self.root.title("🌳 Árbol Binario Completo con 17 Métodos")
        self.root.geometry("1300x850")
        self.root.configure(bg="#f4f4f4")

        tk.Label(root, text="🌿 Árbol Binario Interactivo 🌿", font=("Arial", 22, "bold"), bg="#f4f4f4").pack(pady=10)

        # Frame del Canvas
        frame_canvas = tk.Frame(root, bg="#f4f4f4")
        frame_canvas.pack(fill="both", expand=True, pady=10)
        self.canvas = tk.Canvas(frame_canvas, bg="#E3F2FD")
        self.canvas.pack(fill="both", expand=True)
        self.scroll_x = tk.Scrollbar(frame_canvas, orient="horizontal", command=self.canvas.xview)
        self.scroll_y = tk.Scrollbar(frame_canvas, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side="bottom", fill="x")
        self.scroll_y.pack(side="right", fill="y")

        # Entrada
        frame_entry = tk.Frame(root, bg="#f4f4f4")
        frame_entry.pack(pady=5)
        tk.Label(frame_entry, text="Valor:", bg="#f4f4f4").grid(row=0, column=0)
        self.entry = tk.Entry(frame_entry, width=10)
        self.entry.grid(row=0, column=1)
        self.entry.bind("<Return>", lambda e: self.insertar())
        tk.Button(frame_entry, text="Insertar", bg="#4CAF50", fg="white", command=self.insertar).grid(row=0, column=2, padx=5)

        # Botones
        botones = [
            ("Mostrar Acostado", self.mostrar_acostado),
            ("Graficar Árbol", self.graficar),
            ("Buscar", self.buscar),
            ("PreOrden", self.preorden),
            ("InOrden", self.inorden),
            ("PostOrden", self.postorden),
            ("Eliminar Predecesor", self.eliminar_predecesor),
            ("Eliminar Sucesor", self.eliminar_sucesor),
            ("Por Niveles", self.por_niveles),
            ("Altura", self.altura),
            ("Hojas", self.hojas),
            ("Nodos", self.nodos),
            ("Es Completo", self.es_completo),
            ("Es Lleno", self.es_lleno),
            ("Eliminar Árbol", self.eliminar_arbol)
        ]
        frame_botones = tk.Frame(root, bg="#f4f4f4")
        frame_botones.pack(pady=10)
        for i, (texto, cmd) in enumerate(botones):
            tk.Button(frame_botones, text=texto, width=18, height=2, bg="#64B5F6", fg="white",
                      command=cmd).grid(row=i // 5, column=i % 5, padx=8, pady=8)

    # ====== FUNCIONES DE INTERFAZ ======
    def insertar(self):
        try:
            v = int(self.entry.get())
            self.arbol.insertar(v)
            self.graficar()
            self.entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido")

    def mostrar_acostado(self):
        messagebox.showinfo("Árbol", self.arbol.mostrar_acostado())

    def buscar(self):
        try:
            v = int(self.entry.get())
            ok = self.arbol.buscar(v)
            messagebox.showinfo("Buscar", f"{'Encontrado ✅' if ok else 'No encontrado ❌'}")
        except:
            messagebox.showerror("Error", "Valor inválido")

    def preorden(self): messagebox.showinfo("PreOrden", self.arbol.preorden())
    def inorden(self): messagebox.showinfo("InOrden", self.arbol.inorden())
    def postorden(self): messagebox.showinfo("PostOrden", self.arbol.postorden())
    def por_niveles(self): messagebox.showinfo("Por niveles", self.arbol.por_niveles())
    def altura(self): messagebox.showinfo("Altura", self.arbol.altura())
    def hojas(self): messagebox.showinfo("Hojas", self.arbol.cantidad_hojas())
    def nodos(self): messagebox.showinfo("Nodos", self.arbol.cantidad_nodos())
    def es_completo(self): messagebox.showinfo("Completo", self.arbol.es_completo())
    def es_lleno(self): messagebox.showinfo("Lleno", self.arbol.es_lleno())
    def eliminar_predecesor(self):
        try:
            v = int(self.entry.get())
            ok = self.arbol.eliminar_predecesor(v)
            if ok:
                self.graficar()
                messagebox.showinfo("Éxito", "Eliminado (predecesor)")
            else:
                messagebox.showinfo("Info", "No encontrado")
        except:
            messagebox.showerror("Error", "Valor inválido")
    def eliminar_sucesor(self):
        try:
            v = int(self.entry.get())
            ok = self.arbol.eliminar_sucesor(v)
            if ok:
                self.graficar()
                messagebox.showinfo("Éxito", "Eliminado (sucesor)")
            else:
                messagebox.showinfo("Info", "No encontrado")
        except:
            messagebox.showerror("Error", "Valor inválido")
    def eliminar_arbol(self):
        self.arbol.eliminar_arbol()
        self.canvas.delete("all")
        messagebox.showinfo("Listo", "Árbol eliminado")
    def graficar(self):
        self.canvas.delete("all")
        if not self.arbol.esVacio():
            self.arbol.graficar(self.canvas, 600, 50, 250, 100, self.arbol.raiz)
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

# =====================================
#           EJECUCIÓN
# =====================================
root = tk.Tk()
Interfaz(root)
root.mainloop()
