#!/usr/bin/env python3
import pygame

# intialize
pygame.init()

# Global Variable
display_ratio = 2 # (640 * ratio, 360 * ratio)
running = True
mouse = ""
scene_x = -5
player_x = 320 * display_ratio - 70

# set screen
screen = pygame.display.set_mode((640 * display_ratio, 360 * display_ratio))

# background
cover_image = pygame.image.load("images\\cover_image.jpg")
floor_1_image = pygame.image.load("images\\1F.png")
frame = pygame.image.load("images\\example.png")
sure_to_quit_image = pygame.image.load("images\\sure_to_exit.png")
background_paper = [cover_image, floor_1_image]

# Title and Icon
pygame.display.set_caption("CRC")
logo = pygame.image.load("images/logo.jpg")
pygame.display.set_icon(logo)

# Objects
keys = []
quit_icon = pygame.image.load("images\\quit.png")
quit_icon = pygame.transform.scale(quit_icon, (60 * display_ratio, 24 * display_ratio))
player_front = pygame.image.load("images\\player_front.png")
player_left1 = pygame.image.load("images\\player_left0.png")
player_left1 = pygame.image.load("images\\player_left1.png")
player_left1 = pygame.image.load("images\\player_left2.png")
player_right0 = pygame.image.load("images\\player_right0.png")
player_right1 = pygame.image.load("images\\player_right1.png")
player_right2 = pygame.image.load("images\\player_right2.png")
player_front = pygame.transform.scale(player_front, (140, 196)) # 450 * 11/38 * display_ratio

# Functions
def control_flow(cur_control, started):
    if mouse == "down":
        return 1
    elif not started:
        return 0
    else:
        return cur_control
    

def sure_to_quit():
    while True:
        screen.blit(sure_to_quit_image, (100, 40))


def check_quit(mouse_pos): # 0 for running, 1 for breaking
    global running
    if mouse_pos[0] > 570 * display_ratio and mouse_pos[0] < 630 * display_ratio \
        and mouse_pos[1] > 10 * display_ratio and mouse_pos[1] < 34 * display_ratio:
        running = False
        # sure_to_quit()
    else:
        running = True


def background_display(control, scene, scene_x):
    screen.fill((0, 0, 0))
    if control == 0:
        screen.blit(scene, (0, 0))
    else:
        screen.blit(scene, (scene_x, 0))
    screen.blit(quit_icon, (570 * display_ratio, 10 * display_ratio))


def player_display(control, player_x):
    if control > 0:
        screen.blit(player_front, (player_x, 360))


def scroll_walk():
    global scene_x
    global player_x
    border_r = 2320 - 640 * display_ratio
    if keys[pygame.K_d]:
        if player_x + 10 <= 320 * display_ratio - 70:
            player_x += 10
        elif scene_x - 10 >= -border_r:
            scene_x -= 10
        elif player_x + 140 + 10 <= 640 * display_ratio:
            player_x += 10
    elif keys[pygame.K_a]:
        if player_x - 10 >= 320 * display_ratio - 70:
            player_x -= 10
        elif scene_x + 10 <= -5:
            scene_x += 10
        elif player_x - 10 >= 0:
            player_x -= 10


def pygame_event_response(mouse_pos):
    global running
    global mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = "down"
            print(mouse_pos)
            check_quit(mouse_pos)
        if event.type != pygame.MOUSEBUTTONDOWN:
            mouse = ""


# Game Loop
background = background_paper[0]
control = 1
started = 0
while running:
    # Basic Info
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    scroll_walk()
    pygame_event_response(mouse_pos)

    control = control_flow(control, started)
    started = control
    # background fill
    background_display(control, background_paper[control], scene_x)
    player_display(control, player_x)
    pygame.display.update()
