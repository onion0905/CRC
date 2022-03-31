#!/usr/bin/env python3
import pygame
import time

from pygame import draw
pygame.init()

mode = "normal" # "normal" or "hard"
drop_before_arrive = 0.8
pixel_per_second = 565 / drop_before_arrive


# Screen
wn = pygame.display.set_mode((800 ,600))
pygame.display.set_caption("Is Mayonnaise an Instrument?")
mayo = pygame.image.load("images\mayo.webp")
mayo.convert()
pygame.display.set_icon(mayo)

# Back Ground
start_menu = pygame.image.load("images\patrick_mayo.jpg")
start_menu.convert()
start_menu = pygame.transform.scale(start_menu, (800, 600))
start_button = pygame.image.load("images\start_button.png")
start_button.convert()
start_button = pygame.transform.scale(start_button, (200, 100))
mayo = pygame.transform.rotate(mayo, 90)
mayo = pygame.transform.scale(mayo, (100, 100))

 
# Objects
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

# files
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

# Functions
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
    pygame.draw.rect(wn, (107, 186, 241), white_back)
    pygame.draw.rect(wn, (255, 255, 0), border_left_line)
    pygame.draw.rect(wn, (255, 255, 0), border_right_line)
    
    pygame.draw.line(wn, (255, 255, 255), (275, 0),(275, 600))
    pygame.draw.line(wn, (255, 255, 255), (400, 0),(400, 600))
    pygame.draw.line(wn, (255, 255, 255), (525, 0),(525, 600))
    
    pygame.draw.line(wn, (100, 100, 100), (150, 500),(650, 500))
    pygame.draw.line(wn, (100, 100, 100), (150, 530),(650, 530))



# Main process
def main():
    pygame.init()
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
        now_time = time.time()
        if not started:
            start_time = now_time
        time_pass = float(now_time - start_time)
        time_pass = round(time_pass, 4)
        # background displaying
        if back:
            draw_back()
        else:
            wn.blit(start_menu, (0, 0))
            wn.blit(start_button, (370, 70))
            if mouse == "down":
                if mouse_pos[0] > 300 and mouse_pos[0] < 500 and mouse_pos[1] > 100 and mouse_pos[1] < 400:
                    back = 1
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.play()
                    started = True
                    start_time = time.time()

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
            pygame.draw.rect(wn, (99, 170, 219), display_pressed1)
        if not keys[pygame.K_d]:
            prev_key[0] = 0
        if keys[pygame.K_f]:
            pygame.draw.rect(wn, (99, 170, 219), display_pressed2)
        if not keys[pygame.K_f]:
            prev_key[1] = 0
        if keys[pygame.K_j]:
            pygame.draw.rect(wn, (99, 170, 219), display_pressed3)
        if not keys[pygame.K_j]:
            prev_key[2] = 0
        if keys[pygame.K_k]:
            pygame.draw.rect(wn, (99, 170, 219), display_pressed4)
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
                    wn.blit(mayo, (showing_array[i][1], showing_array[i][2]))

        
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
        now_end_time = time.time()
        now_end_time = round(now_end_time, 4)
        time_loop = now_end_time - now_time
        if time_loop < 0.001 and showing_array:
            time.sleep(0.001-time_loop)
    if time_pass > 108:
        running = False

main()
pygame.quit()