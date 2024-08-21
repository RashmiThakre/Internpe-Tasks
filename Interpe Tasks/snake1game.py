import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")

        self.width = 800
        self.height = 600
        self.cell_size = 20

        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height, bg="grey")
        self.canvas.pack()

        self.snake = [(self.width//2, self.height//2)]
        self.snake_direction = "Right"
        self.food = self.place_food()

        self.game_over = False

        self.master.bind("<KeyPress>", self.change_direction)
        self.run_game()

    def place_food(self):
        while True:
            x = random.randint(0, (self.width - self.cell_size) // self.cell_size) * self.cell_size
            y = random.randint(0, (self.height - self.cell_size) // self.cell_size) * self.cell_size
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, event):
        if event.keysym in ["Left", "Right", "Up", "Down"]:
            self.snake_direction = event.keysym

    def run_game(self):
        if not self.game_over:
            self.move_snake()
            self.check_collision()
            self.check_food()
            self.update_canvas()
            self.master.after(200, self.run_game)  # Increase the delay to slow down the game

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.snake_direction == "Left":
            head_x -= self.cell_size
        elif self.snake_direction == "Right":
            head_x += self.cell_size
        elif self.snake_direction == "Up":
            head_y -= self.cell_size
        elif self.snake_direction == "Down":
            head_y += self.cell_size

        new_head = (head_x, head_y)
        self.snake = [new_head] + self.snake[:-1]

    def check_collision(self):
        head_x, head_y = self.snake[0]
        if head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height or len(self.snake) != len(set(self.snake)):
            self.game_over = True

    def check_food(self):
        if self.snake[0] == self.food:
            self.snake.append(self.snake[-1])
            self.food = self.place_food()

    def update_canvas(self):
        self.canvas.delete(tk.ALL)
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill="black")
        food_x, food_y = self.food
        self.canvas.create_rectangle(food_x, food_y, food_x + self.cell_size, food_y + self.cell_size, fill="red")
        if self.game_over:
            self.canvas.create_text(self.width//2, self.height//2, text="Game Over!!", fill="red", font=("Times new roman", 24))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
