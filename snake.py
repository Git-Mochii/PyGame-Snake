
# Snake PyGame Project #

import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Window dimensions
window_width = 800
window_height = 800

# Game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Clock to control the game's speed
clock = pygame.time.Clock()

# Initial game settings
initial_tick_rate = 5
food_eaten = 0
score = 0
grid_block_size = 50

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (179, 179, 179)

# Function to create a grid with grid lines
def create_grid():
    for x in range(0, window_width, grid_block_size):
        for y in range(0, window_height, grid_block_size):
            rect = pygame.Rect(x, y, grid_block_size, grid_block_size)
            pygame.draw.rect(window, GRAY, rect, 1)

# Function to display score
def display_score(score):
    font = pygame.font.Font(None, 30)
    text = font.render(f"Score: {score}", True, WHITE)
    window.blit(text, (10, 10))

# Class to represent the snake
class Snake:
    def __init__(self):
        self.x, self.y = grid_block_size, grid_block_size
        self.direction_x = 1  # Default right direction
        self.direction_y = 0  # Default left direction

        self.body = [pygame.Rect(self.x - grid_block_size, self.y, grid_block_size, grid_block_size)]
        self.head = pygame.Rect(self.x, self.y, grid_block_size, grid_block_size)

        self.death = False

    def update(self):
        for sq in self.body:
            if self.head.colliderect(sq):  # Check for self-collision
                self.death = True
            if not (0 <= self.head.x < window_width) or not (0 <= self.head.y < window_height):
                self.death = True

        if self.death:
            self.x, self.y = grid_block_size, grid_block_size
            self.head = pygame.Rect(self.x, self.y, grid_block_size, grid_block_size)
            self.body = [pygame.Rect(self.x - grid_block_size, self.y, grid_block_size, grid_block_size)]
            self.direction_x = 1
            self.direction_y = 0
            self.death = False

        self.body.append(self.head)

        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y

        self.head.x += self.direction_x * grid_block_size
        self.head.y += self.direction_y * grid_block_size
        self.body.remove(self.head)

# Class to represent the food
class Food:
    def __init__(self):
        self.x = random.randint(0, (window_width - grid_block_size) // grid_block_size) * grid_block_size
        self.y = random.randint(0, (window_height - grid_block_size) // grid_block_size) * grid_block_size
        self.rect = pygame.Rect(self.x, self.y, grid_block_size, grid_block_size)

    def update(self):
        pygame.draw.rect(window, RED, self.rect)

# Create the objects
create_grid()
snake = Snake()
food = Food()

# Main game loop
while True:
    if snake.death:
        food_eaten = 0  # Reset the food counter
        clock.tick(initial_tick_rate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.direction_y = 1
                snake.direction_x = 0
            elif event.key == pygame.K_UP:
                snake.direction_y = -1
                snake.direction_x = 0
            elif event.key == pygame.K_RIGHT:
                snake.direction_y = 0
                snake.direction_x = 1
            elif event.key == pygame.K_LEFT:
                snake.direction_y = 0
                snake.direction_x = -1

    snake.update()

    window.fill(BLACK)
    create_grid()

    food.update()

    pygame.draw.rect(window, GREEN, snake.head)

    if snake.head.colliderect(food.rect):
        snake.body.append(pygame.Rect(snake.body[-1].x, snake.body[-1].y, grid_block_size, grid_block_size))
        food.x = random.randint(0, (window_width - grid_block_size) // grid_block_size) * grid_block_size
        food.y = random.randint(0, (window_height - grid_block_size) // grid_block_size) * grid_block_size
        food.rect = pygame.Rect(food.x, food.y, grid_block_size, grid_block_size)
        food_eaten += 1
        score += 1

        # Check if the snake has eaten 3 food items and increase the tick rate.
        if food_eaten == 3:
            initial_tick_rate += 1  # Increase the tick rate
            food_eaten = 0

    window.fill(BLACK)
    create_grid()
    food.update()
    display_score(score)
    pygame.draw.rect(window, GREEN, snake.head)

    for sq in snake.body:
        pygame.draw.rect(window, GREEN, sq)

    clock.tick(initial_tick_rate)
    pygame.display.update()