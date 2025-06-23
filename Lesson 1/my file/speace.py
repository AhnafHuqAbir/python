import tkinter as tk
import random

# Constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
SPACESHIP_SPEED = 20
BULLET_SPEED = 10
ASTEROID_SPEED = 5
ASTEROID_INTERVAL = 2000  # in ms
LEVEL_UP_SCORE = 10

class GalaxyDefender:
    def __init__(self, root):
        self.root = root
        self.root.title(":-] Galaxy Defender")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
        self.canvas.pack()

        self.score = 0
        self.level = 1
        self.bullets = []
        self.asteroids = []

        # Create spaceship
        self.spaceship = self.canvas.create_rectangle(230, 550, 270, 580, fill="cyan")

        # Show score and level
        self.text = self.canvas.create_text(10, 10, anchor="nw", fill="white", font=("Arial", 14), text=self.get_status_text())

        # Controls
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.fire_bullet)

        # Start asteroid creation and game loop
        self.spawn_asteroid()
        self.game_loop()

    def get_status_text(self):
        return f"Score: {self.score} | Level: {self.level}"

    def move_left(self, event):
        self.canvas.move(self.spaceship, -SPACESHIP_SPEED, 0)

    def move_right(self, event):
        self.canvas.move(self.spaceship, SPACESHIP_SPEED, 0)

    def fire_bullet(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.spaceship)
        bullet = self.canvas.create_rectangle(x1 + 15, y1 - 10, x1 + 17, y1, fill="red")
        self.bullets.append(bullet)

    def spawn_asteroid(self):
        x = random.randint(0, WINDOW_WIDTH - 30)
        asteroid = self.canvas.create_oval(x, 0, x + 30, 30, fill="gray")
        self.asteroids.append(asteroid)
        self.root.after(ASTEROID_INTERVAL, self.spawn_asteroid)

    def move_bullets(self):
        for bullet in self.bullets[:]:
            self.canvas.move(bullet, 0, -BULLET_SPEED)
            _, y1, _, y2 = self.canvas.coords(bullet)
            if y2 < 0:
                self.canvas.delete(bullet)
                self.bullets.remove(bullet)

    def move_asteroids(self):
        for asteroid in self.asteroids[:]:
            self.canvas.move(asteroid, 0, ASTEROID_SPEED)
            _, y1, _, y2 = self.canvas.coords(asteroid)
            if y1 > WINDOW_HEIGHT:
                self.canvas.delete(asteroid)
                self.asteroids.remove(asteroid)

    def check_collisions(self):
        for bullet in self.bullets[:]:
            bx1, by1, bx2, by2 = self.canvas.coords(bullet)
            for asteroid in self.asteroids[:]:
                ax1, ay1, ax2, ay2 = self.canvas.coords(asteroid)
                if bx2 > ax1 and bx1 < ax2 and by2 > ay1 and by1 < ay2:
                    # Collision
                    self.canvas.delete(bullet)
                    self.canvas.delete(asteroid)
                    self.bullets.remove(bullet)
                    self.asteroids.remove(asteroid)
                    self.score += 1
                    if self.score % LEVEL_UP_SCORE == 0:
                        self.level += 1
                    self.canvas.itemconfig(self.text, text=self.get_status_text())
                    break

    def game_loop(self):
        self.move_bullets()
        self.move_asteroids()
        self.check_collisions()
        self.root.after(50, self.game_loop)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = GalaxyDefender(root)
    root.mainloop()