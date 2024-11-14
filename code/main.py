# main.py
from interface import SimuladorOndasApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorOndasApp(root)
    root.mainloop()
