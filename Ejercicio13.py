import tkinter as tk

def dibujar_circulo(event):
    x, y = event.x, event.y
    r = 20
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="blue")

def limpiar(event):
    if event.char == "c":
        canvas.delete("all")

root = tk.Tk()
root.title("Eventos de teclado y ratón")
root.geometry("400x400")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

# Eventos
canvas.bind("<Button-1>", dibujar_circulo)
root.bind("<Key>", limpiar)

root.mainloop()
