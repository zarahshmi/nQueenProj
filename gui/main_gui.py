import tkinter as tk
from tkinter import ttk, messagebox
from algorithms.backtracking import solve_n_queens_backtracking
from algorithms.genetic import genetic_algorithm
from algorithms.csp import solve_n_queens_csp

MAX_CANVAS_SIZE = 600

class NQueensGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("N-Queens Solver")

        tk.Label(root, text="Board size (N):").grid(row=0, column=0, padx=5, pady=5)
        self.n_entry = tk.Entry(root)
        self.n_entry.grid(row=0, column=1, padx=5, pady=5)
        self.n_entry.insert(0, "8")

        tk.Label(root, text="Algorithm:").grid(row=1, column=0, padx=5, pady=5)
        self.alg_combo = ttk.Combobox(root, values=["Backtracking", "Genetic", "CSP"])
        self.alg_combo.grid(row=1, column=1, padx=5, pady=5)
        self.alg_combo.current(0)
        self.alg_combo.bind("<<ComboboxSelected>>", self.on_algo_change)

        self.solve_button = tk.Button(root, text="Solve", command=self.solve)
        self.solve_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.prev_button = tk.Button(root, text="Previous", command=self.show_prev, state="disabled")
        self.prev_button.grid(row=4, column=0, pady=5)
        self.next_button = tk.Button(root, text="Next", command=self.show_next, state="disabled")
        self.next_button.grid(row=4, column=1, pady=5)

        self.canvas = tk.Canvas(root, width=MAX_CANVAS_SIZE, height=MAX_CANVAS_SIZE)
        self.canvas.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.solutions = []
        self.current_index = 0
        self.n = 8
        self.cell_size = 60

    def on_algo_change(self, event):
        self.prev_button.config(state="disabled")
        self.next_button.config(state="disabled")

    def update_cell_size(self, n):

        self.cell_size = max(10, min(MAX_CANVAS_SIZE // n, 60))

    def draw_board(self, n):
        self.canvas.delete("all")
        self.update_cell_size(n)
        size = self.cell_size * n
        self.canvas.config(width=size, height=size)
        colors = ["#f0d9b5", "#b58863"]

        for i in range(n):
            for j in range(n):
                color = colors[(i + j) % 2]
                self.canvas.create_rectangle(
                    j*self.cell_size, i*self.cell_size,
                    (j+1)*self.cell_size, (i+1)*self.cell_size,
                    fill=color, outline="black"
                )

    def draw_queen(self, x, y):
        cx = x * self.cell_size + self.cell_size // 2
        cy = y * self.cell_size + self.cell_size // 2
        radius = self.cell_size // 3

        self.canvas.create_oval(
            cx - radius, cy - radius,
            cx + radius, cy + radius,
            fill="#d42e2e", outline="black", width=2
        )
        self.canvas.create_oval(
            cx - radius + 6, cy - radius + 6,
            cx + radius - 6, cy + radius - 6,
            fill="#ff5c5c", outline=""
        )
        base_height = radius // 3
        self.canvas.create_rectangle(
            cx - radius // 2, cy + radius - base_height,
            cx + radius // 2, cy + radius,
            fill="#6b1b1b", outline="black"
        )
        crown_radius = radius // 6
        offsets = [-radius // 2, 0, radius // 2]
        for off in offsets:
            self.canvas.create_oval(
                cx + off - crown_radius, cy - radius - crown_radius * 2,
                cx + off + crown_radius, cy - radius,
                fill="#f4d35e", outline="black"
            )
        self.canvas.create_line(
            cx - radius, cy - radius,
            cx + radius, cy - radius,
            fill="black", width=2
        )

    def draw_solution(self, solution):
        if solution is None:
            messagebox.showinfo("No solution", "No solution found!")
            return
        n = len(solution)
        self.draw_board(n)
        for col, row in enumerate(solution):
            self.draw_queen(col, row)

    def solve(self):
        try:
            self.n = int(self.n_entry.get())
            if self.n < 4:
                messagebox.showwarning("Invalid input", "Please enter N >= 4")
                return
        except ValueError:
            messagebox.showwarning("Invalid input", "Please enter a valid integer for N")
            return

        algo = self.alg_combo.get()

        if algo == "Backtracking":
            self.solutions = solve_n_queens_backtracking(self.n)
            if not self.solutions:
                messagebox.showinfo("No solution", "No solutions found!")
                self.prev_button.config(state="disabled")
                self.next_button.config(state="disabled")
                return
            self.current_index = 0
            self.draw_solution(self.solutions[self.current_index])
            self.prev_button.config(state="normal")
            self.next_button.config(state="normal")

        else:
            if algo == "Genetic":
                sol = genetic_algorithm(self.n)
            else:
                sol = solve_n_queens_csp(self.n)

            self.solutions = [sol] if sol else []
            if not self.solutions or self.solutions[0] is None:
                messagebox.showinfo("No solution", "No solution found!")
                self.prev_button.config(state="disabled")
                self.next_button.config(state="disabled")
                return
            self.current_index = 0
            self.draw_solution(self.solutions[0])
            self.prev_button.config(state="disabled")
            self.next_button.config(state="disabled")

    def show_prev(self):
        if not self.solutions:
            return
        self.current_index = (self.current_index - 1) % len(self.solutions)
        self.draw_solution(self.solutions[self.current_index])

    def show_next(self):
        if not self.solutions:
            return
        self.current_index = (self.current_index + 1) % len(self.solutions)
        self.draw_solution(self.solutions[self.current_index])

if __name__ == "__main__":
    root = tk.Tk()
    app = NQueensGUI(root)
    root.mainloop()
