import tkinter as tk
from tkinter import messagebox

def abrir():
    messagebox.showinfo("Abrir", "Función Abrir (aún no implementada)")

def salir():
    root.quit()

def acerca_de():
    messagebox.showinfo("Acerca de", "Programa de ejemplo con menús.")

root = tk.Tk()
root.title("Ejercicio 9 - Menú")

menu_barra = tk.Menu(root)

# Menú Archivo
menu_archivo = tk.Menu(menu_barra, tearoff=0)
menu_archivo.add_command(label="Abrir", command=abrir)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)
menu_barra.add_cascade(label="Archivo", menu=menu_archivo)

# Menú Ayuda
menu_ayuda = tk.Menu(menu_barra, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)
menu_barra.add_cascade(label="Ayuda", menu=menu_ayuda)

root.config(menu=menu_barra)
root.mainloop()
