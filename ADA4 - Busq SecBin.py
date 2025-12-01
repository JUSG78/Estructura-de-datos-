import tkinter as tk
from tkinter import filedialog, scrolledtext
import hashlib
import os

def calcular_hashes_carpeta():
    carpeta = filedialog.askdirectory(title="Selecciona una carpeta")
    if not carpeta:
        return
    
    resultados = []

    # os.walk permite recorrer TODAS las subcarpetas
    for ruta_actual, subcarpetas, archivos in os.walk(carpeta):
        for archivo in archivos:
            ruta_completa = os.path.join(ruta_actual, archivo)
            if os.path.isfile(ruta_completa):
                with open(ruta_completa, "rb") as f:
                    contenido = f.read()
                    hash_sha256 = hashlib.sha256(contenido).hexdigest()

                # Mostrar ruta relativa para entender de dónde viene cada archivo
                ruta_relativa = os.path.relpath(ruta_completa, carpeta)
                resultados.append(f"{ruta_relativa}: {hash_sha256}")

    # Mostrar en pantalla
    texto_resultados.delete(1.0, tk.END)
    texto_resultados.insert(tk.END, "\n".join(resultados))


# Ventana principal
root = tk.Tk()
root.title("Cálculo de Hash SHA-256 (Incluye Subcarpetas)")

# Botón para seleccionar carpeta
btn = tk.Button(root, text="Seleccionar Carpeta", command=calcular_hashes_carpeta)
btn.pack(pady=10)

# Caja donde se muestran los hashes
texto_resultados = scrolledtext.ScrolledText(root, width=90, height=30)
texto_resultados.pack(padx=10, pady=10)

root.mainloop()
