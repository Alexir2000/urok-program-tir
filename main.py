import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption(" Игра ТИР")

icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

targer_img = pygame.image.load("img/target_img.png")
targer_width = 50
targer_height = 50

target_x = random.randint(0,SCREEN_WIDTH - targer_width)
target_y = random.randint(0,SCREEN_HEIGHT - targer_height)

color = (random.randint(0,255), random.randint(0,255),random.randint(0,255))

running = true

while running:
    pass

pygame.quit()

