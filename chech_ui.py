import tkinter as tk

class ChessGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Chess Game")
        self.canvas = tk.Canvas(master, width=480, height=480)
        self.canvas.pack()

        # Load and resize piece images
        self.piece_images = {
            "pawn_white": tk.PhotoImage(file="pieces/png/white-pawn.png").subsample(2),
            "pawn_black": tk.PhotoImage(file="pieces/png/black-pawn.png").subsample(2),
            "rook_white": tk.PhotoImage(file="pieces/png/white-rook.png").subsample(2),
            "rook_black": tk.PhotoImage(file="pieces/png/black-rook.png").subsample(2),
            "knight_white": tk.PhotoImage(file="pieces/png/white-knight.png").subsample(2),
            "knight_black": tk.PhotoImage(file="pieces/png/black-knight.png").subsample(2),
            "bishop_white": tk.PhotoImage(file="pieces/png/white-bishop.png").subsample(2),
            "bishop_black": tk.PhotoImage(file="pieces/png/black-bishop.png").subsample(2),
            "queen_white": tk.PhotoImage(file="pieces/png/white-queen.png").subsample(2),
            "queen_black": tk.PhotoImage(file="pieces/png/black-queen.png").subsample(2),
            "king_white": tk.PhotoImage(file="pieces/png/white-king.png").subsample(2),
            "king_black": tk.PhotoImage(file="pieces/png/black-king.png").subsample(2),
        }

        self.draw_board()

    def draw_board(self):
        colors = ["white", "gray"]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                x0, y0 = col * 60, row * 60
                x1, y1 = x0 + 60, y0 + 60
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

        # Place pieces on the board
        for row, pieces in enumerate([
            ["rook_black", "knight_black", "bishop_black", "queen_black", "king_black", "bishop_black", "knight_black", "rook_black"],
            ["pawn_black"] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            ["pawn_white"] * 8,
            ["rook_white", "knight_white", "bishop_white", "queen_white", "king_white", "bishop_white", "knight_white", "rook_white"]
        ]):
            for col, piece in enumerate(pieces):
                if piece:
                    self.canvas.create_image(col * 60 + 30, row * 60 + 30, image=self.piece_images[piece])

def main():
    root = tk.Tk()
    gui = ChessGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
