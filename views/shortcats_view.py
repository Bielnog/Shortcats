import tkinter as tk
from tkinter import ttk
import ctypes
from PIL import Image, ImageTk


class ShortcatsView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller

        # Configuração básica da janela
        master.title("Shortcats")
        master.overrideredirect(True)
        self.add_to_taskbar(master)
        self.set_window_icon()
        master.attributes("-topmost", True)

        # Aplicar tema dark
        self.apply_dark_theme()

        # Criar widgets
        self.create_title_bar()
        self.create_main_widgets()

    def set_window_icon(self):
        """Define o ícone da janela principal"""
        try:
            # Para .ico no Windows
            self.master.iconbitmap("assets/cato.ico")
        except:
            # Fallback para PNG usando PhotoImage
            self.icon_image = tk.PhotoImage(file="assets/cato.png")
            self.master.iconphoto(True, self.icon_image)

    def add_to_taskbar(self, window):
        """Adiciona a janela à barra de tarefas"""
        hwnd = ctypes.windll.user32.GetParent(window.winfo_id())
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("meuapp.atalhos")
        ctypes.windll.user32.ShowWindow(hwnd, 4)

    def apply_dark_theme(self):
        """Configura o tema dark"""
        self.master.configure(bg="#1e1e1e")
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(".", background="#1e1e1e", foreground="red")
        style.configure("TEntry", fieldbackground="#2d2d2d", foreground="white")
        style.configure("TButton", background="#3d3d3d", foreground="red")
        style.map("TButton", background=[("active", "#4d4d4d")])

    def create_title_bar(self):
        """Cria a barra de título personalizada"""
        self.title_bar = tk.Frame(self.master, bg="#1e1e1e", relief="raised", bd=0)
        self.title_bar.pack(fill="x")

        # Botões
        self.close_btn = tk.Button(
            self.title_bar,
            text="×",
            bg="#1e1e1e",
            fg="red",
            bd=0,
            command=self.master.destroy,
            font=("Arial", 12, "bold"),
        )
        self.close_btn.pack(side="right", padx=5, pady=2)

        self.minimize_btn = tk.Button(
            self.title_bar,
            text="–",
            bg="#1e1e1e",
            fg="white",
            bd=0,
            command=lambda: self.master.iconify(),
            font=("Arial", 12, "bold"),
        )
        self.minimize_btn.pack(side="right", padx=5, pady=2)

        # Título
        self.title_label = tk.Label(
            self.title_bar,
            text="Shortcats",
            bg="#1e1e1e",
            fg="white",
            font=("Arial", 10),
        )
        self.title_label.pack(side="left", padx=10)

        # Eventos de arrastar
        self.title_bar.bind("<ButtonPress-1>", self.start_drag)
        self.title_bar.bind("<ButtonRelease-1>", self.stop_drag)
        self.title_bar.bind("<B1-Motion>", self.do_drag)

    def create_main_widgets(self):
        """Cria os widgets principais da interface"""
        # Campo de entrada
        self.entry = ttk.Entry(self.master, width=40)
        self.entry.pack(pady=10, padx=10)
        self.entry.focus_set()

        # Lista de sugestões
        self.listbox = tk.Listbox(
            self.master, width=38, bg="#2d2d2d", fg="white", selectbackground="#3d3d3d"
        )
        self.listbox.pack()
        self.listbox.pack_forget()

        # Botão para adicionar novo atalho
        self.add_btn = tk.Button(
            self.master,
            text="Adicionar Atalho",
            bg="#1e1e1e",
            fg="white",
            bd=1,
            command=self.controller.open_add_dialog,
        )
        self.add_btn.pack(pady=5)

    def start_drag(self, event):
        self._drag_data = {"x": event.x, "y": event.y}

    def stop_drag(self, event):
        self._drag_data = None

    def do_drag(self, event):
        if hasattr(self, "_drag_data") and self._drag_data:
            x = self.master.winfo_x() + (event.x - self._drag_data["x"])
            y = self.master.winfo_y() + (event.y - self._drag_data["y"])
            self.master.geometry(f"+{x}+{y}")

    def create_add_dialog(self):
        """Cria a janela de diálogo para adicionar novo atalho"""
        dialog = tk.Toplevel(self.master)
        dialog.title("Adicionar Atalho")
        dialog.configure(bg="#1e1e1e")
        dialog.geometry("300x150")

        # Widgets
        tk.Label(dialog, text="Nome:", bg="#1e1e1e", fg="white").pack(pady=5)
        name_entry = ttk.Entry(dialog, width=30)
        name_entry.pack()

        tk.Label(dialog, text="Caminho:", bg="#1e1e1e", fg="white").pack(pady=5)
        path_entry = ttk.Entry(dialog, width=30)
        path_entry.pack()

        tk.Button(
            dialog,
            text="Salvar",
            bg="#3d3d3d",
            fg="white",
            command=lambda: self.controller.save_new_shortcut(
                name_entry.get().strip(), path_entry.get().strip()
            ),
        ).pack(pady=10)

        return dialog

    def update_suggestions(self, suggestions):
        """Atualiza a lista de sugestões"""
        self.listbox.delete(0, tk.END)
        if suggestions:
            for item in suggestions:
                self.listbox.insert(tk.END, item)
            self.listbox.pack()
        else:
            self.listbox.pack_forget()

    def close_add_dialog(self, dialog):
        """Fecha a janela de diálogo de adição"""
        dialog.destroy()

    def clear_entry(self):
        """Limpa o campo de entrada"""
        self.entry.delete(0, tk.END)

    def set_entry(self, text):
        """Define o texto do campo de entrada"""
        self.entry.delete(0, tk.END)
        self.entry.insert(0, text)

    def get_entry_text(self):
        """Retorna o texto do campo de entrada"""
        return self.entry.get().strip()

    def destroy(self):
        """Destroi a janela principal"""
        self.master.destroy()
