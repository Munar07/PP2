import pygame
from clock import load_images, draw_clock

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mickey Clock")

font = pygame.font.SysFont("Arial", 36)
game_clock = pygame.time.Clock()

clock_img, left_hand, right_hand = load_images()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_clock(screen, font, clock_img, left_hand, right_hand)

    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()