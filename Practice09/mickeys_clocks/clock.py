import pygame
import datetime
import os

BASE_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(BASE_DIR, "images")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Подберите эти координаты под вашу картинку clocks.png
LEFT_SHOULDER = (240, 330)   # Левое плечо — секундная стрелка
RIGHT_SHOULDER = (300, 400)  # Правое плечо — минутная стрелка

def load_images():
    clock_img = pygame.image.load(os.path.join(IMAGES_DIR, "clocks.png")).convert_alpha()
    left_hand_img = pygame.image.load(os.path.join(IMAGES_DIR, "left_hand.png")).convert_alpha()
    right_hand_img = pygame.image.load(os.path.join(IMAGES_DIR, "right_hand.png")).convert_alpha()

    clock_img = pygame.transform.scale(clock_img, (600, 600))
    left_hand_img = pygame.transform.scale(left_hand_img, (120, 180))
    right_hand_img = pygame.transform.scale(right_hand_img, (120, 180))

    return clock_img, left_hand_img, right_hand_img

def draw_rotated_hand(screen, image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, -angle)
    w, h = rotated_image.get_size()

    # Точка вращения — НИЗ картинки (конец чёрной ручки)
    new_x = pivot[0] - w // 2
    new_y = pivot[1] - h+5

    screen.blit(rotated_image, (new_x, new_y))

def draw_clock(screen, font, clock_img, left_hand, right_hand):
    now = datetime.datetime.now()
    minute = now.minute
    second = now.second

    minute_angle = minute * 6
    second_angle = second * 6

    screen.fill(WHITE)
    screen.blit(clock_img, clock_img.get_rect(center=(300, 300)))
    draw_rotated_hand(screen, left_hand, second_angle, LEFT_SHOULDER)
    draw_rotated_hand(screen, right_hand, minute_angle, RIGHT_SHOULDER)

    text = font.render(now.strftime("%M:%S"), True, BLACK)
    screen.blit(text, text.get_rect(center=(300, 580)))