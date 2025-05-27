from gui.main_gui import NQueensGUI
import tkinter as tk

def main():
    root = tk.Tk()
    app = NQueensGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
