import tkinter as tk
from tkinter import messagebox

class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Usuarios")
        self.root.geometry("400x400")

        # Nombre
        tk.Label(root, text="Nombre:").pack()
        self.nombre = tk.Entry(root)
        self.nombre.pack()

        # Edad
        tk.Label(root, text="Edad:").pack()
        self.edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
        self.edad.pack()

        # Género
        tk.Label(root, text="Género:").pack()
        self.genero = tk.StringVar(value="Otro")
        for g in ["Masculino", "Femenino"]:
            tk.Radiobutton(root, text=g, variable=self.genero, value=g).pack(anchor="w")

        # Lista de usuarios
        frame_lista = tk.Frame(root)
        frame_lista.pack(fill="both", expand=True)

        self.lista = tk.Listbox(frame_lista)
        self.lista.pack(side="left", fill="both", expand=True)

        scroll = tk.Scrollbar(frame_lista, command=self.lista.yview)
        scroll.pack(side="right", fill="y")
        self.lista.config(yscrollcommand=scroll.set)

        # Botones
        tk.Button(root, text="Añadir", command=self.añadir_usuario).pack(pady=2)
        tk.Button(root, text="Eliminar", command=self.eliminar_usuario).pack(pady=2)
        tk.Button(root, text="Salir", command=self.salir).pack(pady=2)

        # Menú
        menu = tk.Menu(root)
        root.config(menu=menu)
        archivo = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Archivo", menu=archivo)
        archivo.add_command(label="Guardar Lista", command=lambda: messagebox.showinfo("Guardar", "Lista guardada"))
        archivo.add_command(label="Cargar Lista", command=lambda: messagebox.showinfo("Cargar", "Lista cargada"))
        archivo.add_separator()
        archivo.add_command(label="Salir", command=self.salir)

    def añadir_usuario(self):
        nombre = self.nombre.get()
        edad = self.edad.get()
        genero = self.genero.get()
        if nombre:
            self.lista.insert(tk.END, f"{nombre} - {edad} años - {genero}")
            self.nombre.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Introduce un nombre")

    def eliminar_usuario(self):
        seleccionado = self.lista.curselection()
        if seleccionado:
            self.lista.delete(seleccionado)
        else:
            messagebox.showwarning("Aviso", "Selecciona un usuario")

    def salir(self):
        self.root.quit()

root = tk.Tk()
app = RegistroApp(root)
root.mainloop()
