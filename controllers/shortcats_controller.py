import subprocess

class ShortcatsController:
    def __init__(self, root):
        from models.shortcats_model import ShortcatsModel
        from views.shortcats_view import ShortcatsView
        
        self.model = ShortcatsModel()
        self.view = ShortcatsView(root, self)
        
        # Vincular eventos
        self.view.entry.bind("<KeyRelease>", self.handle_key_release)
        self.view.entry.bind("<Tab>", self.handle_tab)
        self.view.entry.bind("<Return>", self.handle_return)
        self.view.entry.bind("<Down>", self.focus_listbox)
        self.view.listbox.bind("<<ListboxSelect>>", self.handle_listbox_select)
        self.view.listbox.bind("<Double-Button-1>", self.handle_double_click)
        self.view.listbox.bind("<Return>", self.handle_return)
        root.bind("<Escape>", lambda e: self.view.destroy())
        
        self.current_dialog = None
    
    def handle_key_release(self, event):
        """Trata o evento de digitação no campo de entrada"""
        term = self.view.get_entry_text().lower()
        
        if term == "all":
            suggestions = sorted(self.model.get_all_shortcuts().keys())
        else:
            suggestions = sorted(
                name for name in self.model.get_all_shortcuts().keys() 
                if name.lower().startswith(term)
            )
        
        self.view.update_suggestions(suggestions)
    
    def handle_tab(self, event):
        """Trata o evento de tabulação"""
        term = self.view.get_entry_text().lower()
        matches = sorted(
            name for name in self.model.get_all_shortcuts().keys() 
            if name.lower().startswith(term)
        )
        
        if matches:
            self.view.set_entry(matches[0])
            self.view.update_suggestions([])
        return "break"
    
    def handle_return(self, event):
        """Trata o evento de pressionar Enter"""
        self.execute_command()
    
    def handle_listbox_select(self, event):
        """Trata a seleção na listbox"""
        if self.view.listbox.curselection():
            index = self.view.listbox.curselection()[0]
            value = self.view.listbox.get(index)
            self.view.set_entry(value)
            self.view.update_suggestions([])
    
    def handle_double_click(self, event):
        """Trata o duplo clique na listbox"""
        self.execute_command()
    
    def focus_listbox(self, event):
        """Foca na listbox quando seta para baixo é pressionada"""
        if self.view.listbox.size() > 0:
            self.view.listbox.focus_set()
            self.view.listbox.selection_set(0)
        return "break"
    
    def execute_command(self):
        """Executa o comando do atalho selecionado"""
        term = self.view.get_entry_text().lower()
        matches = sorted(
            name for name in self.model.get_all_shortcuts().keys() 
            if name.lower().startswith(term)
        )
        
        if matches:
            command = self.model.get_all_shortcuts()[matches[0]]
            if matches[0].lower() == "sqltool":
                subprocess.Popen(
                    command, shell=True, 
                    cwd=r"C:\Users\gabriel.nogueira\Desktop"
                )
            else:
                subprocess.Popen(command, shell=True)
            self.view.destroy()
    
    def open_add_dialog(self):
        """Abre o diálogo para adicionar novo atalho"""
        if not hasattr(self, 'current_dialog') or not self.current_dialog:
            self.current_dialog = self.view.create_add_dialog()
            self.current_dialog.protocol(
                "WM_DELETE_WINDOW", 
                lambda: self.close_add_dialog()
            )
    
    def close_add_dialog(self):
        """Fecha o diálogo de adição"""
        if hasattr(self, 'current_dialog') and self.current_dialog:
            self.current_dialog.destroy()
            self.current_dialog = None
    
    def save_new_shortcut(self, name, command):
        """Salva um novo atalho no banco de dados"""
        if name and command:
            success = self.model.add_shortcut(name, command)
            if success:
                self.close_add_dialog()
            else:
                # Aqui você poderia mostrar uma mensagem de erro na interface
                print("O atalho já existe no banco de dados.")