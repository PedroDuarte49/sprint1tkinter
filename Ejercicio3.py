import tkinter as tk

def saludar():
    nombre = entrada.get()
    etiqueta_saludo.config(text=f"¡Hola, {nombre}!")

root = tk.Tk()
root.title("Ejercicio 3 - Entry")

etiqueta = tk.Label(root, text="Escribe tu nombre:")
etiqueta.pack(pady=5)

entrada = tk.Entry(root)
entrada.pack(pady=5)

boton = tk.Button(root, text="Saludar", command=saludar)
boton.pack(pady=5)

etiqueta_saludo = tk.Label(root, text="")
etiqueta_saludo.pack(pady=5)

root.mainloop()
