import tkinter as tk

def actualizar():
    seleccionadas = []
    if leer.get():
        seleccionadas.append("Leer")
    if deporte.get():
        seleccionadas.append("Deporte")
    if musica.get():
        seleccionadas.append("Música")

    etiqueta.config(text="Aficiones: " + ", ".join(seleccionadas) if seleccionadas else "Sin aficiones seleccionadas")

root = tk.Tk()
root.title("Ejercicio 4 - Checkbutton")

leer = tk.IntVar()
deporte = tk.IntVar()
musica = tk.IntVar()

tk.Checkbutton(root, text="Leer", variable=leer, command=actualizar).pack(anchor="w")
tk.Checkbutton(root, text="Deporte", variable=deporte, command=actualizar).pack(anchor="w")
tk.Checkbutton(root, text="Música", variable=musica, command=actualizar).pack(anchor="w")

etiqueta = tk.Label(root, text="Sin aficiones seleccionadas")
etiqueta.pack(pady=10)

root.mainloop()
