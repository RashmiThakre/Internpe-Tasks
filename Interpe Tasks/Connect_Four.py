import tkinter as tk
from tkinter import messagebox

ROWS = 6
COLS = 7
PLAYER_COLORS = ["green", "blue"]

class ConnectFour:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        self.canvas = tk.Canvas(root, width=COLS*100, height=ROWS*100, bg="grey")
        self.canvas.pack()
        self.initialize_board()
        self.current_player = 0
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.canvas.bind("<Button-1>", self.handle_click)
        
    def initialize_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                x0 = col * 100
                y0 = row * 100
                x1 = x0 + 100
                y1 = y0 + 100
                self.canvas.create_oval(x0+5, y0+5, x1-5, y1-5, fill="white", tags=f"cell_{row}_{col}")
                
    def handle_click(self, event):
        col = event.x // 100
        for row in range(ROWS-1, -1, -1):
            if self.board[row][col] is None:
                self.board[row][col] = self.current_player
                self.update_board(row, col)
                if self.check_winner(row, col):
                    messagebox.showinfo("Game Over", f"Player {self.current_player + 1} wins!")
                    self.reset_game()
                self.current_player = (self.current_player + 1) % 2
                break

    def update_board(self, row, col):
        color = PLAYER_COLORS[self.current_player]
        x0 = col * 100
        y0 = row * 100
        x1 = x0 + 100
        y1 = y0 + 100
        self.canvas.create_oval(x0+5, y0+5, x1-5, y1-5, fill=color, tags=f"cell_{row}_{col}")

    def check_winner(self, row, col):
      
        def count_consecutive(r_step, c_step):
            count = 0
            r, c = row, col
            while 0 <= r < ROWS and 0 <= c < COLS and self.board[r][c] == self.current_player:
                count += 1
                r += r_step
                c += c_step
            return count

        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for r_step, c_step in directions:
            count = (count_consecutive(r_step, c_step) +
                     count_consecutive(-r_step, -c_step) - 1)
            if count >= 4:
                return True
        return False
    
    def reset_game(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.canvas.delete("all")
        self.initialize_board()

if __name__ == "__main__":
    root = tk.Tk()
    game = ConnectFour(root)
    root.mainloop()
