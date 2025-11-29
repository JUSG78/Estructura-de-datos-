import tkinter as tk
from tkinter import messagebox

class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ordenamiento Paso a Paso (Automático)")
        self.root.geometry("820x600")

        # Variables
        self.arr = []
        self.step = 0
        self.sorting_method = None
        self.generator = None
        self.autoplay = False
        self.after_id = None

        # Widgets - selección de método
        top_frame = tk.Frame(root)
        top_frame.pack(pady=8, fill=tk.X)

        label = tk.Label(top_frame, text="Selecciona un método de ordenamiento:")
        label.pack(anchor="w", padx=10)

        self.method_var = tk.StringVar(value="bubble")
        radios_frame = tk.Frame(top_frame)
        radios_frame.pack(anchor="w", padx=10, pady=4)
        self.bubble_radio = tk.Radiobutton(radios_frame, text="Bubble Sort", variable=self.method_var, value="bubble")
        self.bubble_radio.grid(row=0, column=0, padx=6)
        self.insertion_radio = tk.Radiobutton(radios_frame, text="Insertion Sort", variable=self.method_var, value="insertion")
        self.insertion_radio.grid(row=0, column=1, padx=6)
        self.selection_radio = tk.Radiobutton(radios_frame, text="Selection Sort", variable=self.method_var, value="selection")
        self.selection_radio.grid(row=0, column=2, padx=6)

        # Entrada de números
        entry_frame = tk.Frame(root)
        entry_frame.pack(pady=6, fill=tk.X, padx=10)
        self.input_label = tk.Label(entry_frame, text="Ingresa los números separados por comas (ej: 64,34,25,12):")
        self.input_label.pack(anchor="w")
        self.input_entry = tk.Entry(entry_frame, width=80)
        self.input_entry.pack(anchor="w")

        # Controles (iniciar, play, paso, limpiar)
        controls_frame = tk.Frame(root)
        controls_frame.pack(pady=10)

        self.start_button = tk.Button(controls_frame, text="Iniciar Ordenamiento", command=self.start_sorting)
        self.start_button.grid(row=0, column=0, padx=6)

        self.play_button = tk.Button(controls_frame, text="Play", command=self.toggle_play, state=tk.DISABLED)
        self.play_button.grid(row=0, column=1, padx=6)

        self.step_button = tk.Button(controls_frame, text="Siguiente Paso", command=self.next_step, state=tk.DISABLED)
        self.step_button.grid(row=0, column=2, padx=6)

        self.clear_button = tk.Button(controls_frame, text="Limpiar Historial", command=self.clear_history, state=tk.DISABLED)
        self.clear_button.grid(row=0, column=3, padx=6)

        # Velocidad
        speed_frame = tk.Frame(root)
        speed_frame.pack(pady=6, padx=10, anchor="w")
        tk.Label(speed_frame, text="Velocidad (ms por paso):").pack(side=tk.LEFT)
        self.speed_scale = tk.Scale(speed_frame, from_=50, to=2000, orient=tk.HORIZONTAL)
        self.speed_scale.set(400)
        self.speed_scale.pack(side=tk.LEFT)

        # Mostrar lista actual y operación
        display_frame = tk.Frame(root)
        display_frame.pack(pady=6, padx=10, fill=tk.X)
        self.list_label = tk.Label(display_frame, text="Lista actual: []", font=(None, 12))
        self.list_label.pack(anchor="w")
        self.op_label = tk.Label(display_frame, text="Operación: -")
        self.op_label.pack(anchor="w")
        self.status_label = tk.Label(display_frame, text="")
        self.status_label.pack(anchor="w")

        # Historial (gran cuadro, no editable) - cada paso en una línea: "<lista> | <desc>"
        hist_frame = tk.Frame(root)
        hist_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)

        # Text widget grande
        self.history = tk.Text(hist_frame, height=20, width=110, wrap=tk.NONE, font=("Consolas", 11))
        self.history.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Scrollbars
        v_scroll = tk.Scrollbar(hist_frame, orient=tk.VERTICAL, command=self.history.yview)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        h_scroll = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=self.history.xview)
        h_scroll.pack(fill=tk.X, padx=10)
        self.history.config(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

        # Encabezado inicial
        self.history.config(state=tk.NORMAL)
        self.history.insert(tk.END, "Historial de pasos (cada línea muestra la lista completa y la operación):\n")
        self.history.config(state=tk.DISABLED)

    def start_sorting(self):
        try:
            arr_input = self.input_entry.get()
            if not arr_input.strip():
                messagebox.showerror("Error", "Ingresa al menos un número.")
                return
            # Parsear enteros, ignorar entradas vacías
            self.arr = [int(x.strip()) for x in arr_input.split(',') if x.strip() != '']
            if len(self.arr) == 0:
                messagebox.showerror("Error", "Ingresa al menos un número válido.")
                return
            self.sorting_method = self.method_var.get()
            self.step = 0
            self.list_label.config(text=f"Lista original: {self.arr}")
            self.status_label.config(text="Preparado. Puedes presionar 'Play' o 'Siguiente Paso'.")
            self.play_button.config(state=tk.NORMAL, text="Play")
            self.step_button.config(state=tk.NORMAL)
            self.clear_button.config(state=tk.NORMAL)
            self.op_label.config(text="Operación: -")

            # Crear generador que devuelve (arr_copy, descripcion)
            if self.sorting_method == "bubble":
                self.generator = self.bubble_sort_generator(self.arr.copy())
            elif self.sorting_method == "insertion":
                self.generator = self.insertion_sort_generator(self.arr.copy())
            elif self.sorting_method == "selection":
                self.generator = self.selection_sort_generator(self.arr.copy())

            # Si estaba en autoplay, pararlo para reiniciar desde el nuevo generador
            if self.autoplay:
                self.toggle_play()
        except ValueError:
            messagebox.showerror("Error", "Ingresa solo números separados por comas.")

    def toggle_play(self):
        if not self.autoplay:
            # iniciar autoplay
            self.autoplay = True
            self.play_button.config(text="Pause")
            self.step_button.config(state=tk.DISABLED)
            self.status_label.config(text="Autoplay: activado")
            self._schedule_next()
        else:
            # pausar autoplay
            self.autoplay = False
            self.play_button.config(text="Play")
            self.step_button.config(state=tk.NORMAL)
            self.status_label.config(text="Autoplay: pausado")
            if self.after_id is not None:
                try:
                    self.root.after_cancel(self.after_id)
                except Exception:
                    pass
                self.after_id = None

    def _schedule_next(self):
        delay = int(self.speed_scale.get())
        self.after_id = self.root.after(delay, self._autoplay_step)

    def _autoplay_step(self):
        if not self.autoplay:
            return
        finished = self.next_step()
        if finished:
            self.autoplay = False
            self.play_button.config(text="Play")
            self.step_button.config(state=tk.DISABLED)
            self.status_label.config(text="Ordenamiento completado (autoplay).")
            return
        self._schedule_next()

    def clear_history(self):
        # limpia el historial dejando el encabezado
        self.history.config(state=tk.NORMAL)
        self.history.delete(1.0, tk.END)
        self.history.insert(tk.END, "Historial de pasos (cada línea muestra la lista completa y la operación):\n")
        self.history.config(state=tk.DISABLED)
        self.clear_button.config(state=tk.DISABLED)

    def next_step(self):
        # Returns True if finished, False otherwise
        try:
            # Esperamos que el generador devuelva (arr, desc)
            result, desc = next(self.generator)
            # Actualizar etiquetas visibles
            self.list_label.config(text=f"Paso {self.step + 1}: {result}")
            self.op_label.config(text=f"Operación: {desc}")

            # Crear representación en una línea: "0,18,5,... | Descripción"
            try:
                if isinstance(result, (list, tuple)):
                    result_str = ",".join(str(x) for x in result)
                else:
                    result_str = str(result)
                entry = f"{result_str}  |  {desc}\n"
                self.history.config(state=tk.NORMAL)
                self.history.insert(tk.END, entry)
                self.history.see(tk.END)
                self.history.config(state=tk.DISABLED)
                self.clear_button.config(state=tk.NORMAL)
            except Exception:
                pass

            self.step += 1
            self.status_label.config(text=f"Avanzando al paso {self.step + 1}...")
            return False

        except StopIteration:
            # Generador terminó
            self.status_label.config(text="¡Ordenamiento completado!")
            self.op_label.config(text="Operación: -")
            self.step_button.config(state=tk.DISABLED)
            self.play_button.config(state=tk.DISABLED)
            return True
        except TypeError:
            messagebox.showerror("Error", "No hay un ordenamiento en progreso. Presiona 'Iniciar Ordenamiento'.")
            return True

    # Generadores que devuelven (arr_copy, descripcion)
    def bubble_sort_generator(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                desc = f"Comparando arr[{j}]={arr[j]} y arr[{j+1}]={arr[j+1]}"
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    desc = f"Intercambio: arr[{j}] <-> arr[{j+1}]"
                # devolvemos copia del arreglo y descripción
                yield arr.copy(), desc
        yield arr.copy(), "Finalizado"

    def insertion_sort_generator(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            desc = f"Insertando key={key} en la sublista ordenada"
            yield arr.copy(), desc
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                desc = f"Desplazando arr[{j}] -> posición {j+1}"
                yield arr.copy(), desc
                j -= 1
            arr[j + 1] = key
            desc = f"Insertado key={key} en posición {j+1}"
            yield arr.copy(), desc
        yield arr.copy(), "Finalizado"

    def selection_sort_generator(self, arr):
        for i in range(len(arr)):
            min_idx = i
            desc = f"Buscando mínimo desde i={i}"
            yield arr.copy(), desc
            for j in range(i + 1, len(arr)):
                desc = f"Comparando arr[{j}]={arr[j]} con arr[{min_idx}]={arr[min_idx]}"
                if arr[j] < arr[min_idx]:
                    min_idx = j
                    desc = f"Nuevo mínimo en idx={min_idx} (valor {arr[min_idx]})"
                yield arr.copy(), desc
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                desc = f"Intercambio: arr[{i}] <-> arr[{min_idx}]"
            else:
                desc = f"Posición {i} ya es mínima"
            yield arr.copy(), desc
        yield arr.copy(), "Finalizado"


if __name__ == "__main__":
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()
