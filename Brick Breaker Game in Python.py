import pygame
import time
import random

class Game:
    # Constructor for initializing
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Brick Game")

        # Ball Variables
        self.ball_x = 383
        self.ball_y = 540
        self.ball_direction = 'UpRight'
        self.ball_stop = True

        # Paddle Variables
        self.paddle_x = 350
        self.paddle_y = 548
        self.paddle_stop = True

        # Game Logic Variables
        self.game_started = False
        self.pause = False
        self.running = True
        self.lives = 3
        self.score = 0
        self.high_score = 0

        # Brick Variables
        self.bricks = []
        self.power_ups = []
        self.cracked_bricks = []
        self.brick_states = {}

        # Load Images
        self.purple_bricks = pygame.image.load('img/Breakout Tile Set Free/PNG/05-Breakout-Tiles.png')
        self.purple_bricks_cracked = pygame.image.load('img/Breakout Tile Set Free/PNG/06-Breakout-Tiles.png')
        self.grey_bricks = pygame.image.load('img/Breakout Tile Set Free/PNG/17-Breakout-Tiles.png')
        self.grey_bricks_cracked = pygame.image.load('img/Breakout Tile Set Free/PNG/18-Breakout-Tiles.png')
        self.heart = pygame.image.load('img/Breakout Tile Set Free/PNG/60-Breakout-Tiles.png')
        self.paddle = pygame.image.load('img/Breakout Tile Set Free/PNG/56-Breakout-Tiles.png')
        self.ball = pygame.image.load('img/Breakout Tile Set Free/PNG/58-Breakout-Tiles.png')
        self.power_up = pygame.image.load('img/Breakout Tile Set Free/PNG/60-Breakout-Tiles.png')

        # Image Transformations
        self.paddle = pygame.transform.scale(self.paddle, (80, 20))
        self.heart = pygame.transform.scale(self.heart, (20, 20))
        self.ball = pygame.transform.scale(self.ball, (15, 15))
        self.power_up = pygame.transform.scale(self.power_up, (30, 30))
        self.purple_bricks = pygame.transform.scale(self.purple_bricks, (60, 20))
        self.grey_bricks = pygame.transform.scale(self.grey_bricks, (60, 20))
        self.purple_bricks_cracked = pygame.transform.scale(self.purple_bricks_cracked, (60, 20))
        self.grey_bricks_cracked = pygame.transform.scale(self.grey_bricks_cracked, (60, 20))

        # Load Sounds
        self.hit_brick_sound = pygame.mixer.Sound('img/Breakout Tile Set Free/PNG/brick.wav')
        self.hit_paddle_sound = pygame.mixer.Sound('img/Breakout Tile Set Free/PNG/glass.wav')
        self.game_over_sound = pygame.mixer.Sound('img/Breakout Tile Set Free/PNG/game_over2.wav')
        self.life_lost_sound = pygame.mixer.Sound('img/Breakout Tile Set Free/PNG/game_over.wav')

    # Generate Bricks
    def generate_bricks(self):
        brick_x = 65
        brick_y = 20
        for row in range(4):
            for col in range(13):
                x = col * brick_x
                y = 50 + row * brick_y
                brick_color = self.purple_bricks if (row + col) % 2 == 0 else self.grey_bricks
                brick_rect = pygame.Rect(x, y, brick_x, brick_y)
                self.bricks.append({"rect": brick_rect, "color": brick_color, "state": 0})

    # Check if all bricks are removed
    def all_bricks_removed(self):
        if not self.bricks:
            self.ball_stop = True
            self.reset_ball()
            time.sleep(0.2)
            self.generate_bricks()

    # Reset Ball
    def reset_ball(self):
        self.ball_x, self.ball_y = 383, 540
        self.paddle_x = 350
        self.paddle_y = 548
        self.power_ups.clear()

    # Manage High Score
    def high_score_manager(self):
        try:
            with open("HighScore.txt", "r") as file:
                content = file.read()
                self.high_score = int(content) if content else 0
        except FileNotFoundError:
            self.high_score = 0

        if self.score > self.high_score:
            self.high_score = self.score
            with open("HighScore.txt", "w") as file:
                file.write(str(self.high_score))

    # Ball Movement
    def go_up_right(self):
        self.ball_x += 1.7
        self.ball_y -= 3
        time.sleep(0.007)

    def go_up_left(self):
        self.ball_x -= 1.7
        self.ball_y -= 3
        time.sleep(0.007)

    def go_down_right(self):
        self.ball_x += 1.7
        self.ball_y += 3
        time.sleep(0.007)

    def go_down_left(self):
        self.ball_x -= 1.7
        self.ball_y += 3
        time.sleep(0.007)

# Main
if __name__ == "__main__":
    game = Game()
    game.generate_bricks()
    # Add your main game loop here
