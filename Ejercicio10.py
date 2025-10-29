import tkinter as tk

root = tk.Tk()
root.title("Ejemplo de Scrollbar")
root.geometry("400x300")

frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

texto = tk.Text(frame, wrap="word")
texto.grid(row=0, column=0, sticky="nsew")

scroll_vert = tk.Scrollbar(frame, orient="vertical", command=texto.yview)
scroll_vert.grid(row=0, column=1, sticky="ns")
texto.config(yscrollcommand=scroll_vert.set)

texto.insert("1.0", (
    "Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto "
    "Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto\n\n "
    "Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto "
    "Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto \n\n"
    "Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto "
    "Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto\n\n "
    "Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto "
    "Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto\n\n "
    "Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto "
    "Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto\n\n "
    "Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto "
    "Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto Texto de texto\n\n "
))

root.mainloop()
