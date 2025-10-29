import tkinter as tk

def mostrar_fruta():
    seleccion = lista.curselection()
    if seleccion:
        fruta = lista.get(seleccion)
        etiqueta.config(text=f"Fruta seleccionada: {fruta}")
    else:
        etiqueta.config(text="No has seleccionado ninguna fruta")

root = tk.Tk()
root.title("Ejercicio 6 - Listbox")

tk.Label(root, text="Selecciona una fruta:").pack(pady=5)

lista = tk.Listbox(root)
for fruta in ["Manzana", "Banana", "Naranja"]:
    lista.insert(tk.END, fruta)
lista.pack()

tk.Button(root, text="Mostrar selección", command=mostrar_fruta).pack(pady=5)

etiqueta = tk.Label(root, text="")
etiqueta.pack(pady=5)

root.mainloop()
