import pygame
import random
import sys

pygame.init()

WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont(None, 35)

snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0) 

food = (
    random.randrange(0, WIDTH, CELL_SIZE),
    random.randrange(0, HEIGHT, CELL_SIZE)
    
)

score = 0
game_over = False

def draw_snake():
    for part in snake:
        pygame.draw.rect(
            screen, GREEN,
            (part[0], part[1], CELL_SIZE, CELL_SIZE)
        )
        
def draw_food():
    pygame.draw.rect(
        screen, RED,
        (food[0], food[1], CELL_SIZE, CELL_SIZE)
    )
    
def show_score():
    text = font.render(f"Score:{score}", True, WHITE)
    screen.blit(text, (10, 10))
    
    
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE) 
                
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
                
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
                
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)
                
            
            elif event.key == pygame.K_r and game_over:
                snake = [(100, 100), (80, 100), (60, 100)]
                direction = (CELL_SIZE, 0)
                score = 0
                food = (
                    random.randrange(0, WIDTH, CELL_SIZE),
                    random.randrange(0, HEIGHT, CELL_SIZE)
                )
                game_over = False
                
    if not game_over:
        
        head_x = snake[0][0] + direction[0]
        head_y = snake[0][1] + direction[1]
        
        new_head = (head_x, head_y)
        
        snake.insert(0, new_head)
        
        if new_head == food:
            score += 10
            
            while food in snake:
                food = (
                    random.randrange(0, WIDTH, CELL_SIZE),
                    random.randrange(0, HEIGHT, CELL_SIZE)
                )
                
        else:
            snake.pop()
            
        if (head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT):
            game_over = True
            
        if new_head in snake[1:]:
            game_over = True
            
    screen.fill(BLACK)
            
    draw_snake()
    draw_food()
    show_score()
            
    if game_over:
        text = font.render("GAME OVER! Press R to Restart", True, RED)
        screen.blit(text, (100, HEIGHT // 2))
                        
    pygame.display.update()
                    
    clock.tick(10)
