#!/usr/bin/env python3
import pygame
import time

# intialize
pygame.init()

# Global Variable
display_ratio = 2 # (640 * ratio, 360 * ratio)
running = True
mouse = ""
scene_x = -5
player_x = 320 * display_ratio - 70
time_frame = 0
control = 0
ex_control = control

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
player_left0 = pygame.image.load("images\\player_left0.png")
player_left1 = pygame.image.load("images\\player_left1.png")
player_left2 = pygame.image.load("images\\player_left2.png")
player_right0 = pygame.image.load("images\\player_right0.png")
player_right1 = pygame.image.load("images\\player_right1.png")
player_right2 = pygame.image.load("images\\player_right2.png")
player_front = pygame.transform.scale(player_front, (140, 196)) # 450 * 11/38 * display_ratio
player_left0 = pygame.transform.scale(player_left0, (130, 196))
player_left1 = pygame.transform.scale(player_left1, (130, 196))
player_left2 = pygame.transform.scale(player_left2, (130, 196))
player_right0 = pygame.transform.scale(player_right0, (130, 196))
player_right1 = pygame.transform.scale(player_right1, (130, 196))
player_right2 = pygame.transform.scale(player_right2, (130, 196))
player_images = [[player_front], [player_left0, player_left1, player_left2], [player_right0, player_right1, player_right2]]



# Functions
def control_flow(cur_control, started):
    if cur_control == -1:
        return -1
    if mouse == "down":
        return 1
    elif not started:
        return 0
    else:
        return cur_control
    

def sure_to_quit(ex_control):
    global running
    global control
    if control == -1:
        if mouse_pos[0] > 592 and mouse_pos[0] < 778 \
            and mouse_pos[1] > 480 and mouse_pos[1] < 555 and mouse == "down":
            running = False
        elif mouse_pos[0] > 850 and mouse_pos[0] < 1033 \
            and mouse_pos[1] > 480 and mouse_pos[1] < 555 and mouse == "down":
            control = ex_control
    


def check_quit(mouse_pos): # 0 for running, 1 for breaking
    global running
    global control
    if mouse_pos[0] > 570 * display_ratio and mouse_pos[0] < 630 * display_ratio \
        and mouse_pos[1] > 10 * display_ratio and mouse_pos[1] < 34 * display_ratio:
        # running = False
        control = -1
    else:
        running = True


def background_display(control, scene, scene_x):
    screen.fill((0, 0, 0))
    if control == -1:
        screen.blit(sure_to_quit_image, (100, 40))
    elif control == 0:
        screen.blit(scene, (0, 0))
    else:
        screen.blit(scene, (scene_x, 0))
    screen.blit(quit_icon, (570 * display_ratio, 10 * display_ratio))


def player_display(control, player_x, time_frame):
    if keys[pygame.K_d]:
        side = 2
    elif keys[pygame.K_a]:
        side = 1
    else:
        side = 0
    if side == 0:
        feet = 0
    elif time_frame < 10:
        feet = 1
    else:
        feet = 2
    player = player_images[side][feet]
    if control > 0:
        screen.blit(player, (player_x, 360))


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
started = 0
while running:
    # Basic Info
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    scroll_walk()
    pygame_event_response(mouse_pos)
    time_frame = (time_frame + 1) % 20
    control = control_flow(control, started)
    if control == -1:
        sure_to_quit(ex_control)
    started = control
    # background fill
    background_display(control, background_paper[control], scene_x)
    player_display(control, player_x, time_frame)
    pygame.display.update()
