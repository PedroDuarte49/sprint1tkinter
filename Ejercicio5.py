import tkinter as tk

def cambiar_color():
    root.config(bg=color.get())

root = tk.Tk()
root.title("Ejercicio 5 - Radiobutton")

color = tk.StringVar(value="white")

tk.Label(root, text="Elige tu color favorito:").pack(pady=5)

tk.Radiobutton(root, text="Rojo", variable=color, value="red", command=cambiar_color).pack(anchor="w")
tk.Radiobutton(root, text="Verde", variable=color, value="green", command=cambiar_color).pack(anchor="w")
tk.Radiobutton(root, text="Azul", variable=color, value="blue", command=cambiar_color).pack(anchor="w")

root.mainloop()
