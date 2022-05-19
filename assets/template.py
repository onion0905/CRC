import pygame
from pygame import mixer
import subprocess


# intialize
pygame.init()

# set screen
screen = pygame.display.set_mode((1280, 720))
print(pygame.FULLSCREEN)

# background
# frame = pygame.transform.scale(frame, (1200, 800))

# Title and Icon //Skyclick
pygame.display.set_caption("CRC")
# icon = pygame.image.load("images/spaceship.png")
# pygame.display.set_icon(icon)

# Objects
sure_to_exit = pygame.image.load("images\sure_to_exit.png")
plot_2_0 = pygame.image.load("images\plot\plot_2_0.png")
# Game Loop
running = True
mouse = ""
x = 0
background = sure_to_exit
while running:
    # Basic Info
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    # set RGB
    screen.fill((0, 0, 0))

    # background fill
    screen.blit(background, (100, 40))
    screen.blit(plot_2_0, (-300, -200))

    # quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = "down"
            print(x)
        if event.type != pygame.MOUSEBUTTONDOWN:
            mouse = ""

    pygame.display.update()
