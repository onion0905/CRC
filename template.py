import pygame
from pygame import mixer
import subprocess


# intialize
pygame.init()

# set screen
screen = pygame.display.set_mode((800, 600))
print(pygame.FULLSCREEN)

# background
floor_1_image = pygame.image.load("CRC\images\\1F.png")
frame = pygame.image.load("CRC\images\hsryr.png")
# frame = pygame.transform.scale(frame, (1200, 800))

# Title and Icon //Skyclick
pygame.display.set_caption("CRC")
# icon = pygame.image.load("images/spaceship.png")
# pygame.display.set_icon(icon)

# Objects
quit_icon = pygame.image.load("CRC\images\\quit2.jpg")

# Game Loop
running = True
mouse = ""
x = 0
background = frame
while running:
    # Basic Info
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    # set RGB
    screen.fill((0, 0, 0))

    # background fill
    screen.blit(background, (0, 0))

    # quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = "down"
            subprocess.run("./test.exe")
            print(x)
        if event.type != pygame.MOUSEBUTTONDOWN:
            mouse = ""

    pygame.display.update()
