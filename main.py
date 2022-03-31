#!/usr/bin/env python3
import pygame
from time import time, sleep

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


# Mayonaise Game #54 ~ #263
mode = "normal" # "normal" or "hard"
drop_before_arrive = 0.8
pixel_per_second = 565 / drop_before_arrive

mayo = pygame.image.load("images\mayo.webp")
mayo.convert()
start_menu = pygame.image.load("images\patrick_mayo.jpg")
start_menu.convert()
start_menu = pygame.transform.scale(start_menu, (800, 600))
start_button = pygame.image.load("images\start_button.png")
start_button.convert()
start_button = pygame.transform.scale(start_button, (200, 100))
mayo = pygame.transform.rotate(mayo, 90)
mayo = pygame.transform.scale(mayo, (100, 100))

slot = (125, 30)
rect = pygame.Rect(200, 0, 10, 600)
white_back = pygame.Rect(0, 0, 800, 600)
border_left_line = pygame.Rect(140, 0, 10, 600)
border_right_line = pygame.Rect(650, 0, 10, 600)
display_pressed1 = pygame.Rect(150, 500, slot[0], slot[1])
display_pressed2 = pygame.Rect(275, 500, slot[0], slot[1])
display_pressed3 = pygame.Rect(400, 500, slot[0], slot[1])
display_pressed4 = pygame.Rect(525, 500, slot[0], slot[1])
music = "images\\ver.hard.mp3"
track = pygame.mixer.music.load(music)

times_arrive = []
times_drop = []
notes = []
note_dict = {64:0, 192:1, 320:2, 448:3}
with open(f"note_and_time\\times_{mode}.txt", "r") as time_f:
    for i in time_f:
        i = int(i)
        i /= 1000
        i = round(i, 4)
        times_arrive.append(i)

with open(f"note_and_time\\notes_{mode}.txt", "r") as note_f:
    for i in note_f:
        i = int(i)
        i = note_dict[i]
        notes.append(i)

for i in times_arrive:
    i -= drop_before_arrive # dropping rate
    i = round(i, 4)
    times_drop.append(i)

locations = [160, 285, 410, 535]
def check_dy(now_time, drop_time, cord_y):
    p = now_time - drop_time
    return pixel_per_second * p - (cord_y+60)

def check_remove(time_pass, showing_array_i, prev_key, block):
    block_check = showing_array_i[4] == block
    cord_y_check = showing_array_i[2] <= 800 and showing_array_i[2] >= 400 # 500, 430
    prev_check = prev_key == 0

    time_check = abs(time_pass - showing_array_i[3]) <= 0.1

    return block_check and time_check and prev_check

def draw_back():
    pygame.draw.rect(screen, (107, 186, 241), white_back)
    pygame.draw.rect(screen, (255, 255, 0), border_left_line)
    pygame.draw.rect(screen, (255, 255, 0), border_right_line)
    
    pygame.draw.line(screen, (255, 255, 255), (275, 0),(275, 600))
    pygame.draw.line(screen, (255, 255, 255), (400, 0),(400, 600))
    pygame.draw.line(screen, (255, 255, 255), (525, 0),(525, 600))
    
    pygame.draw.line(screen, (100, 100, 100), (150, 500),(650, 500))
    pygame.draw.line(screen, (100, 100, 100), (150, 530),(650, 530))

def mayo_main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    running = True
    back = 0
    mouse = ""
    pointer = 0
    start_time = 0
    started = False
    ended = False
    showing_array = []
    tapping_array = []
    prev_key = [0, 0, 0, 0] # d f j k
    time_pass = 0
    combo = 0
    note_now = 0
    end_cnt = 0
    while running:
        mouse_pos = pygame.mouse.get_pos()
        now_time = time()
        if not started:
            start_time = now_time
        time_pass = float(now_time - start_time)
        time_pass = round(time_pass, 4)
        # background displaying
        if back:
            draw_back()
        else:
            screen.blit(start_menu, (0, 0))
            screen.blit(start_button, (370, 70))
            if mouse == "down":
                if mouse_pos[0] > 300 and mouse_pos[0] < 500 and mouse_pos[1] > 100 and mouse_pos[1] < 400:
                    back = 1
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.play()
                    started = True
                    start_time = time()

        # pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = "down"
                print(mouse)
            if event.type != pygame.MOUSEBUTTONDOWN:
                mouse = ""

        # pressed key displaying
        keys = pygame.key.get_pressed()
        for i in range(len(showing_array)):
            In = True
            if i <= len(showing_array) - 1 and check_remove(time_pass, showing_array[i], prev_key[showing_array[i][4]], 0) \
                and keys[pygame.K_d]:
                showing_array[i][1] = 2000
                showing_array[i][2] = 2000
                showing_array[i][5] = 1
            if i <= len(showing_array) - 1 and check_remove(time_pass, showing_array[i], prev_key[showing_array[i][4]], 1) \
                and keys[pygame.K_f]:
                showing_array[i][1] = 2000
                showing_array[i][2] = 2000
                showing_array[i][5] = 1
            if i <= len(showing_array) - 1 and check_remove(time_pass, showing_array[i], prev_key[showing_array[i][4]], 2) \
                and keys[pygame.K_j]:
                showing_array[i][1] = 2000
                showing_array[i][2] = 2000
                showing_array[i][5] = 1
            if i <= len(showing_array) - 1 and check_remove(time_pass, showing_array[i], prev_key[showing_array[i][4]], 3) \
                and keys[pygame.K_k]:
                showing_array[i][1] = 2000
                showing_array[i][2] = 2000
                showing_array[i][5] = 1
        if keys[pygame.K_d]:
            pygame.draw.rect(screen, (99, 170, 219), display_pressed1)
        if not keys[pygame.K_d]:
            prev_key[0] = 0
        if keys[pygame.K_f]:
            pygame.draw.rect(screen, (99, 170, 219), display_pressed2)
        if not keys[pygame.K_f]:
            prev_key[1] = 0
        if keys[pygame.K_j]:
            pygame.draw.rect(screen, (99, 170, 219), display_pressed3)
        if not keys[pygame.K_j]:
            prev_key[2] = 0
        if keys[pygame.K_k]:
            pygame.draw.rect(screen, (99, 170, 219), display_pressed4)
        if not keys[pygame.K_k]:
            prev_key[3] = 0
        while pointer < len(times_drop) and time_pass <= (times_drop[pointer])+0.1 and time_pass >= (times_drop[pointer])-0.1 and not ended:
            data_array = []
            data_array = [times_drop[pointer], locations[notes[pointer]], -100, times_arrive[pointer], notes[pointer], 0] # the last one is for combo counting
            showing_array.append(data_array)
            pointer += 1
            if pointer > len(times_drop):
                ended = True

        
        showing_pointer = 0
        for i in range(showing_pointer, len(showing_array)):
            if i == len(showing_array):
                break
            elif showing_array[i][2] > 600 or showing_array[i][1] > 800:
                continue
            else:
                dy = check_dy(time_pass, showing_array[i][0], showing_array[i][2])
                showing_array[i][2] += dy
                if showing_array[i][1] > 800:
                    showing_pointer += 1
                elif showing_array[i][2] > 600:
                    showing_pointer += 1
                elif showing_array[i][1] < 800:
                    screen.blit(mayo, (showing_array[i][1], showing_array[i][2]))

        
        for i in range(len(times_arrive)):
            if time_pass >= times_arrive[i]:
                note_now = i

        for i in range(note_now+1):
            if i < len(showing_array):
                if showing_array[i][5]:
                    combo += 1
                else:
                    combo = 0

        combo = 0
        pygame.display.update()
        now_end_time = time()
        now_end_time = round(now_end_time, 4)
        time_loop = now_end_time - now_time
        if time_loop < 0.001 and showing_array:
            sleep(0.001-time_loop)
        if time_pass > 10:
            break
    return

# Functions
def control_flow(cur_control, started):
    if cur_control == -1:
        return -1
    elif started == 0 and mouse == "down":
        return 1
    elif not started:
        return 0
    elif cur_control == 1: # and tp
        # call story 1
        # call dia 1
        # call battle 1
        return 4
    # elif cur_control == 4: # and tp

    # else:
    #     return cur_control
    

def sure_to_quit(ex_control):
    global running
    global control
    global screen
    mayo_main()
    control = ex_control
    screen = pygame.display.set_mode((640 * display_ratio, 360 * display_ratio))
    return
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
            check_quit(mouse_pos)
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
    if control != -1:
        ex_control = control
    if control == -1:
        sure_to_quit(ex_control)
    started = control
    # background fill
    background_display(control, background_paper[control], scene_x)
    player_display(control, player_x, time_frame)
    pygame.display.update()
