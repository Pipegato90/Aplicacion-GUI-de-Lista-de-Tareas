import tkinter as tk
from tkinter import ttk, messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x500")

        # Configurar estilo
        self.style = ttk.Style()
        self.style.configure("Completed.TLabel", foreground="gray", font=('Arial', 10, 'overstrike'))
        self.style.configure("Normal.TLabel", foreground="black", font=('Arial', 10))

        # Crear widgets
        self.create_widgets()

        # Configurar eventos
        self.setup_events()

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Entrada de texto
        self.task_entry = ttk.Entry(main_frame, font=('Arial', 12))
        self.task_entry.pack(fill=tk.X, pady=(0, 10))

        # Frame para botones
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(0, 10))

        # Botones
        self.add_button = ttk.Button(button_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

        self.complete_button = ttk.Button(button_frame, text="Marcar Completada", command=self.mark_completed)
        self.complete_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

        self.delete_button = ttk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

        # Lista de tareas
        self.task_list = tk.Listbox(main_frame, font=('Arial', 12), selectmode=tk.SINGLE)
        self.task_list.pack(fill=tk.BOTH, expand=True)

        # Barra de desplazamiento
        scrollbar = ttk.Scrollbar(self.task_list)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_list.yview)

    def setup_events(self):
        # Evento de tecla Enter en el campo de entrada
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        # Evento de doble clic en la lista
        self.task_list.bind("<Double-Button-1>", lambda event: self.mark_completed())

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.task_list.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea válida")

    def mark_completed(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            task_text = self.task_list.get(index)

            # Verificar si ya está marcada como completada
            if not task_text.startswith("✓ "):
                self.task_list.delete(index)
                self.task_list.insert(index, f"✓ {task_text}")
                self.task_list.itemconfig(index, {'fg': 'gray'})
            else:
                messagebox.showinfo("Información", "Esta tarea ya está marcada como completada")
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea")

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.task_list.delete(selected_index)
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()