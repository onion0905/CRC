#!/usr/bin/env python3
from dis import dis
from pygame.display import set_mode, update, set_caption, set_icon, flip, init as dinit
from pygame.transform import scale, rotate
from pygame.image import load
from pygame.mixer import music
from pygame.draw import rect as draw_rect, line
from pygame import init, Rect, QUIT, MOUSEBUTTONDOWN, K_d, K_f, K_j, K_k, K_a, K_f, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_b
from pygame.mouse import get_pos
from pygame.key import get_pressed
from pygame.event import get
from time import time, sleep
from os import system
from subprocess import run as subrun
import tkinter as tk
import tkinter.messagebox as msg
import tkinter.font as tkFont

# intialize
init() # pygame.init()

# Global Variable
display_ratio = 2 # (640 * ratio, 360 * ratio)
speed = (display_ratio - 1) * 10
running = True
mouse = ""
scene_x = -5
player_x = 320 * display_ratio - 70
foxxy_x = player_x - 50 * display_ratio
time_frame = 0
control = 0
ex_control = control
started = 0
floor_passed = 1
floor4_entered = False
next_floor = 4
egg_frame = 0
egg_count = 0

# constant
chr_xpos = [220 * display_ratio, 110 * display_ratio, 300 * display_ratio]
chr_ypos = [180, 120, 180, 150, 150, 150] # [player, diangod, bright, foxxy, bamboo, fire]

# set screen
screen = set_mode((640 * display_ratio, 360 * display_ratio)) # pygame.display.set_mode()

# background
cover_image = load("images\\cover_image.png").convert_alpha() # pygame.image.load()
sure_to_quit_image = load("images\\sure_to_exit.png").convert_alpha()
floor_1_image = load("images\\floor\\1F.png").convert_alpha()
floor_2_image = load("images\\floor\\2F.png").convert_alpha()
floor_3_image = load("images\\floor\\3F.png").convert_alpha()
floor_4_image = load("images\\floor\\4F.png").convert_alpha()
Efoxxy_background = load("images\\Efoxxy.png").convert_alpha()
Hfoxxy_background = load("images\\Hfoxxy.png").convert_alpha()
arrow_down = load("images\\arrow_down.png").convert_alpha()
arrow_up = load("images\\arrow_up.png").convert_alpha()
classroom = load("images\\classroom.png").convert_alpha()
bamboo_forest = load("images\\bamboo_forest.png").convert_alpha()
floor_sign_12 = load("images\\1-2F.png").convert_alpha()
floor_sign_23 = load("images\\2-3F.jfif").convert_alpha()
floor_sign_34 = load("images\\3-4F.jfif").convert_alpha()
floor_sign_44 = load("images\\4-4F.jfif").convert_alpha()
warning_image = load("images\\warning.png").convert_alpha()
thank_list = load("images\\thank_list.png").convert_alpha()
arrow_down = scale(arrow_down, (60 * display_ratio, 40 * display_ratio))
arrow_up = scale(arrow_up, (60 * display_ratio, 40 * display_ratio))
floor_sign_12 = scale(floor_sign_12, (33 * display_ratio, 33 * display_ratio))
floor_sign_23 = scale(floor_sign_23, (33 * display_ratio, 33 * display_ratio))
floor_sign_34 = scale(floor_sign_34, (33 * display_ratio, 33 * display_ratio))
floor_sign_44 = scale(floor_sign_44, (33 * display_ratio, 33 * display_ratio))
if display_ratio != 3:
    cover_image = scale(cover_image, (640 * display_ratio, 360 * display_ratio))
    floor_1_image = scale(floor_1_image, (1153 * display_ratio, 360 * display_ratio))
    floor_2_image = scale(floor_2_image, (1153 * display_ratio, 360 * display_ratio))
    floor_3_image = scale(floor_3_image, (1153 * display_ratio, 360 * display_ratio))
    floor_4_image = scale(floor_4_image, (1153 * display_ratio, 360 * display_ratio))
    Efoxxy_background = scale(Efoxxy_background, (640 * display_ratio, 360 * display_ratio))
    Hfoxxy_background = scale(Hfoxxy_background, (640 * display_ratio, 360 * display_ratio))
    classroom = scale(classroom, (640 * display_ratio, 360 * display_ratio))
    bamboo_forest = scale(bamboo_forest, (640 * display_ratio, 360 * display_ratio))
    warning_image = scale(warning_image, (640 * display_ratio, 360 * display_ratio))
    thank_list = scale(thank_list, (640 * display_ratio, 3700 * display_ratio))
background_paper = [cover_image, floor_1_image, floor_2_image, floor_3_image, floor_4_image]


# Title and Icon
set_caption("CRC") # pygame.display.set_caption()
logo = load("images/logo.jpg") # pygame.image.load()
set_icon(logo) # pygame.display.set_icon

# Objects
keys = []
quit_icon = load("images\\quit.png").convert_alpha() # pygame.image.load()
quit_icon = scale(quit_icon, (60 * display_ratio, 24 * display_ratio)) # pygame.transform.scale

player_front = load("images\\8bit\\player_front.png").convert_alpha()
player_left0 = load("images\\8bit\\player_left0.png").convert_alpha()
player_left1 = load("images\\8bit\\player_left1.png").convert_alpha()
player_left2 = load("images\\8bit\\player_left2.png").convert_alpha()
player_right0 = load("images\\8bit\\player_right0.png").convert_alpha()
player_right1 = load("images\\8bit\\player_right1.png").convert_alpha()
player_right2 = load("images\\8bit\\player_right2.png").convert_alpha()
foxxy_left0 = load("images\\8bit\\foxxy_left0.png").convert_alpha()
foxxy_left1 = load("images\\8bit\\foxxy_left1.png").convert_alpha()
foxxy_right0 = load("images\\8bit\\foxxy_right0.png").convert_alpha()
foxxy_right1 = load("images\\8bit\\foxxy_right1.png").convert_alpha()
tp_point_image1 = load("images\\tp1.png").convert_alpha()
tp_point_image2 = load("images\\tp2.png").convert_alpha()
key_f = load("images\\key_f.png").convert_alpha()

player_front = scale(player_front, (70 * display_ratio, 98 * display_ratio)) # 450 * 11/38 * display_ratio
player_left0 = scale(player_left0, (65 * display_ratio, 98 * display_ratio))
player_left1 = scale(player_left1, (65 * display_ratio, 98 * display_ratio))
player_left2 = scale(player_left2, (65 * display_ratio, 98 * display_ratio))
player_right0 = scale(player_right0, (65 * display_ratio, 98 * display_ratio))
player_right1 = scale(player_right1, (65 * display_ratio, 98 * display_ratio))
player_right2 = scale(player_right2, (65 * display_ratio, 98 * display_ratio))
foxxy_left0 = scale(foxxy_left0, (65 * display_ratio, 98 * display_ratio))
foxxy_left1 = scale(foxxy_left1, (65 * display_ratio, 98 * display_ratio))
foxxy_right0 = scale(foxxy_right0, (65 * display_ratio, 98 * display_ratio))
foxxy_right1 = scale(foxxy_right1, (65 * display_ratio, 98 * display_ratio))
tp_point_image1 = scale(tp_point_image1, (100 * display_ratio, 100 * display_ratio))
tp_point_image2 = scale(tp_point_image2, (100 * display_ratio, 100 * display_ratio))
key_f = scale(key_f, (30 * display_ratio, 30 * display_ratio))

foxyy_8bit = load("images\\8bit\\Foxxy_8bit.png").convert_alpha()
bamboo_8bit = load("images\\8bit\\Bamboo_8bit.png").convert_alpha()
bright_8bit = load("images\\8bit\\Bright_8bit.png").convert_alpha()
dianGod_8bit = load("images\\8bit\\DianGod_8bit.png").convert_alpha()
fire_8bit = load("images\\8bit\\Fire_8bit.png").convert_alpha()

foxyy_8bit = scale(foxyy_8bit, (80 * display_ratio, 98 * display_ratio))
bamboo_8bit = scale(bamboo_8bit, (80 * display_ratio, 98 * display_ratio))
bright_8bit = scale(bright_8bit, (80 * display_ratio, 98 * display_ratio))
dianGod_8bit = scale(dianGod_8bit, (80 * display_ratio, 98 * display_ratio))
fire_8bit = scale(fire_8bit, (80 * display_ratio, 98 * display_ratio))

player_images = [[player_front], [player_left0, player_left1, player_left2], [player_right0, player_right1, player_right2]]
foxxy_images = [[foxyy_8bit], [foxxy_left0, foxxy_left1], [foxxy_right0, foxxy_right1]]
npc_images = [foxyy_8bit, foxyy_8bit, bright_8bit, bamboo_8bit, dianGod_8bit, fire_8bit]


# characters
player_0 = load("images\\character\\player\\player_0.png").convert_alpha()
player_1 = load("images\\character\\player\\player_1.png").convert_alpha()
player_2 = load("images\\character\\player\\player_2.png").convert_alpha()
bright_0 = load("images\\character\\bright\\bright_0.png").convert_alpha()
bright_1 = load("images\\character\\bright\\bright_1.png").convert_alpha()
bright_2 = load("images\\character\\bright\\bright_2.png").convert_alpha()
bright_3 = load("images\\character\\bright\\bright_3.png").convert_alpha()
bamboo_0 = load("images\\character\\bamboo\\bamboo_0.png").convert_alpha()
bamboo_1 = load("images\\character\\bamboo\\bamboo_1.png").convert_alpha()
bamboo_2 = load("images\\character\\bamboo\\bamboo_2.png").convert_alpha()
bamboo_3 = load("images\\character\\bamboo\\bamboo_3.png").convert_alpha()
diangod_0 = load("images\\character\\diangod\\diangod_0.png").convert_alpha()
diangod_1 = load("images\\character\\diangod\\diangod_1.png").convert_alpha()
diangod_2 = load("images\\character\\diangod\\diangod_2.png").convert_alpha()
fire_0 = load("images\\character\\fire\\fire_0.png").convert_alpha()
fire_1 = load("images\\character\\fire\\fire_1.png").convert_alpha()
fire_2 = load("images\\character\\fire\\fire_2.png").convert_alpha()
foxxy_0 = load("images\\character\\foxxy\\foxxy_0.png").convert_alpha()
foxxy_1 = load("images\\character\\foxxy\\foxxy_1.png").convert_alpha()
foxxy_2 = load("images\\character\\foxxy\\foxxy_2.png").convert_alpha()


player_0 = scale(player_0, (200 * display_ratio, 300 * display_ratio))
player_1 = scale(player_1, (200 * display_ratio, 300 * display_ratio))
player_2 = scale(player_2, (200 * display_ratio, 300 * display_ratio))
bright_0 = scale(bright_0, (200 * display_ratio, 300 * display_ratio))
bright_1 = scale(bright_1, (200 * display_ratio, 300 * display_ratio))
bright_2 = scale(bright_2, (200 * display_ratio, 300 * display_ratio))
bright_3 = scale(bright_3, (200 * display_ratio, 300 * display_ratio))
bamboo_0 = scale(bamboo_0, (297 * display_ratio, 310 * display_ratio))
bamboo_1 = scale(bamboo_1, (297 * display_ratio, 310 * display_ratio))
bamboo_2 = scale(bamboo_2, (297 * display_ratio, 310 * display_ratio))
bamboo_3 = scale(bamboo_3, (348 * display_ratio, 310 * display_ratio))
diangod_0 = scale(diangod_0, (277 * display_ratio, 320 * display_ratio))
diangod_1 = scale(diangod_1, (277 * display_ratio, 320 * display_ratio))
diangod_2 = scale(diangod_2, (277 * display_ratio, 320 * display_ratio))
fire_0 = scale(fire_0, (169 * display_ratio, 310 * display_ratio))
fire_1 = scale(fire_1, (169 * display_ratio, 310 * display_ratio))
fire_2 = scale(fire_2, (169 * display_ratio, 310 * display_ratio))
foxxy_0 = scale(foxxy_0, (290 * display_ratio, 310 * display_ratio))
foxxy_1 = scale(foxxy_1, (290 * display_ratio, 310 * display_ratio))
foxxy_2 = scale(foxxy_2, (290 * display_ratio, 310 * display_ratio))


# Mayonaise Game #54 ~ #279
mode = "normal"
drop_before_arrive = 0.8
pixel_per_second = 300 * display_ratio / drop_before_arrive

mayo = load("images\mayo.webp") # pygame.image.load()
mayo.convert()
start_menu = load("images\patrick_mayo.jpg")
start_menu.convert()
start_menu = scale(start_menu, (640 * display_ratio, 360 * display_ratio)) # pygame.transform.scale
start_button = load("images\start_button.png")
start_button.convert()
start_button = scale(start_button, (335, 140))
mayo = rotate(mayo, 90) # pygame.transform.rotate
mayo = scale(mayo, (100, 100))

slot = (125, 30)
rect = Rect(200, 0, 10, 600) # pygame.Rect()
white_back = Rect(0, 0, 640 * display_ratio, 360 * display_ratio)
border_left_line = Rect(230 * display_ratio, 0, 10, 360 * display_ratio)
border_right_line = Rect(230 * display_ratio + 510, 0, 10, 360 * display_ratio)
display_pressed1 = Rect(183 * display_ratio + 150, 300 * display_ratio, slot[0], slot[1])
display_pressed2 = Rect(183 * display_ratio + 275, 300 * display_ratio, slot[0], slot[1])
display_pressed3 = Rect(183 * display_ratio + 400, 300 * display_ratio, slot[0], slot[1])
display_pressed4 = Rect(183 * display_ratio + 525, 300 * display_ratio, slot[0], slot[1])
music_mp3 = "images\\ver.hard.mp3"
track = music.load(music_mp3) # pygame.mixer.music.load()

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

locations = [183 * display_ratio + 160, 183 * display_ratio + 285, 183 * display_ratio + 410, 183 * display_ratio + 535]
def check_dy(now_time, drop_time, cord_y):
    p = now_time - drop_time
    return pixel_per_second * p - (cord_y+60)

def check_remove(time_pass, showing_array_i, prev_key, block):
    block_check = showing_array_i[4] == block
    prev_check = prev_key == 0
    time_check = abs(time_pass - showing_array_i[3]) <= 0.1
    return block_check and time_check and prev_check

def draw_back():
    draw_rect(screen, (107, 186, 241), white_back) # pygame.draw.rect()
    draw_rect(screen, (255, 255, 0), border_left_line)
    draw_rect(screen, (255, 255, 0), border_right_line)
    # pygame.draw.line
    line(screen, (255, 255, 255), (183 * display_ratio + 275, 0),(183 * display_ratio + 275, 360 * display_ratio))
    line(screen, (255, 255, 255), (183 * display_ratio + 400, 0),(183 * display_ratio + 400, 360 * display_ratio))
    line(screen, (255, 255, 255), (183 * display_ratio + 525, 0),(183 * display_ratio + 525, 360 * display_ratio))
    
    line(screen, (100, 100, 100), (183 * display_ratio + 150, 300 * display_ratio),(183 * display_ratio + 650, 300 * display_ratio))
    line(screen, (100, 100, 100), (183 * display_ratio + 150, 300 * display_ratio + 30),(183 * display_ratio + 650, 300 * display_ratio + 30))


def mayo_main():
    global screen
    init() # pygame.init()
    screen = set_mode((640 * display_ratio, 360 * display_ratio)) # pygame.display.set_mode
    running = True
    back = 0
    mouse = ""
    pointer = 0
    start_time = 0
    started = False
    ended = False
    showing_array = []
    prev_key = [0, 0, 0, 0] # d f j k
    time_pass = 0
    combo = 0
    note_now = 0
    while running:
        mouse_pos = get_pos() # pygame.mouse.get_pos()
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
            screen.blit(start_button, (335 * display_ratio, 70 * display_ratio))
            if mouse == "down":
                if mouse_pos[0] > 335 * display_ratio and mouse_pos[0] < 335 * display_ratio + 335\
                    and mouse_pos[1] > 70 * display_ratio and mouse_pos[1] < 70 * display_ratio + 140:
                    back = 1
                    music.set_volume(0.1) # pygame.mixer.music.set_volume()
                    music.play() # pygame.mixer.music.play()
                    started = True
                    start_time = time()

        # pygame events
        for event in get(): # pygame.event.get()
            if event.type == QUIT: #pygame.QUIT
                running = False
            if event.type == MOUSEBUTTONDOWN: # pygame.MOUSEBUTTONDOWN
                mouse = "down"
                print(mouse)
            if event.type != MOUSEBUTTONDOWN:
                mouse = ""

        # pressed key displaying
        keys = get_pressed() # pygame.key.get_pressed()
        for i in range(len(showing_array)):
            if i <= len(showing_array) - 1 and check_remove(time_pass-0.1, showing_array[i], prev_key[showing_array[i][4]], 0) \
                and keys[K_d]: # pygame.K_d
                showing_array[i][1] = 2000
                showing_array[i][2] = 2000
                showing_array[i][5] = 1
            if i <= len(showing_array) - 1 and check_remove(time_pass-0.1, showing_array[i], prev_key[showing_array[i][4]], 1) \
                and keys[K_f]: # pygame.K_f
                showing_array[i][1] = 2000
                showing_array[i][2] = 2000
                showing_array[i][5] = 1
            if i <= len(showing_array) - 1 and check_remove(time_pass-0.1, showing_array[i], prev_key[showing_array[i][4]], 2) \
                and keys[K_j]: # pygame.K_j
                showing_array[i][1] = 2000
                showing_array[i][2] = 2000
                showing_array[i][5] = 1
            if i <= len(showing_array) - 1 and check_remove(time_pass-0.1, showing_array[i], prev_key[showing_array[i][4]], 3) \
                and keys[K_k]: # pygame.K_k
                showing_array[i][1] = 2000
                showing_array[i][2] = 2000
                showing_array[i][5] = 1
        if keys[K_d]:
            draw_rect(screen, (99, 170, 219), display_pressed1) # pygame.draw.rect()
        if not keys[K_d]:
            prev_key[0] = 0
        if keys[K_f]:
            draw_rect(screen, (99, 170, 219), display_pressed2)
        if not keys[K_f]:
            prev_key[1] = 0
        if keys[K_j]:
            draw_rect(screen, (99, 170, 219), display_pressed3)
        if not keys[K_j]:
            prev_key[2] = 0
        if keys[K_k]:
            draw_rect(screen, (99, 170, 219), display_pressed4)
        if not keys[K_k]:
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
            elif showing_array[i][2] > 360 * display_ratio or showing_array[i][1] > 1900:
                continue
            else:
                dy = check_dy(time_pass, showing_array[i][0], showing_array[i][2])
                showing_array[i][2] += dy
                if showing_array[i][1] > 1900:
                    showing_pointer += 1
                elif showing_array[i][2] > 360 * display_ratio:
                    showing_pointer += 1
                elif showing_array[i][1] < 1900:
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
        update() # pygame.display.update()
        now_end_time = time()
        now_end_time = round(now_end_time, 4)
        time_loop = now_end_time - now_time
        if time_loop < 0.001 and showing_array:
            sleep(0.001-time_loop)
        if time_pass > 10: # remember to change
            break
    screen = set_mode((640 * display_ratio, 360 * display_ratio))
    return


# GOD CLASS # 290 ~ # 774
class Plot :
    def plot_1(self):
        plot_1_0 = load("images\\plot\\plot_1_0.png")
        if display_ratio == 2:
            plot_1_0 = scale(plot_1_0, (1280, 720))
        # screen.blit(player_image, (0,0))
        screen.blit(plot_1_0, (0,0)) # 你不斷地往上方走，試圖找到光的來源。你走到了四樓，發現光來自電腦教室，於是你抱著好奇心走進裡面。進去後，你看到一位渾身散發著閃電的男子
        update()
        check_mouse()
        # # screen.blit(diangod_image, (0,0))
        # update()
        # check_mouse()
        # screen.blit(plot_1_1, (0,0)) # 進去後，你看到一位渾身散發著閃電的男子
        # update()
        # check_mouse()
    def plot_2(self):
        plot_2_0 = load("images\\plot\\plot_2_0.png")
        plot_2_1 = load("images\\plot\\plot_2_1.png")
        if display_ratio == 2:
            plot_2_0 = scale(plot_2_0, (1280, 720))
            plot_2_1 = scale(plot_2_1, (1280, 720))
        # screen.blit(player_image, (0,0))
        screen.blit(plot_2_0, (0,0)) # 雖然你落敗了，但這也挑起你對程式的興趣，眼看下一道閃電即將轟來，你連忙躲進旁邊的電梯裡。
        update()
        check_mouse()
        screen.blit(plot_2_1, (0,0)) # 你乘著電梯來到二樓，你看見二樓教室裡有位穿著如同電神小弟一般的不明男子。
        update()
        check_mouse()
    def plot_3(self):
        plot_3_0 = load("images\\plot\\plot_3_0.png")
        if display_ratio == 2:
            plot_3_0 = scale(plot_3_0, (1280, 720))
        screen.blit(plot_3_0, (0,0)) # 發現我們其實是自己人後，Bamboo向你道歉，並將出口恢復成原樣。於是你和foxyy最後終於到達四樓了，但是，在準備進入電腦教室前，突然有人從教室裡走出來，他是剛才電神旁的小弟。
        update()
        check_mouse()
    def plot_4(self):
        plot_4_0 = load("images\\plot\\plot_4_0.png")
        if display_ratio == 2:
            plot_4_0 = scale(plot_4_0, (1280, 720))
        screen.blit(plot_4_0, (0,0)) # 你不了解她說的意思，直到看見她手中的閃電，你才終於發現了異常。foxyy脱去女裝，周圍爆發出閃電
        update()
        check_mouse()
    def plot_5(self):
        plot_5_0 = load("images\\plot\\plot_5_0.png")
        if display_ratio == 2:
            plot_5_0 = scale(plot_5_0, (1280, 720))
        screen.blit(Hfoxxy_background, (0, 0))
        screen.blit(plot_5_0, (0,0)) # 之後，你成為了下一任電神，在你的帶領之下，組織不再繼續作亂，反而變成喜歡不斷的教導程式能力，培養人才的組織，這就是我們現在的社團—CRC電算社
        update()
        check_mouse()


class Dialogue :
    def dia_1(self):
        dia_1_0 = load("images\\dia\\dia_1\\dia_1_0.png")
        dia_1_1 = load("images\\dia\\dia_1\\dia_1_1.png")
        dia_1_2 = load("images\\dia\\dia_1\\dia_1_2.png")
        if display_ratio == 2:
            dia_1_0 = scale(dia_1_0, (1280, 720))
            dia_1_1 = scale(dia_1_1, (1280, 720))
            dia_1_2 = scale(dia_1_2, (1280, 720))
        
        story_backgroud()
        screen.blit(player_0, (chr_xpos[1], chr_ypos[0])) # 電神輕視表情
        screen.blit(diangod_0, (chr_xpos[2], chr_ypos[1]))
        screen.blit(dia_1_0, (0,0)) # 電神：「又有挑戰者了嗎？」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_1, (chr_xpos[1], chr_ypos[0])) # 電神輕視表情
        screen.blit(diangod_0, (chr_xpos[2], chr_ypos[1]))
        screen.blit(dia_1_1, (0,0)) # （你皺了皺眉，聽不太懂他的意思）
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_1, (chr_xpos[1], chr_ypos[0])) # 電神輕視表情
        screen.blit(diangod_1, (chr_xpos[2], chr_ypos[1]))
        screen.blit(dia_1_2, (0,0)) # 電神：「沒關係，準備被電爆吧。」
        update()
        check_mouse()


    def dia_2(self):
        dia_2_0 = load("images\\dia\\dia_2\\dia_2_0.png")
        dia_2_1 = load("images\\dia\\dia_2\\dia_2_1.png")
        dia_2_2 = load("images\\dia\\dia_2\\dia_2_2.png")
        dia_2_3 = load("images\\dia\\dia_2\\dia_2_3.png")
        if display_ratio == 2:
            dia_2_0 = scale(dia_2_0, (1280, 720))
            dia_2_1 = scale(dia_2_1, (1280, 720))
            dia_2_2 = scale(dia_2_2, (1280, 720))
            dia_2_3 = scale(dia_2_3, (1280, 720))
        
        story_backgroud()
        screen.blit(bright_0, (chr_xpos[0], chr_ypos[2]))
        screen.blit(dia_2_0, (0,0)) # Bright：「你剛剛和他戰鬥了吧！」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_0, (chr_xpos[0], chr_ypos[0]))
        screen.blit(dia_2_1, (0,0)) # 你：「他？指在四樓的那個閃電人嗎？」or 「對啊，他究竟是誰啊？」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_0, (chr_xpos[1], chr_ypos[0]))
        screen.blit(bright_0, (chr_xpos[2], chr_ypos[2]))
        screen.blit(dia_2_2, (0,0)) # Bright:「呵呵，他是《電神》是我們組織的統治者」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_0, (chr_xpos[0], chr_ypos[0]))
        screen.blit(dia_2_3, (0,0)) # 你：「組織？什麼組織」
        update()
        check_mouse()


    def dia_3(self):
        dia_3_0 = load("images\\dia\\dia_3\\dia_3_0.png")
        dia_3_1 = load("images\\dia\\dia_3\\dia_3_1.png")
        dia_3_2 = load("images\\dia\\dia_3\\dia_3_2.png")
        dia_3_3 = load("images\\dia\\dia_3\\dia_3_3.png")
        dia_3_4 = load("images\\dia\\dia_3\\dia_3_4.png")
        dia_3_5 = load("images\\dia\\dia_3\\dia_3_5.png")
        # dia_3_6 = load("images\\dia\\dia_3\\dia_3_6.png")
        if display_ratio == 2:
            dia_3_0 = scale(dia_3_0, (1280, 720))
            dia_3_1 = scale(dia_3_1, (1280, 720))
            dia_3_2 = scale(dia_3_2, (1280, 720))
            dia_3_3 = scale(dia_3_3, (1280, 720))
            dia_3_4 = scale(dia_3_4, (1280, 720))
            dia_3_5 = scale(dia_3_5, (1280, 720))
            # dia_3_6 = scale(dia_3_6, (1280, 720))
        
        story_backgroud()
        screen.blit(foxxy_0, (chr_xpos[0], chr_ypos[3])) # foxyy 開心表情
        screen.blit(dia_3_0, (0,0)) # foxyy：「我們是CRC！」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_0, (chr_xpos[1], chr_ypos[0])) # player 和 bright 若有所思
        screen.blit(bright_1, (chr_xpos[2], chr_ypos[2]))
        screen.blit(dia_3_1, (0,0)) # (看著突然出現的女子，你跟Bright都若有所思）
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_0, (chr_xpos[1], chr_ypos[0])) # player 和 bright 若有所思
        screen.blit(bright_1, (chr_xpos[2], chr_ypos[2]))
        screen.blit(dia_3_2, (0,0)) # 你：（怎麼突然有人冒出來）
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_0, (chr_xpos[1], chr_ypos[0])) # bright 驚嚇表情
        screen.blit(bright_2, (chr_xpos[2], chr_ypos[2]))
        screen.blit(dia_3_3, (0,0)) # Bright：（他…怎麼會出現在這裡）
        update()
        check_mouse()

        story_backgroud()
        screen.blit(foxxy_1, (chr_xpos[0], chr_ypos[3])) # foxyy 開心表情
        screen.blit(dia_3_4, (0,0)) # foxyy：「CRC，又稱為電算社，我們擁有能改變世界的電算之力！」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(foxxy_0, (chr_xpos[0], chr_ypos[3]))
        screen.blit(dia_3_5, (0,0)) # foxyy：「簡單來說，就是程式設計。如果精通這項能力，就會擁有很強大的力量，例如發射閃電之類的喔！」
        update()
        check_mouse()

        # screen.fill((0, 0, 0))
        # screen.blit(classroom, (0, 0))
        # screen.blit(player_2, (chr_xpos[1], chr_ypos[0])) # player 和 bright 開心表情
        # screen.blit(bright_0, (chr_xpos[2], chr_ypos[2]))
        # screen.blit(dia_3_6, (0,0)) # （你聽完後對程式擁有了更濃厚的興趣，同時Bright似乎也有意教導你）
        # update()
        # check_mouse()


    def dia_4(self):
        dia_4_0 = load("images\\dia\\dia_4\\dia_4_0.png")
        dia_4_1 = load("images\\dia\\dia_4\\dia_4_1.png")
        dia_4_2 = load("images\\dia\\dia_4\\dia_4_2.png")
        if display_ratio == 2:
            dia_4_0 = scale(dia_4_0, (1280, 720))
            dia_4_1 = scale(dia_4_1, (1280, 720))
            dia_4_2 = scale(dia_4_2, (1280, 720))

        story_backgroud()
        screen.blit(player_0, (chr_xpos[1], chr_ypos[0])) # bright 驚嚇表情
        screen.blit(bright_3, (chr_xpos[2], chr_ypos[2]))
        screen.blit(dia_4_0, (0,0)) # Bright：「我可是教導程式的高手呢！只要十分鐘，我便能把所有的基礎都教會你！」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_2, (chr_xpos[1], chr_ypos[0])) # foxyy：「人家也來幫你吧！」
        screen.blit(foxxy_1, (chr_xpos[2], chr_ypos[3]))
        screen.blit(dia_4_1, (0,0)) 
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_2, (chr_xpos[0], chr_ypos[0])) # player 安心表情
        screen.blit(dia_4_2, (0,0)) # （看來這裡還是有很多善良的人呢，你放心了許多）
        update()
        check_mouse()


    def dia_5(self):
        dia_5_0 = load("images\\dia\\dia_5\\dia_5_0.png")
        dia_5_1 = load("images\\dia\\dia_5\\dia_5_1.png")
        dia_5_2 = load("images\\dia\\dia_5\\dia_5_2.png")
        if display_ratio == 2:
            dia_5_0 = scale(dia_5_0, (1280, 720))
            dia_5_1 = scale(dia_5_1, (1280, 720))
            dia_5_2 = scale(dia_5_2, (1280, 720))
        
        story_backgroud()
        screen.blit(player_0, (chr_xpos[1], chr_ypos[0]))
        screen.blit(bright_0, (chr_xpos[2], chr_ypos[2]))
        screen.blit(dia_5_0, (0,0)) # （在Bright和foxyy的教導之下，你很快就學會基礎的程式設計，並感覺到有股電流在你的身體裡流竄）
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_2, (chr_xpos[1], chr_ypos[0]))
        screen.blit(bright_0, (chr_xpos[2], chr_ypos[2])) # bright 開心表情
        screen.blit(dia_5_1, (0,0)) # Bright：「學的這麼快，看來你擁有很強的潛力呢。不過，我能教的都教完了，如果你想學更多，就到三樓去找更多高手請教吧，但是要注意，有些人並不歡迎外人打擾。」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_2, (chr_xpos[1], chr_ypos[0]))
        screen.blit(foxxy_0, (chr_xpos[2], chr_ypos[3])) # foxyy 驚嚇表情
        screen.blit(dia_5_2, (0,0)) # foxyy：「放心，人家會陪著你上去~」
        update()
        check_mouse()


    def dia_6(self):
        dia_6_0 = load("images\\dia\\dia_6\\dia_6_0.png")
        dia_6_1 = load("images\\dia\\dia_6\\dia_6_1.png")
        dia_6_2 = load("images\\dia\\dia_6\\dia_6_2.png")
        dia_6_3 = load("images\\dia\\dia_6\\dia_6_3.png")
        dia_6_4 = load("images\\dia\\dia_6\\dia_6_4.png")
        dia_6_5 = load("images\\dia\\dia_6\\dia_6_5.png")
        dia_6_6 = load("images\\dia\\dia_6\\dia_6_6.png")
        dia_6_7 = load("images\\dia\\dia_6\\dia_6_7.png")
        dia_6_8 = load("images\\dia\\dia_6\\dia_6_8.png")
        dia_6_9 = load("images\\dia\\dia_6\\dia_6_9.png")
        dia_6_10 = load("images\\dia\\dia_6\\dia_6_10.png")
        dia_6_11 = load("images\\dia\\dia_6\\dia_6_11.png")
        dia_6_12 = load("images\\dia\\dia_6\\dia_6_12.png")
        if display_ratio == 2:
            dia_6_0 = scale(dia_6_0, (1280, 720))
            dia_6_1 = scale(dia_6_1, (1280, 720))
            dia_6_2 = scale(dia_6_2, (1280, 720))
            dia_6_3 = scale(dia_6_3, (1280, 720))
            dia_6_4 = scale(dia_6_4, (1280, 720))
            dia_6_5 = scale(dia_6_5, (1280, 720))
            dia_6_6 = scale(dia_6_6, (1280, 720))
            dia_6_7 = scale(dia_6_7, (1280, 720))
            dia_6_8 = scale(dia_6_8, (1280, 720))
            dia_6_9 = scale(dia_6_9, (1280, 720))
            dia_6_10 = scale(dia_6_10, (1280, 720))
            dia_6_11 = scale(dia_6_11, (1280, 720))
            dia_6_12 = scale(dia_6_12, (1280, 720))
        
        story_backgroud()
        screen.blit(dia_6_0, (0,0)) # （你和foxyy來到了三樓）
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_0, (chr_xpos[1], chr_ypos[0]))
        screen.blit(foxxy_1, (chr_xpos[2], chr_ypos[3]))
        screen.blit(dia_6_1, (0,0)) # foxyy：「我們去右邊的教室吧！」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(dia_6_2, (0,0)) # (一進去教室，你看到有名女子正坐在講桌電腦旁擦著手上的刀)
        update()
        check_mouse()

        story_backgroud()
        screen.blit(foxxy_1, (chr_xpos[0], chr_ypos[3])) # foxyy 普通表情
        screen.blit(dia_6_3, (0,0)) # foxyy:是學術組的Bamboo，看來真的遇到高手了
        update()
        check_mouse()

        story_backgroud()
        screen.blit(bamboo_0, (chr_xpos[0], chr_ypos[4])) # bamboo 殺氣臉
        screen.blit(dia_6_4, (0,0)) # (Bamboo望了你們一眼）
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_0, (chr_xpos[1], chr_ypos[0]))
        screen.blit(bamboo_1, (chr_xpos[2], chr_ypos[4]))
        screen.blit(dia_6_5, (0,0)) # Bamboo:「怎麼會有外人前來拜訪」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_2, (chr_xpos[0], chr_ypos[0])) # player 普通表情
        screen.blit(dia_6_6, (0,0)) # 你：「早安，為了雪恥，請教我更進階的程式以面對電神，請885」or「ㄜ...我來學精深的程式，助我打敗電神」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(bamboo_2, (chr_xpos[0], chr_ypos[4])) # bamboo 殺氣表情
        screen.blit(dia_6_7, (0,0)) # Bamboo:「聽你一說，你想請託我協助你們挑戰電神？所以你們其實是入侵者吧」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(foxxy_2, (chr_xpos[1], chr_ypos[3]))
        screen.blit(bamboo_3, (chr_xpos[2], chr_ypos[4]))
        screen.blit(dia_6_8, (0,0)) # （foxyy正想解釋，但Bamboo已經拔刀奔來）
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_1, (chr_xpos[1], chr_ypos[0]))
        screen.blit(bamboo_3, (chr_xpos[2], chr_ypos[4]))
        screen.blit(dia_6_9, (0,0)) # Bamboo:「沒想到你們竟能從電神手中逃過一劫，不過在下是不會放過任何入侵者的」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_0, (chr_xpos[1], chr_ypos[0]))
        screen.blit(foxxy_2, (chr_xpos[2], chr_ypos[3]))
        screen.blit(dia_6_10, (0,0)) # foxyy:「（指著門）快點離開，危險！」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(bamboo_2, (chr_xpos[0], chr_ypos[4])) # bamboo 殺氣表情
        screen.blit(dia_6_11, (0,0)) # Bamboo:「別想逃，”竹林叢生”」
        update()
        check_mouse()

        screen.blit(bamboo_forest, (0,0))
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_1, (chr_xpos[1], chr_ypos[0]))
        screen.blit(bamboo_3, (chr_xpos[2], chr_ypos[4]))
        screen.blit(bamboo_forest, (0,0))
        screen.blit(dia_6_12, (0,0)) # （門口前瞬間長出一堆竹子，賭住了唯一的出口，看來只能戰鬥了）
        update()
        check_mouse()


    def dia_7(self):
        dia_7_0 = load("images\\dia\\dia_7\\dia_7_0.png")
        dia_7_1 = load("images\\dia\\dia_7\\dia_7_1.png")
        dia_7_2 = load("images\\dia\\dia_7\\dia_7_2.png")
        dia_7_3 = load("images\\dia\\dia_7\\dia_7_3.png")
        dia_7_4 = load("images\\dia\\dia_7\\dia_7_4.png")
        dia_7_5 = load("images\\dia\\dia_7\\dia_7_5.png")
        dia_7_6 = load("images\\dia\\dia_7\\dia_7_6.png")
        dia_7_7 = load("images\\dia\\dia_7\\dia_7_7.png")
        dia_7_8 = load("images\\dia\\dia_7\\dia_7_8.png")
        dia_7_9 = load("images\\dia\\dia_7\\dia_7_9.png")
        dia_7_10 = load("images\\dia\\dia_7\\dia_7_10.png")
        dia_7_11 = load("images\\dia\\dia_7\\dia_7_11.png")
        if display_ratio == 2:
            dia_7_0 = scale(dia_7_0, (1280, 720))
            dia_7_1 = scale(dia_7_1, (1280, 720))
            dia_7_2 = scale(dia_7_2, (1280, 720))
            dia_7_3 = scale(dia_7_3, (1280, 720))
            dia_7_4 = scale(dia_7_4, (1280, 720))
            dia_7_5 = scale(dia_7_5, (1280, 720))
            dia_7_6 = scale(dia_7_6, (1280, 720))
            dia_7_7 = scale(dia_7_7, (1280, 720))
            dia_7_8 = scale(dia_7_8, (1280, 720))
            dia_7_9 = scale(dia_7_9, (1280, 720))
            dia_7_10 = scale(dia_7_10, (1280, 720))
            dia_7_11 = scale(dia_7_11, (1280, 720))
        
        story_backgroud()
        screen.blit(bamboo_1, (chr_xpos[0], chr_ypos[4])) # player 累 bamboo 憤怒表情
        screen.blit(dia_7_0, (0,0)) # （你不斷閃過Bamboo的斬擊，Bamboo開始感到心急）
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_1, (chr_xpos[1], chr_ypos[0]))
        screen.blit(bamboo_1, (chr_xpos[2], chr_ypos[4])) # bamboo 憤怒表情
        screen.blit(dia_7_1, (0,0)) # Bamboo:可惡，區區入侵者在下居然不能解決
        update()
        check_mouse()

        story_backgroud()
        screen.blit(dia_7_2, (0,0)) # Bamboo:《程式枷鎖》
        update()
        check_mouse()

        story_backgroud()
        # screen.blit(playerRRR_image, (0,0)) # player + 枷鎖
        screen.blit(dia_7_3, (0,0)) # （突然有一條寫滿程式的繩子將你綁住，使你無法動彈）
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_1, (chr_xpos[0], chr_ypos[0])) # player 問號表情
        screen.blit(dia_7_4, (0,0)) # 你：「這是什麼東西」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(foxxy_2, (chr_xpos[0], chr_ypos[3])) # foxyy 嚴肅表情
        screen.blit(dia_7_5, (0,0)) # foxyy:「程式枷鎖⋯⋯，除非你找出這程式的bug，否則這不會解開」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(player_1, (chr_xpos[1], chr_ypos[0]))
        screen.blit(bamboo_3, (chr_xpos[2], chr_ypos[4]))
        screen.blit(dia_7_6, (0,0)) # Bamboo：「這樣就結束了，接招吧《竹切斬》」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(bamboo_1, (chr_xpos[0], chr_ypos[4]))
        screen.blit(dia_7_7, (0,0)) # （強力的斬擊落下，劍氣所及之處煙霧四散）
        update()
        check_mouse()

        story_backgroud()
        screen.blit(bamboo_3, (chr_xpos[0], chr_ypos[4]))
        screen.blit(dia_7_8, (0,0)) # （待煙霧散去，Bam發現你們兩個都沒事）
        update()
        check_mouse()

        story_backgroud()
        screen.blit(foxxy_1, (chr_xpos[0], chr_ypos[3])) # foxyy 自豪表情
        screen.blit(dia_7_9, (0,0)) # foxyy:「這種程式，找出bug有什麼難的」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(bamboo_0, (chr_xpos[0], chr_ypos[4])) # bamboo 驚訝表情
        screen.blit(dia_7_10, (0,0)) # （Bamboo驚訝的看著foxyy，過了幾秒後發現原來foxyy其實是自己人）
        update()
        check_mouse()

        story_backgroud()
        screen.blit(foxxy_0, (chr_xpos[1], chr_ypos[3]))
        screen.blit(bamboo_0, (chr_xpos[2], chr_ypos[4]))
        screen.blit(dia_7_11, (0,0)) # Bamboo:原來是foxyy，這代表你不是入侵者吧
        update()
        check_mouse()


    def dia_8(self):
        dia_8_0 = load("images\\dia\\dia_8\\dia_8_0.png")
        dia_8_1 = load("images\\dia\\dia_8\\dia_8_1.png")
        if display_ratio == 2:
            dia_8_0 = scale(dia_8_0, (1280, 720))
            dia_8_1 = scale(dia_8_1, (1280, 720))
        
        story_backgroud()
        screen.blit(fire_0, (chr_xpos[0], chr_ypos[5])) # fire 輕視表情
        screen.blit(dia_8_0, (0,0)) # Fire:「你怎麼又上來了，還想再被電爆嗎？」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(fire_1, (chr_xpos[0], chr_ypos[5]))
        screen.blit(dia_8_1, (0,0)) # Fire:「以你這種程度，根本不用電神出馬，我一個人就能解決你了」
        update()
        check_mouse()


    def dia_9(self):
        dia_9_0 = load("images\\dia\\dia_9\\dia_9_0.png")
        if display_ratio == 2:
            dia_9_0 = scale(dia_9_0, (1280, 720))
        
        story_backgroud()
        screen.blit(fire_2, (chr_xpos[0], chr_ypos[5])) # fire 驚訝表情
        screen.blit(dia_9_0, (0,0)) # Fire:「沒想到你竟然能答出這些問題⋯，是我太大意了⋯⋯」
        update()
        check_mouse()


    def dia_10(self):
        dia_10_0 = load("images\\dia\\dia_10\\dia_10_0.png")
        dia_10_1 = load("images\\dia\\dia_10\\dia_10_1.png")
        dia_10_2 = load("images\\dia\\dia_10\\dia_10_2.png")
        dia_10_3 = load("images\\dia\\dia_10\\dia_10_3.png")
        dia_10_4 = load("images\\dia\\dia_10\\dia_10_4.png")
        if display_ratio == 2:
            dia_10_0 = scale(dia_10_0, (1280, 720))
            dia_10_1 = scale(dia_10_1, (1280, 720))
            dia_10_2 = scale(dia_10_2, (1280, 720))
            dia_10_3 = scale(dia_10_3, (1280, 720))
            dia_10_4 = scale(dia_10_4, (1280, 720))
        
        story_backgroud()
        screen.blit(player_1, (chr_xpos[0], chr_ypos[0]))
        screen.blit(dia_10_0, (0,0)) # （之後你走進教室，看見教室裡面只有foxyy一個人）
        update()
        check_mouse()
        
        story_backgroud()
        screen.blit(dia_10_1, (0,0)) # 你：「電神不在這裡嗎？」or「foxyy，電神在哪裡？」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(foxxy_1, (chr_xpos[0], chr_ypos[3])) # foxyy 普通表情
        screen.blit(dia_10_2, (0,0)) # foxyy:「電神？他現在正在這間教室裡啊」
        update()
        check_mouse()

        story_backgroud()
        screen.blit(Efoxxy_background, (0, 0))
        screen.blit(dia_10_3, (0,0)) # 你不了解她說的意思，直到看見她手中的閃電，你才終於發現了異常。foxyy脱去女裝，周圍爆發出閃電
        update()
        check_mouse()

        story_backgroud()
        screen.blit(Efoxxy_background, (0, 0))
        screen.blit(dia_10_4, (0,0)) # foxyy:「好了，你的實力已經增強不少了，真是另人期待，開始最後的戰鬥吧！」
        update()
        check_mouse()


    def dia_11(self):
        dia_11_0 = load("images\\dia\\dia_11\\dia_11_0.png")
        dia_11_1 = load("images\\dia\\dia_11\\dia_11_1.png")
        dia_11_2 = load("images\\dia\\dia_11\\dia_11_2.png")
        dia_11_3 = load("images\\dia\\dia_11\\dia_11_3.png")
        if display_ratio == 2:
            dia_11_0 = scale(dia_11_0, (1280, 720))
            dia_11_1 = scale(dia_11_1, (1280, 720))
            dia_11_2 = scale(dia_11_2, (1280, 720))
            dia_11_3 = scale(dia_11_3, (1280, 720))
        
        story_backgroud()
        screen.blit(diangod_2, (chr_xpos[0], chr_ypos[1])) # foxyy 倒地
        screen.blit(dia_11_0, (0,0)) # （你歷經了千辛萬苦，終於在最後一刻找到機會電爆foxyy，foxyy倒地不起）
        update()
        check_mouse()

        story_backgroud()
        screen.blit(diangod_2, (chr_xpos[0], chr_ypos[1]))
        screen.blit(dia_11_1, (0,0)) # foxyy:我⋯竟然輸了
        update()
        check_mouse()
        screen.blit(classroom, (0, 0))

        story_backgroud()
        screen.blit(Hfoxxy_background, (0, 0)) # foxyy 欣慰表情
        screen.blit(dia_11_2, (0,0)) # （foxyy臉上並未出現任何不甘和憤怒，反而欣慰的笑了）
        update()
        check_mouse()

        story_backgroud()
        screen.blit(Hfoxxy_background, (0, 0))
        screen.blit(dia_11_3, (0,0)) # foxyy:「我就知道你有這個潛力，當初放你一馬並教導你，就是為了激發深藏在你體內的電算之力，CRC之後就交給你了」
        update()
        check_mouse()


def question1():
    base = tk.Tk()
    base.wm_attributes('-topmost',1)
    base.title("問題一")
    t = '''
    電神看著你狂妄地笑著，心想著又有一個店小二來送菜了。
    現在他的助手突然帶著重要的訊息前來，他不想讓你聽到內容
    但你擋在電神面前，以致於助手無法傳遞訊息。
    於是，他決定使用「雜湊」來產生一串你聽不懂的數字，再請電神用已經講好的方法來解密。
    問題是，雜湊並非一個簡單的技巧，而助手因為不夠電而忘了如何雜湊
    所以他對你提出一個條件：如果你幫他雜湊並把訊息傳遞給電神，那他就可以幫你講幾句好話。
    好奇的你心想，這是什麼簡單的東西，雜湊我幼稚園就會了！
    現在請你找到兩個好的常數雜湊該訊息，讓電神解密時不會發生碰撞或其他錯誤。
    1. p = 0, m = 1
    2. p = 1, m = 0
    3. p = 1560, m = 1563
    4. p = 1570, m = 1576
    5. p = 1559, m = 1581
    6. p = 1567, m = 1571
    7. 開玩笑的，幼稚園怎麼可能會這種東西，我開玩笑的啦，放我一馬
    '''
    base.geometry("600x330")
    def false():
        false_msg = '''
        電神先是冷笑一聲，緊接著是更加狂妄的大笑：
        「哼哈哈哈哈你答錯囉，準備接受電神的制裁和助手的怒火吧！」
        '''
        msg.showerror("完蛋ㄌ", false_msg)
        base.destroy()

    def correct():
        correct_msg = '''
        助手用欽慕的眼神望著你，開始對著你瘋狂地膜拜，
        但此舉卻惹怒了在一旁的電神。電神怒吼：
        「你這個沒用的東西，上禮拜社課才剛教完的東西，現在就忘記！？
        還要請一個外人來幫忙！？我看你是沒救了，快給我從電算社滾出去！」
        接著發射一道超強的電流，直接一擊斃命，把他的助手電爛了。
        電神上下打量著你，竟然能解出這種難題，
        不過後來想一想，你肯定是靠賽嘛，怎麼可能有人會這種困難的知識！
        電神又露出了他詭異唯妙的笑容......'''
        msg.showinfo("完蛋ㄌ", correct_msg)
        base.destroy()

    def main():
        tk.Label(base, text=t).grid(row = 0)
        for i in range(7):
            if i == 5:
                tk.Button(base, text = str(i+1), command=correct).place(x = 150 + 50*i, y = 270)
            else:
                tk.Button(base, text = str(i+1), command=false).place(x = 150 + 50*i, y = 270)
        base.mainloop()

    main()


class Question2_1():
    def __init__(self):
        self.base = tk.Tk()
        self.base.wm_attributes('-topmost',1)
        self.base.title("問題二")
        self.text = tk.StringVar()
        self.base.geometry("800x650")
        self.proc = 0
        self.choose = False
        self.t = '''
Foxxy 帶著你進入奇幻的程式世界，準備教授你程式語言的基礎。一起來看他精心精簡過的講義吧:D
我們今天要教的程式語言是 C++！它的基礎語法非常簡單，那我們先來示範如何定義變數：
'''
        self.op1text = '''
int a;
int b;
std::cout << a + b << std::endl;
'''

        self.op2text = '''
int a = 3;
int b = a + a;
cout<< b << endl;
'''

        self.op3text = '''
int a = 10 * 100;
std::cout << a << std::endl;
'''
        self.op4text = '''
int a = 3
std::cout << a << std::endl
'''
        self.text.set(self.t)
        self.label = tk.Label(self.base, textvariable=self.text)
        self.button = tk.Button(self.base, text = "下一頁", command=self.changeText)
        self.button.place(x = 360, y = 20)
        self.label.place(x = 120, y = 50)
        self.base.mainloop()
    def changeText(self):
        self.proc += 1
        self.new_script = self.t
        if self.proc == 1:
            msg.showinfo("變數", "int a = 0;")
            self.new_script += '''
int a = 0;
這行程式非常的簡單。int 是 integer 的縮寫，代表這個變數是整數型別，而 a 則是它的名字。
一開始我們給他 0 這個值。記得 C++ 的每行程式碼後面都要加分號喔！
'''
        elif self.proc == 2:
            msg.showinfo("變數", "int b = a + 1")
            self.new_script += '''
int b = a + 1

那這行也是一樣，定義一個整數 b，賦予它 a + 1 的值。
最後我們來輸出他們的值吧！
'''
        elif self.proc == 3:
            msg.showinfo("輸出", "std::cout << a << b << std::endl;")
            self.new_script += '''
std::cout << a << b << std::endl;
這行比較複雜一點。std 是 C++ 最常用的物件、函式和型別的集合
而標準輸出函式 cout 和換行 endl 則是 std 旗下的東西
所以前面要加上 std:: ，編譯器才認得這些東西喔！
輸出變數的方法就是在變數前輸入 << 就可以輸出了。是不是很方便？            
'''
        elif self.proc == 4:
            msg.showinfo("執行結果", "執行結果：01")
            self.new_script += '''
執行結果：01

可是這不是我們想要的耶，我想要把兩個變數分開輸出，不要黏在一起！
那我們稍微修改一下程式碼，加個空白看看：
'''
        elif self.proc == 5:
            msg.showinfo("輸出", "std::cout << a << ' ' << b << std::endl;")
            self.new_script += '''
std::cout << a << "\x20" << b << std::endl;
執行結果：0  1


恭喜你成功學習了程式設計的基礎知識！接下來我們來做一些練習：
Foxyy 看到你昏昏欲睡的表情，決定來給你實際操作一下程式設計。
請試著用講義中學到的知識幫 foxxy debug 一下吧！請問下列哪一個程式片段沒有錯誤？
'''
            self.choose = True
            tk.Button(self.base, text = self.op1text, command=self.op1).place(x = 50, y = 550)
            tk.Button(self.base, text = self.op2text, command=self.op2).place(x = 250, y = 550)
            tk.Button(self.base, text = self.op3text, command=self.op3).place(x = 390, y = 550)
            tk.Button(self.base, text = self.op4text, command=self.op4).place(x = 570, y = 550)

        self.t = self.new_script
        self.text.set(self.t)

    def op1(self):
        msg.showerror("哎呀錯ㄌ", "看清楚，你根本沒有跟電腦說 a 跟 b 分別等於什麼，他沒辦法把他們加在一起啦！再試試看吧！")
    def op2(self):
        msg.showerror("哎呀錯ㄌ", "唉呀唉呀，你忘記加 std:: 了啦！記得注意喔！再試試看吧！")
    def op3(self):
        msg.showinfo("恭喜答對:D", "恭喜你答對了！Foxxy 很為你高興！")
        self.base.destroy()
    def op4(self):
        msg.showerror("哎呀錯ㄌ", "忘記加分號啦！再試試看吧！")


class Question2_2():
    def __init__(self):
        self.base = tk.Tk()
        self.base.wm_attributes('-topmost',1)
        self.base.title("問題三")
        self.text = tk.StringVar()
        self.base.geometry("600x500")
        self.proc = 0
        self.choose = False
        # beware, there are lots of space in the text
        self.t = '''
有了變數的基礎，Foxxy 請你實作「拿出一個兩位數的兩個數字、分別輸出」。
a 為該兩位數，現在請你輸出 a 的十位數和個位數，中間輸出一個空格，行尾輸出空格。
Foxxy 先幫你寫好了一些 code，如下：

#include <iostream>
int main() {                   
	int a;                                    
	std::cin >> a; // 輸入       
	...                                         
	return 0;                             
}                                   

請問 ... 為下列哪一段程式碼時可以解決這個問題？
'''
        self.op1text = '''
std::cout << a[2] << ' ' << a[1] << std::endl;
'''

        self.op2text = '''
std::cout << a << ' ' << a % 10 << std::endl;
'''

        self.op3text = '''
std::cout << a / 10 << ' ' << a % 10 << std::endl;
'''
        self.op4text = '''
std::cout << a << std::endl;
'''
        self.text.set(self.t)
        self.label = tk.Label(self.base, textvariable=self.text)
        self.label.pack()
        tk.Button(self.base, text = self.op1text, command=self.op1).pack()
        tk.Button(self.base, text = self.op2text, command=self.op2).pack()
        tk.Button(self.base, text = self.op3text, command=self.op3).pack()
        tk.Button(self.base, text = self.op4text, command=self.op4).pack()
        self.base.mainloop()

    def op1(self):
        msg.showerror("哎呀錯ㄌ", "a 不是陣列（加入電算社，我們會教你怎麼用陣列的！）\n沒辦法這樣取值喔！")
    def op2(self):
        msg.showerror("哎呀錯ㄌ", "一開始輸出 a 就已經超過一個數字了，再想想吧！")
    def op3(self):
        msg.showinfo("恭喜答對:D", "恭喜你答對！")
        self.base.destroy()
    def op4(self):
        msg.showerror("哎呀錯ㄌ", "這樣數字中間不會有空格喔！再想想吧！")


class Question2_3():
    def __init__(self):
        self.base = tk.Tk()
        self.base.wm_attributes('-topmost',1)
        self.base.title("問題四")
        self.text = tk.StringVar()
        self.base.geometry("600x400")
        self.proc = 0
        self.choose = False
        # beware, there are lots of space in the text
        self.t = '''
現在 foxxy 拿出一排重量不一的蘋果排成一列，但他們的大小並不一樣，
你只知道他們已經把蘋果按照重量由左至右排序過了。
你剛跟電神戰鬥完，突然感到口乾舌燥，急著想拿一顆蘋果吃掉，
但 foxxy 想到了一個好玩的遊戲。他請你找到一顆重量剛剛好為 w 的蘋果，當你找到它就可以把它吃掉。
因為你快渴死了，所以你想要在最快時間內找到 foxxy 指定的蘋果。
請問下列哪一種搜尋方法找到蘋果的速度會最快？
'''
        self.op1text = '''
從最左邊開始，一個一個往右找，反正一定會找到的嘛
'''

        self.op2text = '''
把蘋果按照大小排序，感覺重量對的選下去就對了
'''

        self.op3text = '''
從重量中間的開始找，如果比目標重就找左邊的蘋果，比目標輕就找右邊的
'''
        self.op4text = '''
哎呦不管了啦，這什麼白癡問題，雜湊就對了啦，我要電爛 Foxyy owo
'''
        self.text.set(self.t)
        self.label = tk.Label(self.base, textvariable=self.text)
        self.label.pack()
        tk.Button(self.base, text = self.op1text, command=self.op1).pack()
        tk.Button(self.base, text = self.op2text, command=self.op2).pack()
        tk.Button(self.base, text = self.op3text, command=self.op3).pack()
        tk.Button(self.base, text = self.op4text, command=self.op4).pack()
        self.base.mainloop()

    def op1(self):
        msg.showerror("哎呀錯ㄌ", "你正準備這樣做的時候，Foxxy 趕快跳出來阻止你這麼做\n因為在你找到對的蘋果之前，你會因為找太久就渴死了。\n再看看有沒有更快的搜尋方法吧！")
    def op2(self):
        msg.showerror("哎呀錯ㄌ", "Foxxy 都快哭了，他好不容易幫你照重量排序好結果又被你打亂了！\n大小跟重量沒有絕對關係，所以不能用大小來判斷重量啦！\n好在好心的 Foxxy 又幫你把蘋果照重量排序好了，再試另一個答案吧！")
    def op3(self):
        msg.showinfo("恭喜答對:D", "好耶你答對了，你吃到了 foxxy 精心幫你挑選最好吃的蘋果！")
        self.base.destroy()
    def op4(self):
        msg.showerror("哎呀錯ㄌ", "Foxxy 苦著臉拜託你好好看完選項再應答\n也千萬不要想著靠他幼稚園就會的東西把他電爛，那是不可能的事的啦！")


class Question4():
    def __init__(self):
        self.base = tk.Tk()
        self.base.wm_attributes('-topmost',1)
        self.base.title("問題五")
        self.text = tk.StringVar()
        self.base.geometry("600x400")
        self.proc = 0
        self.choose = False
        # beware, there are lots of space in the text
        self.t = '''
經過了電算社員的開導，你的資訊能力（電場？）明顯大幅提升。
你毫不畏懼地面對 Fire 對你提出的挑戰。
Fire 拿出一段很毒（指易讀性低）的程式碼，請你告訴他程式的輸出結果。
熟悉了變數的你決定直接開電，向 Fire 證明你的實力。
#include <iostream>
int a = 1;                      
int main() {                  
	int a = 2;                            
    	       std::cout << a << std::endl;
	return 0;                             
}                                   
請問輸出結果為何？
'''
        self.op1text = "1"
        self.op2text = "2"
        self.op3text = "1endl0"
        self.op4text = "2endl0"
        self.text.set(self.t)
        self.label = tk.Label(self.base, textvariable=self.text)
        self.label.pack()
        tk.Button(self.base, text = self.op1text, command=self.op1).pack()
        tk.Button(self.base, text = self.op2text, command=self.op2).pack()
        tk.Button(self.base, text = self.op3text, command=self.op3).pack()
        tk.Button(self.base, text = self.op4text, command=self.op4).pack()
        self.base.mainloop()

    def op1(self):
        msg.showerror("哎呀錯ㄌ", "這裡應該選區域變數的 a 喔，再試試看吧")
    def op2(self):
        msg.showinfo("恭喜答對:D", "好耶你答對了")
        self.base.destroy()
    def op3(self):
        msg.showerror("哎呀錯ㄌ", "這裡應該選區域變數的 a 喔，而且 endl 是換行\n然後return 的 0 是不會輸出的啦XD\n再試試看吧")
    def op4(self):
        msg.showerror("哎呀錯ㄌ", "endl 是換行，不是文字\n而且return 的 0 是不會輸出的啦XD\n再試試看吧")


class Question5():
    def __init__(self):
        self.base = tk.Tk()
        self.base.wm_attributes('-topmost',1)
        self.base.title("最終決戰！！！！")
        self.text = tk.StringVar()
        self.base.geometry("600x400")
        self.proc = 0
        self.choose = False
        # beware, there are lots of space in the text
        self.t = '''
Foxxy / 電神狂妄地笑著，他準備拿他幼稚園就會的雜湊來電爛你。
請運用你的計算能力算出 Foxxy / 電神究竟說了些什麼！

已知一個英文字（例：car）是由一個一個英文字母所組成
我們定義 w_1 是字串中倒數第一個字母，w_2 是字串中倒數第二個字母...
而各個英文字母會被轉換成它在 alphabet 裡的順序，如 'a' = 1。
則 car 的 w_1 = 18, w_2 = 1, w_3 = 3
它會被雜湊成 w_1 * p^1 + w_2 * p^2 + w_3 * p^3 +...
若 p = 31，則雜湊值為 18 * (31^1) + 1 * (31^2) + 3 * (31^3) = 90892。

Foxxy / 電神現在對你說 "3963598"，請問他是什麼意思？
提示：你有計算機，這不是考試，是決鬥，所以盡量用！
'''
        self.op1text = "cyf（卡油飯）"
        self.op2text = "clm（卡拉麵）"
        self.op3text = "weak（弱）"
        self.op4text = "dian（電）"
        self.text.set(self.t)
        self.label = tk.Label(self.base, textvariable=self.text)
        self.label.pack()
        tk.Button(self.base, text = self.op1text, command=self.op1).pack()
        tk.Button(self.base, text = self.op2text, command=self.op2).pack()
        tk.Button(self.base, text = self.op3text, command=self.op3).pack()
        tk.Button(self.base, text = self.op4text, command=self.op4).pack()
        self.base.mainloop()

    def op1(self):
        msg.showerror("哎呀錯ㄌ", "沒有油飯可以卡啦 > < \n自己想辦法去找油飯")
    def op2(self):
        msg.showerror("哎呀錯ㄌ", "拉麵好ㄘ\n但答案不是這個ㄛ")

    def op3(self):
        msg.showerror("哎呀錯ㄌ", "你不弱 :angry:")
    def op4(self):
        msg.showinfo("恭喜答對:D", "沒錯！你真電~~~")
        self.base.destroy()



plot = Plot()
dialogue = Dialogue()


# Functions
def initialize():
    global scene_x
    global player_x
    global foxxy_x
    global time_frame
    global control
    global ex_control
    global background
    global started
    global mouse
    global floor_passed
    global floor4_entered
    global next_floor
    global egg_frame
    global egg_count
    scene_x = -5
    player_x = 320 * display_ratio - 70
    foxxy_x = player_x - 50 * display_ratio
    time_frame = 0
    control = 0
    ex_control = control
    background = background_paper[0]
    started = 0
    mouse = ""
    floor_passed = 1
    floor4_entered = False
    next_floor = 4
    egg_frame = 0
    egg_count = 0
    system("cls")


def control_flow(cur_control, started):
    global floor_passed
    global floor4_entered
    global next_floor
    bias = check_tp_f(cur_control, player_x, floor_passed)
    control_loc = cur_control + bias
    if bias != 0:
        print(f"bias = {bias}, control_loc = {control_loc}, next_floor = {next_floor}")
        cutscene(0)
        if control_loc == next_floor:
            if not floor4_entered and next_floor == 4:
                cutscene("jump")
                plot.plot_1()
                floor_passed = 0
                return 4
            floor_passed = 0
            cutscene("jump")
            return control_loc
        else:
            cutscene("jump")
            return control_loc
    if cur_control == -1:
        return -1
    elif started == 0 and mouse == "down":
        screen.blit(warning_image, (0, 0))
        update()
        check_mouse()
        return 1
    elif not started:
        return 0
    elif control_loc == next_floor:
        if next_floor == 4:
            if not floor4_entered and check_npc_event(control_loc, scene_x, floor_passed):
                dialogue.dia_1()
                call_battle(1) # battle 1
                floor4_entered = True
                floor_passed = 1
                cutscene(0)
                plot.plot_2()
                cutscene(0)
                floor_passed = 0
                next_floor = 2
                return 2
            elif floor4_entered and check_npc_event(control_loc, scene_x, floor_passed):
                dialogue.dia_8()
                call_battle(5) # battle 4
                dialogue.dia_9()
                dialogue.dia_10()
                call_battle(6) # battle 5
                dialogue.dia_11()
                plot.plot_5()
                floor_passed = 1
                print("遊戲結束:D, 謝謝你的參與:D")
                thanks_display()
                return 1
            else:
                return control_loc
        elif next_floor == 2 and check_npc_event(control_loc, scene_x, floor_passed):
            cutscene(0)
            dialogue.dia_2()
            dialogue.dia_3()
            dialogue.dia_4()
            call_battle(2) # battle 2.1
            call_battle(3) # battle 2.2
            call_battle(4) # battle 2.3
            dialogue.dia_5()
            floor_passed = 1
            next_floor = 3
            cutscene(0)
            return 2
        elif next_floor == 3 and check_npc_event(control_loc, scene_x, floor_passed):
            cutscene(0)
            dialogue.dia_6()
            mayo_main() # battle 3
            dialogue.dia_7()
            plot.plot_3()
            cutscene(0)
            floor_passed = 1
            next_floor = 4
            return 3
        else:
            return control_loc
    else:
        return control_loc


def check_mouse():
    while True:
        flag = 0
        for event in get(): # pygame.event.get()
            if event.type == QUIT: # pygame.QUIT
                check_quit(mouse_pos)
            if event.type == MOUSEBUTTONDOWN: # pygame.MOUSEBUTTONDOWN
                check_quit(mouse_pos)
                flag = 1
        if flag:
            break


def check_quit(mouse_pos): # 0 for running, 1 for breaking
    global running
    global control
    # screen.blit(frame, (0, 0))
    # input()
    if mouse_pos[0] > 570 * display_ratio and mouse_pos[0] < 630 * display_ratio \
        and mouse_pos[1] > 10 * display_ratio and mouse_pos[1] < 34 * display_ratio:
        # running = False
        control = -1
    else:
        running = True


def check_tp(player_x, floor_passed):
    if floor_passed:
        if player_x <= 260:
            return -1
        if player_x >= 490 * display_ratio:
            return 1
        else:
            return 0
    else:
        return 0


def check_tp_f(control, player_x, floor_passed):
    if control <= 0:
        return 0
    elif check_tp(player_x, floor_passed) == -1:
        if control == 1:
            return 0
        screen.blit(key_f, (110 + scene_x, 140 * display_ratio))
        screen.blit(arrow_down, (130 + scene_x, 135 * display_ratio))
            
        if keys[K_f]:
            return -1
        else:
            return 0
    elif check_tp(player_x, floor_passed) == 1:
        if control == 4:
            return 0
        screen.blit(key_f, (1060 * display_ratio + scene_x, 140 * display_ratio))
        screen.blit(arrow_up, (1080 * display_ratio + scene_x, 135 * display_ratio))
        if keys[K_f]:
            return 1
        else:
            return 0
    else:
        return 0


def check_npc_event(control, scene_x, floor_passed):
    if control <= 1 or floor_passed:
        return False
    elif scene_x <= -230 * display_ratio and scene_x >= -300 * display_ratio:
        screen.blit(key_f, (575 * display_ratio + scene_x, 155 * display_ratio))
        update()
        if keys[K_f]:
            return True
        else:
            return False
    else:
        return False


def sure_to_quit(ex_control):
    global running
    global control
    global screen
    if control == -1:
        if display_ratio == 2:
            if mouse_pos[0] > 592 and mouse_pos[0] < 778 \
                and mouse_pos[1] > 480 and mouse_pos[1] < 555 and mouse == "down":
                # initialize()
                running = False
            elif mouse_pos[0] > 850 and mouse_pos[0] < 1033 \
                and mouse_pos[1] > 480 and mouse_pos[1] < 555 and mouse == "down":
                control = ex_control
        else:
            if mouse_pos[0] > 877 and mouse_pos[0] < 1063 \
                and mouse_pos[1] > 600 and mouse_pos[1] < 675 and mouse == "down":
                # initialize()
                running = False
            elif mouse_pos[0] > 1135 and mouse_pos[0] < 1318 \
                and mouse_pos[1] > 600 and mouse_pos[1] < 675 and mouse == "down":
                control = ex_control


def background_display(control, scene, scene_x):
    screen.fill((0, 0, 0))
    if control == -1:
        if display_ratio == 2:
            screen.blit(sure_to_quit_image, (100, 40))
        else:
            screen.blit(sure_to_quit_image, (385, 160)) # 2: (100, 40)
    elif control == 0:
        screen.blit(scene, (0, 0))
    else:
        screen.blit(scene, (scene_x, 0))
        # if control != 0:
            # screen.blit(arrow_down, (30 * display_ratio + scene_x, 270 * display_ratio))
            # screen.blit(arrow_up, (1050 * display_ratio + scene_x, 270 * display_ratio))
    screen.blit(quit_icon, (570 * display_ratio, 10 * display_ratio))


def player_display(control, player_x, time_frame):
    if keys[K_d]: # pygame.K_d
        side = 2
    elif keys[K_a]:
        side = 1
    else:
        side = 0
    if side == 0:
        feet = 0
    elif time_frame < 10:
        feet = 0
    else:
        feet = 1
    player = player_images[side][feet]
    if control > 0:
        screen.blit(player, (player_x, 180 * display_ratio))


def foxxy_display(control, player_x, time_frame):
    if next_floor != 3:
        return
    if keys[K_d]: # pygame.K_d
        side = 2
    elif keys[K_a]:
        side = 1
    else:
        side = 0
    if side == 0:
        feet = 0
    elif time_frame < 10:
        feet = 0
    else:
        feet = 1
    foxxy = foxxy_images[side][feet]
    if control > 0:
        screen.blit(foxxy, (player_x - 60 * display_ratio, 180 * display_ratio))


def npc_display(control, scene_x, floor_passed, next_floor):
    if control <= 1 or floor_passed or control != next_floor:
        return
    elif control == 4 and floor4_entered:
        screen.blit(npc_images[5], (550 * display_ratio + scene_x, 180 * display_ratio))
    else:
        screen.blit(npc_images[control], (550 * display_ratio + scene_x, 180 * display_ratio))
    

def tp_display(control, scene_x, time_frame, floor_passed):
    if control < 1 or not floor_passed:
        return
    if time_frame < 10:
        if control != 1:
            screen.blit(tp_point_image1, (60 + scene_x, 170 * display_ratio))
        if control != 4:
            screen.blit(tp_point_image1, (1040 * display_ratio + scene_x, 170 * display_ratio))
    else:
        if control != 1:
            screen.blit(tp_point_image2, (60 + scene_x,  170 * display_ratio))
        if control != 4:
            screen.blit(tp_point_image2, (1040 * display_ratio + scene_x, 170 * display_ratio))



def floorSign_display(control, scene_x):
    if control == 1:
        # screen.blit(floor_sign_12, (110 * display_ratio + scene_x, 107 * display_ratio))
        screen.blit(floor_sign_12, (1000 * display_ratio + scene_x, 108 * display_ratio))
    elif control == 2:
        screen.blit(floor_sign_12, (110 * display_ratio + scene_x, 107 * display_ratio))
        screen.blit(floor_sign_23, (1000 * display_ratio + scene_x, 108 * display_ratio))
    elif control == 3:
        screen.blit(floor_sign_23, (110 * display_ratio + scene_x, 107 * display_ratio))
        screen.blit(floor_sign_34, (1000 * display_ratio + scene_x, 108 * display_ratio))
    elif control == 4:
        screen.blit(floor_sign_34, (110 * display_ratio + scene_x, 107 * display_ratio))
        screen.blit(floor_sign_44, (1000 * display_ratio + scene_x, 108 * display_ratio))


def thanks_display():
    screen.fill((0, 0, 0))
    update()
    y = 1500
    while y > -11500:
        screen.blit(thank_list, (0, y))
        y -= 10
        update()
        sleep(0.03)
        if y % 1000 == 0:
            get()
    check_mouse()
        

def egg():
    global egg_frame
    pass


def call_battle(proc):
    if proc == 1:
        question1()
    elif proc == 2:
        Q = Question2_1()
    elif proc == 3:
        Q = Question2_2()
    elif proc == 4:
        Q = Question2_3()
    elif proc == 5:
        Q = Question4()
    elif proc == 6:
        Q = Question5()


def cutscene(mode=0):
    global player_x
    global scene_x
    screen.fill((0, 0, 0))
    update()
    sleep(0.5)
    if mode == "jump":
        player_x = 320 * display_ratio - 70
    scene_x = -5
    print(player_x)


def story_backgroud():
    screen.fill((0, 0, 0))
    screen.blit(classroom, (0, 0))

def scroll_walk():
    global scene_x
    global player_x
    global foxxy_x
    border_r = 520 * display_ratio
    if control <= 0:
        return
    if keys[K_d]: # pygame.K_d
        if player_x + speed <= 320 * display_ratio - 70:
            player_x += speed
        elif scene_x - speed >= -border_r:
            scene_x -= speed
        elif player_x + 140 + speed <= 640 * display_ratio:
            player_x += speed
    elif keys[K_a]: # pygame.K_a
        if player_x - speed >= 320 * display_ratio - 70:
            player_x -= speed
        elif scene_x + speed <= -5:
            scene_x += speed
        elif player_x - speed >= 0:
            player_x -= speed


def pygame_event_response(mouse_pos):
    global running
    global mouse
    global egg_frame
    global egg_count
    for event in get(): # pygame.event.get()
        if event.type == QUIT: # pygame.QUIT
            check_quit(mouse_pos)
        if event.type == MOUSEBUTTONDOWN: # pygame.MOUSEBUTTONDOWN
            mouse = "down"
            print(mouse_pos)
            check_quit(mouse_pos)
        if event.type != MOUSEBUTTONDOWN:
            mouse = ""
        if event.type == KEYDOWN:
            print("keydown")
            if egg_frame == 0:
                print("count = 0")
                if event.key == K_UP:
                    print("UP")
                    egg_count = 1
                    egg_frame += 1
            else:
                if egg_frame > 500:
                    egg_frame = 0
                else:
                    egg_frame += 1
                    if egg_count == 1:
                        if event.key == K_UP:
                            egg_count = 2
                        else:
                            egg_count = 0
                    elif egg_count == 2:
                        if event.key == K_DOWN:
                            egg_count += 1
                        else:
                            egg_count = 0
                    elif egg_count == 3:
                        if event.key == K_DOWN:
                            egg_count += 1
                        else:
                            egg_count = 0
                    elif egg_count == 4:
                        if event.key == K_LEFT:
                            egg_count += 1
                        else:
                            egg_count = 0
                    elif egg_count == 5:
                        if event.key == K_RIGHT:
                            egg_count += 1
                        else:
                            egg_count = 0
                    elif egg_count == 6:
                        if event.key == K_LEFT:
                            egg_count += 1
                        else:
                            egg_count = 0
                    elif egg_count == 7:
                        if event.key == K_RIGHT:
                            egg_count += 1
                        else:
                            egg_count = 0
                    elif egg_count == 8:
                        if event.key == K_a:
                            egg_count += 1
                        else:
                            egg_count = 0
                    elif egg_count == 9:
                        if event.key == K_b:
                            egg_count += 1
                            thanks_display()
                            egg_count = 0
                        else:
                            egg_count = 0
                            



# Game Loop
background = background_paper[0]
initialize()
print("點下滑鼠，開始遊戲吧:D")
while running:
    # Basic Info
    keys = get_pressed() # pygame.key.get_pressed()
    mouse_pos = get_pos() # pygame.mouse.get_pos()
    scroll_walk()
    pygame_event_response(mouse_pos)
    time_frame = (time_frame + 1) % 20
    if control != -1:
        ex_control = control
    if control == -1:
        sure_to_quit(ex_control)
    started = control
    # background fill
    background_display(control, background_paper[control], scene_x)
    tp_display(control, scene_x, time_frame, floor_passed)
    floorSign_display(control, scene_x)
    npc_display(control, scene_x, floor_passed, next_floor)
    player_display(control, player_x, time_frame)
    foxxy_display(control, player_x, time_frame)
    control = control_flow(control, started)
    update() # pygame.display.update()
    sleep(0.01)
