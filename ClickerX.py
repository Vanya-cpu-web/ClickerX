import pygame
import sys


pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Кликер")
background = pygame.transform.scale(pygame.image.load("Zhdun.jpg"), (WIDTH,))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont('Arial', 50)
clicks = 0

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicks += 1  


    screen.fill(WHITE)


    text = font.render(f"Кликов: {clicks}", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))


    pygame.display.flip()

pygame.quit()
sys.exit()