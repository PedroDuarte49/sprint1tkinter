import tkinter as tk

def actualizar_valor(val):
    etiqueta_valor.config(text=f"Valor: {val}")

root = tk.Tk()
root.title("Ejercicio 11 - Scale")
root.geometry("300x150")

tk.Label(root, text="Selecciona un número (0-100):").pack(pady=8)

scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar_valor)
scale.pack(fill="x", padx=20)

etiqueta_valor = tk.Label(root, text="Valor: 0")
etiqueta_valor.pack(pady=10)

root.mainloop()
