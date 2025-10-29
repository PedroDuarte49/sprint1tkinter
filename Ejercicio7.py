import tkinter as tk

def dibujar():
    try:
        x1 = int(entry_x1.get())
        y1 = int(entry_y1.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())
        canvas.delete("all")  # Limpiar antes de dibujar
        canvas.create_rectangle(x1, y1, x2, y2, outline="blue", width=2)
        canvas.create_oval(x1, y1, x2, y2, outline="red", width=2)
    except ValueError:
        etiqueta_resultado.config(text="Introduce solo números válidos")

root = tk.Tk()
root.title("Ejercicio 7 - Canvas")

tk.Label(root, text="x1:").grid(row=0, column=0)
entry_x1 = tk.Entry(root, width=5)
entry_x1.grid(row=0, column=1)

tk.Label(root, text="y1:").grid(row=0, column=2)
entry_y1 = tk.Entry(root, width=5)
entry_y1.grid(row=0, column=3)

tk.Label(root, text="x2:").grid(row=1, column=0)
entry_x2 = tk.Entry(root, width=5)
entry_x2.grid(row=1, column=1)

tk.Label(root, text="y2:").grid(row=1, column=2)
entry_y2 = tk.Entry(root, width=5)
entry_y2.grid(row=1, column=3)

tk.Button(root, text="Dibujar", command=dibujar).grid(row=2, column=0, columnspan=4, pady=5)

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.grid(row=3, column=0, columnspan=4, pady=10)

etiqueta_resultado = tk.Label(root, text="")
etiqueta_resultado.grid(row=4, column=0, columnspan=4)

root.mainloop()
