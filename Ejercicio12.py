import tkinter as tk
from tkinter import messagebox

class RegistroApp:
    def __init__(self, root):
        self.root = root
        root.title("Ejercicio 12 - Registro de Usuarios")
        root.geometry("520x360")


        menubar = tk.Menu(root)
        archivo = tk.Menu(menubar, tearoff=0)
        archivo.add_command(label="Guardar Lista", command=self.guardar_lista)
        archivo.add_command(label="Cargar Lista", command=self.cargar_lista)
        menubar.add_cascade(label="Archivo", menu=archivo)
        menubar.add_cascade(label="Salir", menu=tk.Menu(menubar, tearoff=0))
        root.config(menu=menubar)

        marco = tk.Frame(root)
        marco.pack(padx=10, pady=8, fill="x")

        tk.Label(marco, text="Nombre:").grid(row=0, column=0, sticky="w")
        self.entry_nombre = tk.Entry(marco, width=30)
        self.entry_nombre.grid(row=0, column=1, columnspan=2, padx=6, pady=4, sticky="w")

        tk.Label(marco, text="Edad:").grid(row=1, column=0, sticky="w")
        self.scale_edad = tk.Scale(marco, from_=0, to=100, orient="horizontal")
        self.scale_edad.set(20)
        self.scale_edad.grid(row=1, column=1, columnspan=2, sticky="we", padx=6)

        tk.Label(marco, text="Género:").grid(row=2, column=0, sticky="w")
        self.var_genero = tk.StringVar(value="Otro")
        tk.Radiobutton(marco, text="Masculino", variable=self.var_genero, value="Masculino").grid(row=2, column=1, sticky="w")
        tk.Radiobutton(marco, text="Femenino", variable=self.var_genero, value="Femenino").grid(row=2, column=2, sticky="w")

        tk.Button(marco, text="Añadir", command=self.añadir_usuario).grid(row=0, column=4, rowspan=2, padx=10)

        caja_lista = tk.Frame(root)
        caja_lista.pack(padx=10, pady=6, fill="both", expand=True)

        self.listbox = tk.Listbox(caja_lista)
        self.listbox.pack(side="left", fill="both", expand=True)

        scroll = tk.Scrollbar(caja_lista, orient="vertical", command=self.listbox.yview)
        scroll.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scroll.set)

        botones = tk.Frame(root)
        botones.pack(pady=6)

        tk.Button(botones, text="Eliminar seleccionado", command=self.eliminar_usuario).pack(side="left", padx=8)
        tk.Button(botones, text="Salir", command=root.quit).pack(side="left", padx=8)

        self.usuarios = []

    def añadir_usuario(self):
        nombre = self.entry_nombre.get().strip()
        edad = int(self.scale_edad.get())
        genero = self.var_genero.get()
        if not nombre:
            messagebox.showwarning("Aviso", "Introduce un nombre antes de añadir.")
            return
        entrada = f"{nombre} — {edad} años — {genero}"
        self.usuarios.append((nombre, edad, genero))
        self.listbox.insert(tk.END, entrada)
        self.entry_nombre.delete(0, tk.END)

    def eliminar_usuario(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("Eliminar", "No has seleccionado ningún usuario.")
            return
        idx = sel[0]
        self.listbox.delete(idx)
        del self.usuarios[idx]

    def guardar_lista(self):
        messagebox.showinfo("Guardar Lista", "Función 'Guardar Lista' (aún no implementada).")

    def cargar_lista(self):
        messagebox.showinfo("Cargar Lista", "Función 'Cargar Lista' (aún no implementada).")

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroApp(root)
    root.mainloop()
