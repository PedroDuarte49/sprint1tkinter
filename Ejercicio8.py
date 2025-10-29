import tkinter as tk

def mostrar_texto():
    texto = entrada.get()
    etiqueta_resultado.config(text=f"Has escrito: {texto}")

def borrar_texto():
    entrada.delete(0, tk.END)
    etiqueta_resultado.config(text="")

root = tk.Tk()
root.title("Ejercicio 8 - Frame")

# Frame superior
frame_superior = tk.Frame(root)
frame_superior.pack(pady=10)

tk.Label(frame_superior, text="Nombre:").grid(row=0, column=0, padx=5)
entrada = tk.Entry(frame_superior)
entrada.grid(row=0, column=1, padx=5)
etiqueta_resultado = tk.Label(frame_superior, text="")
etiqueta_resultado.grid(row=1, column=0, columnspan=2, pady=5)

# Frame inferior
frame_inferior = tk.Frame(root)
frame_inferior.pack(pady=10)

tk.Button(frame_inferior, text="Mostrar", command=mostrar_texto).grid(row=0, column=0, padx=5)
tk.Button(frame_inferior, text="Borrar", command=borrar_texto).grid(row=0, column=1, padx=5)

root.mainloop()
