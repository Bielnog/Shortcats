import tkinter as tk
from controllers.shortcats_controller import ShortcatsController

if __name__ == "__main__":
    root = tk.Tk()
    app = ShortcatsController(root)
    root.mainloop()