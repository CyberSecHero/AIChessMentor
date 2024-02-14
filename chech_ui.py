import tkinter as tk

class ChessGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Chess Game")
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.draw_board()

    def draw_board(self):
        colors = ["white", "gray"]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                x0, y0 = col * 50, row * 50
                x1, y1 = x0 + 50, y0 + 50
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

def main():
    root = tk.Tk()
    gui = ChessGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
