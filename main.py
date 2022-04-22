#!/usr/bin/env python3
from pygame.display import set_mode, update, set_caption, set_icon
from pygame.transform import scale, rotate
from pygame.image import load
from pygame.mixer import music
from pygame.draw import rect as draw_rect, line
from pygame import init, Rect, QUIT, MOUSEBUTTONDOWN, K_d, K_f, K_j, K_k, K_a
from pygame.mouse import get_pos
from pygame.key import get_pressed
from pygame.event import get
from time import time, sleep
from subprocess import run as subrun
from os import system
from time import time, sleep

# intialize
init() # pygame.init()

# Global Variable
display_ratio = 2 # (640 * ratio, 360 * ratio)
speed = (display_ratio - 1) * 10
running = True
mouse = ""
scene_x = -5
player_x = 320 * display_ratio - 70
time_frame = 0
control = 0
ex_control = control
print_flag = 0
started = 0
floor_passed = 1
floor4_entered = False

# set screen
screen = set_mode((640 * display_ratio, 360 * display_ratio)) # pygame.display.set_mode()

# background
cover_image = load("images\\cover_image.png") # pygame.image.load()
floor_1_image = load("images\\1F.png")
floor_2_image = load("images\\2F.png")
floor_3_image = load("images\\3F.png")
floor_4_image = load("images\\4F.png")
if display_ratio != 3:
    cover_image = scale(cover_image, (640 * display_ratio, 360 * display_ratio))
    floor_1_image = scale(floor_1_image, (1153 * display_ratio, 360 * display_ratio))
    floor_2_image = scale(floor_2_image, (1153 * display_ratio, 360 * display_ratio))
    floor_3_image = scale(floor_3_image, (1153 * display_ratio, 360 * display_ratio))
    floor_4_image = scale(floor_4_image, (1153 * display_ratio, 360 * display_ratio))
frame = load("images\\example.png")
sure_to_quit_image = load("images\\sure_to_exit.png")
background_paper = [cover_image, floor_1_image, floor_2_image, floor_3_image, floor_4_image]

# Title and Icon
set_caption("CRC") # pygame.display.set_caption()
logo = load("images/logo.jpg") # pygame.image.load()
set_icon(logo) # pygame.display.set_icon

# Objects
keys = []
quit_icon = load("images\\quit.png") # pygame.image.load()
quit_icon = scale(quit_icon, (60 * display_ratio, 24 * display_ratio)) # pygame.transform.scale

player_front = load("images\\player_front.png")
player_left0 = load("images\\player_left0.png")
player_left1 = load("images\\player_left1.png")
player_left2 = load("images\\player_left2.png")
player_right0 = load("images\\player_right0.png")
player_right1 = load("images\\player_right1.png")
player_right2 = load("images\\player_right2.png")
tp_point_image1 = load("images\\tp1.png")
tp_point_image2 = load("images\\tp2.png")

player_front = scale(player_front, (70 * display_ratio, 98 * display_ratio)) # 450 * 11/38 * display_ratio
player_left0 = scale(player_left0, (65 * display_ratio, 98 * display_ratio))
player_left1 = scale(player_left1, (65 * display_ratio, 98 * display_ratio))
player_left2 = scale(player_left2, (65 * display_ratio, 98 * display_ratio))
player_right0 = scale(player_right0, (65 * display_ratio, 98 * display_ratio))
player_right1 = scale(player_right1, (65 * display_ratio, 98 * display_ratio))
player_right2 = scale(player_right2, (65 * display_ratio, 98 * display_ratio))
tp_point_image1 = scale(tp_point_image1, (133 * display_ratio, 133 * display_ratio))
tp_point_image2 = scale(tp_point_image2, (133 * display_ratio, 133 * display_ratio))

foxyy_8bit = load("images\\Foxxy_8bit.png")
bamboo_8bit = load("images\\Bamboo_8bit.png")
bright_8bit = load("images\\Bright_8bit.png")

foxyy_8bit = scale(foxyy_8bit, (80 * display_ratio, 98 * display_ratio))
bamboo_8bit = scale(bamboo_8bit, (80 * display_ratio, 98 * display_ratio))
bright_8bit = scale(bright_8bit, (80 * display_ratio, 98 * display_ratio))

player_images = [[player_front], [player_left0, player_left1, player_left2], [player_right0, player_right1, player_right2]]
npc_images = [foxyy_8bit, None, bright_8bit, bamboo_8bit, foxyy_8bit] # index 4 is waiting to be changed


# Mayonaise Game #54 ~ #279
mode = "normal" # "normal" or "hard"
drop_before_arrive = 0.8
pixel_per_second = 565 / drop_before_arrive

mayo = load("images\mayo.webp") # pygame.image.load()
mayo.convert()
start_menu = load("images\patrick_mayo.jpg")
start_menu.convert()
start_menu = scale(start_menu, (800, 600)) # pygame.transform.scale
start_button = load("images\start_button.png")
start_button.convert()
start_button = scale(start_button, (200, 100))
mayo = rotate(mayo, 90) # pygame.transform.rotate
mayo = scale(mayo, (100, 100))

slot = (125, 30)
rect = Rect(200, 0, 10, 600) # pygame.Rect()
white_back = Rect(0, 0, 800, 600)
border_left_line = Rect(140, 0, 10, 600)
border_right_line = Rect(650, 0, 10, 600)
display_pressed1 = Rect(150, 500, slot[0], slot[1])
display_pressed2 = Rect(275, 500, slot[0], slot[1])
display_pressed3 = Rect(400, 500, slot[0], slot[1])
display_pressed4 = Rect(525, 500, slot[0], slot[1])
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
    draw_rect(screen, (107, 186, 241), white_back) # pygame.draw.rect()
    draw_rect(screen, (255, 255, 0), border_left_line)
    draw_rect(screen, (255, 255, 0), border_right_line)
    
    line(screen, (255, 255, 255), (275, 0),(275, 600)) # pygame.draw.line()
    line(screen, (255, 255, 255), (400, 0),(400, 600))
    line(screen, (255, 255, 255), (525, 0),(525, 600))
    
    line(screen, (100, 100, 100), (150, 500),(650, 500))
    line(screen, (100, 100, 100), (150, 530),(650, 530))

def mayo_main():
    global screen
    init() # pygame.init()
    screen = set_mode((800, 600)) # pygame.display.set_mode
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
            screen.blit(start_button, (370, 70))
            if mouse == "down":
                if mouse_pos[0] > 300 and mouse_pos[0] < 500 and mouse_pos[1] > 100 and mouse_pos[1] < 400:
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
            In = True
            if i <= len(showing_array) - 1 and check_remove(time_pass, showing_array[i], prev_key[showing_array[i][4]], 0) \
                and keys[K_d]: # pygame.K_d
                showing_array[i][1] = 2000
                showing_array[i][2] = 2000
                showing_array[i][5] = 1
            if i <= len(showing_array) - 1 and check_remove(time_pass, showing_array[i], prev_key[showing_array[i][4]], 1) \
                and keys[K_f]: # pygame.K_f
                showing_array[i][1] = 2000
                showing_array[i][2] = 2000
                showing_array[i][5] = 1
            if i <= len(showing_array) - 1 and check_remove(time_pass, showing_array[i], prev_key[showing_array[i][4]], 2) \
                and keys[K_j]: # pygame.K_j
                showing_array[i][1] = 2000
                showing_array[i][2] = 2000
                showing_array[i][5] = 1
            if i <= len(showing_array) - 1 and check_remove(time_pass, showing_array[i], prev_key[showing_array[i][4]], 3) \
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


# GOD CLASS # 290 ~ # 684
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
        # screen.blit(diangod_image, (0,0)) # 電神輕視表情
        screen.blit(dia_1_0, (0,0)) # 電神：「又有挑戰者了嗎？」
        update()
        check_mouse()
        # screen.blit(player_image, (0,0)) # 玩家皺眉表情
        screen.blit(dia_1_1, (0,0)) # （你皺了皺眉，聽不太懂他的意思）
        update()
        check_mouse()
        # screen.blit(diangod_image, (0,0)) # 電神得意表情
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
        # screen.blit(bright_image, (0,0))
        screen.blit(dia_2_0, (0,0)) # Bright：「你剛剛和他戰鬥了吧！」
        update()
        check_mouse()
        # screen.blit(player_image, (0,0))
        screen.blit(dia_2_1, (0,0)) # 你：「他？指在四樓的那個閃電人嗎？」or 「對啊，他究竟是誰啊？」
        update()
        check_mouse()
        # screen.blit(bright_image, (0,0))
        screen.blit(dia_2_2, (0,0)) # Bright:「呵呵，他是《電神》是我們組織的統治者」
        update()
        check_mouse()
        # screen.blit(player_image, (0,0))
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
        # screen.blit(foxyy_image, (0,0)) # foxyy 開心表情
        screen.blit(dia_3_0, (0,0)) # foxyy：「我們是CRC！」
        update()
        check_mouse()
        # screen.blit(playerbright_image, (0,0)) # player 和 bright 若有所思
        screen.blit(dia_3_1, (0,0)) # (看著突然出現的女子，你跟Bright都若有所思）
        update()
        check_mouse()
        # screen.blit(player_image, (0,0)) # player 驚嚇表情
        screen.blit(dia_3_2, (0,0)) # 你：（怎麼突然有人冒出來）
        update()
        check_mouse()
        # screen.blit(bright_image, (0,0)) # bright 驚嚇表情
        screen.blit(dia_3_3, (0,0)) # Bright：（他…怎麼會出現在這裡）
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 開心表情
        screen.blit(dia_3_4, (0,0)) # foxyy：「CRC，又稱為電算社，我們擁有能改變世界的電算之力！」
        update()
        check_mouse()
        screen.blit(dia_3_5, (0,0)) # foxyy：「簡單來說，就是程式設計。如果精通這項能力，就會擁有很強大的力量，例如發射閃電之類的喔！」
        update()
        check_mouse()
        # screen.blit(player_image, (0,0)) # player 和 bright 開心表情
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
        # screen.blit(bright_image, (0,0)) # bright 得意表情
        screen.blit(dia_4_0, (0,0)) # Bright：「我可是教導程式的高手呢！只要十分鐘，我便能把所有的基礎都教會你！」
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 可愛表情
        screen.blit(dia_4_1, (0,0)) # foxyy：「人家也來幫你吧！」
        update()
        check_mouse()
        # screen.blit(player_image, (0,0)) # player 安心表情
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
        # screen.blit(player_image, (0,0)) # player 電流
        screen.blit(dia_5_0, (0,0)) # （在Bright和foxyy的教導之下，你很快就學會基礎的程式設計，並感覺到有股電流在你的身體裡流竄）
        update()
        check_mouse()
        # screen.blit(bright_image, (0,0)) # bright 開心表情
        screen.blit(dia_5_1, (0,0)) # Bright：「學的這麼快，看來你擁有很強的潛力呢。不過，我能教的都教完了，如果你想學更多，就到三樓去找更多高手請教吧，但是要注意，有些人並不歡迎外人打擾。」
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 驚嚇表情
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
        # screen.blit(playerfoxyy_image, (0,0)) # player 和 foxyy 牽手
        screen.blit(dia_6_0, (0,0)) # （你和foxyy來到了三樓）
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 開心表情
        screen.blit(dia_6_1, (0,0)) # foxyy：「我們去右邊的教室吧！」
        update()
        check_mouse()
        # screen.blit(bamboo_image, (0,0)) # bamboo 殺氣背影配刀
        screen.blit(dia_6_2, (0,0)) # (一進去教室，你看到有名女子正坐在講桌電腦旁擦著手上的刀)
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 普通表情
        screen.blit(dia_6_3, (0,0)) # foxyy:是學術組的Bamboo，看來真的遇到高手了
        update()
        check_mouse()
        # screen.blit(bamboo_image, (0,0)) # bamboo 殺氣臉
        screen.blit(dia_6_4, (0,0)) # (Bamboo望了你們一眼）
        update()
        check_mouse()
        screen.blit(dia_6_5, (0,0)) # Bamboo:「怎麼會有外人前來拜訪」
        update()
        check_mouse()
        # screen.blit(player_image, (0,0)) # player 普通表情
        screen.blit(dia_6_6, (0,0)) # 你：「早安，為了雪恥，請教我更進階的程式以面對電神，請885」or「ㄜ...我來學精深的程式，助我打敗電神」
        update()
        check_mouse()
        # screen.blit(bamboo_image, (0,0)) # bamboo 殺氣表情
        screen.blit(dia_6_7, (0,0)) # Bamboo:「聽你一說，你想請託我協助你們挑戰電神？所以你們其實是入侵者吧」
        update()
        check_mouse()
        # screen.blit(foxyybamboo_image, (0,0)) # foxyy 冒汗表情 bamboo 握刀
        screen.blit(dia_6_8, (0,0)) # （foxyy正想解釋，但Bamboo已經拔刀奔來）
        update()
        check_mouse()
        # screen.blit(bamboo_image, (0,0)) # bamboo 殺氣表情
        screen.blit(dia_6_9, (0,0)) # Bamboo:「沒想到你們竟能從電神手中逃過一劫，不過在下是不會放過任何入侵者的」
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 冒汗表情
        screen.blit(dia_6_10, (0,0)) # foxyy:「（指著門）快點離開，危險！」
        update()
        check_mouse()
        # screen.blit(bamboo_image, (0,0)) # bamboo 殺氣表情
        screen.blit(dia_6_11, (0,0)) # Bamboo:「別想逃，”竹林叢生”」
        update()
        check_mouse()
        # screen.blit(manybamboo_image, (0,0)) # 一堆竹子
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
        # screen.blit(playerbamboo_image, (0,0)) # player 累 bamboo 憤怒表情
        screen.blit(dia_7_0, (0,0)) # （你不斷閃過Bamboo的斬擊，Bamboo開始感到心急）
        update()
        check_mouse()
        # screen.blit(bamboo_image, (0,0)) # bamboo 憤怒表情
        screen.blit(dia_7_1, (0,0)) # Bamboo:可惡，區區入侵者在下居然不能解決
        update()
        check_mouse()
        screen.blit(dia_7_2, (0,0)) # Bamboo:《程式枷鎖》
        update()
        check_mouse()
        # screen.blit(playerRRR_image, (0,0)) # player + 枷鎖
        screen.blit(dia_7_3, (0,0)) # （突然有一條寫滿程式的繩子將你綁住，使你無法動彈）
        update()
        check_mouse()
        # screen.blit(player_image, (0,0)) # player 問號表情
        screen.blit(dia_7_4, (0,0)) # 你：「這是什麼東西」
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 嚴肅表情
        screen.blit(dia_7_5, (0,0)) # foxyy:「程式枷鎖⋯⋯，除非你找出這程式的bug，否則這不會解開」
        update()
        check_mouse()
        # screen.blit(bamboo_image, (0,0)) # bamboo 殺氣表情
        screen.blit(dia_7_6, (0,0)) # Bamboo：「這樣就結束了，接招吧《竹切斬》」
        update()
        check_mouse()
        screen.blit(dia_7_7, (0,0)) # （強力的斬擊落下，劍氣所及之處煙霧四散）
        update()
        check_mouse()
        screen.blit(dia_7_8, (0,0)) # （待煙霧散去，Bam發現你們兩個都沒事）
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 自豪表情
        screen.blit(dia_7_9, (0,0)) # foxyy:「這種程式，找出bug有什麼難的」
        update()
        check_mouse()
        # screen.blit(bamboo_image, (0,0)) # bamboo 驚訝表情
        screen.blit(dia_7_10, (0,0)) # （Bamboo驚訝的看著foxyy，過了幾秒後發現原來foxyy其實是自己人）
        update()
        check_mouse()
        screen.blit(dia_7_11, (0,0)) # Bamboo:原來是foxyy，這代表你不是入侵者吧
        update()
        check_mouse()
    def dia_8(self):
        dia_8_0 = load("images\\dia\\dia_8\\dia_8_0.png")
        dia_8_1 = load("images\\dia\\dia_8\\dia_8_1.png")
        if display_ratio == 2:
            dia_8_0 = scale(dia_8_0, (1280, 720))
            dia_8_1 = scale(dia_8_1, (1280, 720))
        # screen.blit(fire_image, (0,0)) # fire 輕視表情
        screen.blit(dia_8_0, (0,0)) # Fire:「你怎麼又上來了，還想再被電爆嗎？」
        update()
        check_mouse()
        screen.blit(dia_8_1, (0,0)) # Fire:「以你這種程度，根本不用電神出馬，我一個人就能解決你了」
        update()
        check_mouse()
    def dia_9(self):
        dia_9_0 = load("images\\dia\\dia_9\\dia_9_0.png")
        if display_ratio == 2:
            dia_9_0 = scale(dia_9_0, (1280, 720))
        # screen.blit(fire_image, (0,0)) # fire 驚訝表情
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
        screen.blit(dia_10_0, (0,0)) # （之後你走進教室，看見教室裡面只有foxyy一個人）
        update()
        check_mouse()
        screen.blit(dia_10_1, (0,0)) # 你：「電神不在這裡嗎？」or「foxyy，電神在哪裡？」
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 普通表情
        screen.blit(dia_10_2, (0,0)) # foxyy:「電神？他現在正在這間教室裡啊」
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 女裝
        screen.blit(dia_10_3, (0,0)) # 你不了解她說的意思，直到看見她手中的閃電，你才終於發現了異常。foxyy脱去女裝，周圍爆發出閃電
        update()
        check_mouse()
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
        # screen.blit(foxyy_image, (0,0)) # foxyy 倒地
        screen.blit(dia_11_0, (0,0)) # （你歷經了千辛萬苦，終於在最後一刻找到機會電爆foxyy，foxyy倒地不起）
        update()
        check_mouse()
        screen.blit(dia_11_1, (0,0)) # foxyy:我⋯竟然輸了
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 欣慰表情
        screen.blit(dia_11_2, (0,0)) # （foxyy臉上並未出現任何不甘和憤怒，反而欣慰的笑了）
        update()
        check_mouse()
        screen.blit(dia_11_3, (0,0)) # foxyy:「我就知道你有這個潛力，當初放你一馬並教導你，就是為了激發深藏在你體內的電算之力，CRC之後就交給你了」
        update()
        check_mouse()


plot = Plot()
dialogue = Dialogue()


# Functions
def initialize():
    global scene_x
    global player_x
    global time_frame
    global control
    global ex_control
    global print_flag
    global background
    global started
    global mouse
    global floor_passed
    global floor4_entered
    scene_x = -5
    player_x = 320 * display_ratio - 70
    time_frame = 0
    control = 0
    ex_control = control
    print_flag = 0
    background = background_paper[0]
    started = 0
    mouse = ""
    floor_passed = 1
    floor4_entered = False
    system("cls")


def control_flow(cur_control, started):
    global floor_passed
    global floor4_entered
    if cur_control == -1:
        return -1
    elif started == 0 and mouse == "down":
        return 1
    elif not started:
        return 0
    elif cur_control == 1 and check_tp(player_x, floor_passed):
        cutscene("jump")
        plot.plot_1()
        floor_passed = 0
        return 4
    elif cur_control == 4 and check_npc_event(control, scene_x, floor_passed) and not floor4_entered:
        dialogue.dia_1()
        # battle 1
        floor4_entered = True
        floor_passed = 1
        cutscene(0)
        plot.plot_2()
        cutscene(0)
        floor_passed = 0
        return 2
    elif cur_control == 2 and check_npc_event(control, scene_x, floor_passed):
        cutscene(0)
        dialogue.dia_2()
        dialogue.dia_3()
        dialogue.dia_4()
        # battle 2
        dialogue.dia_5()
        floor_passed = 1
        cutscene(0)
        return 2
    elif cur_control == 2 and check_tp(player_x, floor_passed):
        floor_passed = 0
        cutscene("jump")
        return 3
    elif cur_control == 3 and check_npc_event(control, scene_x, floor_passed):
        cutscene(0)
        dialogue.dia_6()
        mayo_main() # battle 3
        dialogue.dia_7()
        plot.plot_3()
        cutscene(0)
        floor_passed = 1
        return 3
    elif cur_control == 3 and check_tp(player_x, floor_passed):
        floor_passed = 0
        cutscene("jump")
        return 4
    elif cur_control == 4 and check_npc_event(control, scene_x, floor_passed) and floor4_entered:
        dialogue.dia_8()
        # battle 4
        dialogue.dia_9()
        dialogue.dia_10()
        # battle 5
        dialogue.dia_11()
        plot.plot_5()
        floor_passed = 1
        print("遊戲結束:D, 謝謝你的參與:D")
        return 1
    else:
        return cur_control


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
    global control
    if floor_passed:
        if player_x <= 260 or player_x >= 515 * display_ratio:
            return True
        else:
            return False
    else:
        return False


def check_npc_event(control, scene_x, floor_passed):
    if control <= 1 or floor_passed:
        return False
    elif scene_x <= -230 * display_ratio:
        return True
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
        feet = 1
    else:
        feet = 2
    player = player_images[side][feet]
    if control > 0:
        screen.blit(player, (player_x, 180 * display_ratio))


def npc_display(control, scene_x, floor_passed):
    if control <= 1 or floor_passed:
        return
    screen.blit(npc_images[control], (550 * display_ratio + scene_x, 180 * display_ratio))
    


def tp_display(control, scene_x, time_frame, floor_passed):
    if control < 1 or not floor_passed:
        return
    if time_frame < 10:
        screen.blit(tp_point_image1, (90 + scene_x, 143 * display_ratio))
        screen.blit(tp_point_image1, (1000 * display_ratio + scene_x, 143 * display_ratio))
    else:
        screen.blit(tp_point_image2, (90 + scene_x,  143 * display_ratio))
        screen.blit(tp_point_image2, (1000 * display_ratio + scene_x, 143 * display_ratio))

def cutscene(mode):
    global player_x
    global scene_x
    screen.fill((0, 0, 0))
    update()
    sleep(1)
    if mode == "jump":
        player_x = 320 * display_ratio - 70
    scene_x = -5
    print(player_x)

def scroll_walk():
    global scene_x
    global player_x
    border_r = 520 * display_ratio
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
    for event in get(): # pygame.event.get()
        if event.type == QUIT: # pygame.QUIT
            check_quit(mouse_pos)
        if event.type == MOUSEBUTTONDOWN: # pygame.MOUSEBUTTONDOWN
            mouse = "down"
            print(mouse_pos)
            check_quit(mouse_pos)
        if event.type != MOUSEBUTTONDOWN:
            mouse = ""


# Game Loop
background = background_paper[0]
print("點下滑鼠，開始遊戲吧:D")
while running:
    # Basic Info
    keys = get_pressed() # pygame.key.get_pressed()
    mouse_pos = get_pos() # pygame.mouse.get_pos()
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
    tp_display(control, scene_x, time_frame, floor_passed)
    npc_display(control, scene_x, floor_passed)
    update() # pygame.display.update()
