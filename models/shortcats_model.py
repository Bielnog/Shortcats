import sqlite3

class ShortcatsModel:
    def __init__(self, db_path="shortcats.db"):
        self.db_path = db_path
        self.initialize_db()
        
    def initialize_db(self):
        """Cria o banco de dados e tabela se não existirem"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS shortcuts (
                name TEXT PRIMARY KEY,
                command TEXT NOT NULL
            )
            """
        )
        
        # Inserir dados iniciais se a tabela estiver vazia
        cursor.execute("SELECT COUNT(*) FROM shortcuts")
        if cursor.fetchone()[0] == 0:
            self.insert_initial_data(cursor)
            
        conn.commit()
        conn.close()
    
    def insert_initial_data(self, cursor):
        """Insere dados iniciais no banco"""
        initial_data = [
            ('Bloco de notas', 'notepad.exe'),
            ('Everything', 'C:\\Program Files (x86)\\Everything\\Everything.exe'),
        ]
        cursor.executemany("INSERT INTO shortcuts (name, command) VALUES (?, ?)", initial_data)
    
    def get_all_shortcuts(self):
        """Retorna todos os atalhos como dicionário {nome: comando}"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name, command FROM shortcuts")
        rows = cursor.fetchall()
        conn.close()
        return {row[0]: row[1] for row in rows}
    
    def add_shortcut(self, name, command):
        """Adiciona um novo atalho ao banco"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO shortcuts (name, command) VALUES (?, ?)",
                (name, command)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False  # Atalho já existe
        finally:
            conn.close()