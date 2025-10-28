import tkinter as tk

def cambiar_texto():
    etiqueta3.config(text="¡Texto cambiado!")

root = tk.Tk()
root.title("Ejercicio 1 - Labels")

etiqueta1 = tk.Label(root, text="¡Bienvenido a mi programa!")
etiqueta1.pack(pady=5)

etiqueta2 = tk.Label(root, text="Tu nombre completo: Pedro Duarte Neira García")
etiqueta2.pack(pady=5)

etiqueta3 = tk.Label(root, text="Texto original")
etiqueta3.pack(pady=5)

boton = tk.Button(root, text="Cambiar texto", command=cambiar_texto)
boton.pack(pady=5)

root.mainloop()
