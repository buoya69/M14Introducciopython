import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLUE = (63, 72, 204)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cara de Doraemon")

def draw_doraemon():

    pygame.draw.circle(screen, BLUE, (200, 200), 150)
    pygame.draw.circle(screen, WHITE, (200, 200), 150, 5)

    pygame.draw.circle(screen, WHITE, (130, 130), 30)
    pygame.draw.circle(screen, BLACK, (130, 130), 10)
    pygame.draw.circle(screen, WHITE, (270, 130), 30)
    pygame.draw.circle(screen, BLACK, (270, 130), 10)

    pygame.draw.rect(screen, RED, (150, 230, 100, 50))

    pygame.draw.circle(screen, BLACK, (200, 180), 10)

    pygame.draw.line(screen, BLACK, (100, 170), (150, 170), 5)
    pygame.draw.line(screen, BLACK, (100, 200), (150, 200), 5)
    pygame.draw.line(screen, BLACK, (100, 230), (150, 230), 5)
    pygame.draw.line(screen, BLACK, (250, 170), (300, 170), 5)
    pygame.draw.line(screen, BLACK, (250, 200), (300, 200), 5)
    pygame.draw.line(screen, BLACK, (250, 230), (300, 230), 5)

    pygame.draw.circle(screen, BLACK, (170, 270), 5)
    pygame.draw.circle(screen, BLACK, (230, 270), 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    draw_doraemon()

    pygame.display.flip()
