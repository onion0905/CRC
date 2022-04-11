class Plot :
    def plot_1(self):
        plot_1_0 = load("images\\plot\\plot_1_0.png")
        plot_1_1 = load("images\\plot\\plot_1_1.png")
        plot_1_0 = scale(plot_1_0, (1280, 720))
        plot_1_1 = scale(plot_1_1, (1280, 720))
        # screen.blit(player_image, (0,0))
        update()
        check_mouse()
        screen.blit(plot_1_0, (0,0)) # 你不斷地往上方走，試圖找到光的來源。你走到了四樓，發現光來自電腦教室，於是你抱著好奇心走進裡面。
        update()
        check_mouse()
        # screen.blit(diangod_image, (0,0))
        update()
        check_mouse()
        screen.blit(plot_1_1, (0,0)) # 進去後，你看到一位渾身散發著閃電的男子
        update()
        check_mouse()
    def plot_2(self):
        plot_2_0 = load("images\\plot\\plot_2_0.png")
        plot_2_1 = load("images\\plot\\plot_2_1.png")
        plot_2_0 = scale(plot_2_0, (1280, 720))
        plot_2_1 = scale(plot_2_1, (1280, 720))
        # screen.blit(player_image, (0,0))
        update()
        check_mouse()
        screen.blit(plot_2_0, (0,0)) # 雖然你落敗了，但這也挑起你對程式的興趣，眼看下一道閃電即將轟來，你連忙躲進旁邊的電梯裡。
        update()
        check_mouse()
        screen.blit(plot_2_1, (0,0)) # 你乘著電梯來到二樓，你看見二樓教室裡有位穿著如同電神小弟一般的不明男子。
        update()
        check_mouse()
    def plot_3(self):
        plot_3_0 = load("images\\plot\\plot_3_0.png")
        plot_3_0 = scale(plot_3_0, (1280, 720))
        screen.blit(plot_3_0, (0,0)) # 發現我們其實是自己人後，Bamboo向你道歉，並將出口恢復成原樣。於是你和foxyy最後終於到達四樓了，但是，在準備進入電腦教室前，突然有人從教室裡走出來，他是剛才電神旁的小弟。
        update()
        check_mouse()
    def plot_4(self):
        plot_4_0 = load("images\\plot\\plot_4_0.png")
        plot_4_0 = scale(plot_4_0, (1280, 720))
        screen.blit(plot_4_0, (0,0)) # 你不了解她說的意思，直到看見她手中的閃電，你才終於發現了異常。foxyy脱去女裝，周圍爆發出閃電
        update()
        check_mouse()
    def plot_5(self):
        plot_5_0 = load("images\\plot\\plot_5_0.png")
        plot_5_0 = scale(plot_5_0, (1280, 720))
        screen.blit(plot_5_0.jpg, (0,0)) # 之後，你成為了下一任電神，在你的帶領之下，組織不再繼續作亂，反而變成喜歡不斷的教導程式能力，培養人才的組織，這就是我們現在的社團—CRC電算社
        update()
        check_mouse()


class Dialogue :
    def dia_1(self):
        dia_1_0 = load("images\\dia\\dia_1_0.png")
        dia_1_1 = load("images\\dia\\dia_1_1.png")
        dia_1_2 = load("images\\dia\\dia_1_2.png")
        dia_1_0 = scale(dia_1_0, (1280, 720))
        dia_1_1 = scale(dia_1_1, (1280, 720))
        dia_1_2 = scale(dia_1_2, (1280, 720))
        # screen.blit(diangod_image, (0,0)) # 電神輕視表情
        update()
        check_mouse()
        screen.blit(dia_1_0, (0,0)) # 電神：「又有挑戰者了嗎？」
        update()
        check_mouse()
        # screen.blit(player_image, (0,0)) # 玩家皺眉表情
        update()
        check_mouse()
        screen.blit(dia_1_1, (0,0)) # （你皺了皺眉，聽不太懂他的意思）
        update()
        check_mouse()
        # screen.blit(diangod_image, (0,0)) # 電神得意表情
        update()
        check_mouse()
        screen.blit(dia_1_2, (0,0)) # 電神：「沒關係，準備被電爆吧。」
        update()
        check_mouse()
    def dia_2(self):
        dia_2_0 = load("images\\dia\\dia_2_0.png")
        dia_2_1 = load("images\\dia\\dia_2_1.png")
        dia_2_2 = load("images\\dia\\dia_2_2.png")
        dia_2_3 = load("images\\dia\\dia_2_3.png")
        dia_2_0 = scale(dia_2_0, (1280, 720))
        dia_2_1 = scale(dia_2_1, (1280, 720))
        dia_2_2 = scale(dia_2_2, (1280, 720))
        dia_2_3 = scale(dia_2_3, (1280, 720))
        # screen.blit(bright_image, (0,0))
        update()
        check_mouse()
        screen.blit(dia_2_0, (0,0)) # Bright：「你剛剛和他戰鬥了吧！」
        update()
        check_mouse()
        # screen.blit(player_image, (0,0))
        update()
        check_mouse()
        screen.blit(dia_2_1, (0,0)) # 你：「他？指在四樓的那個閃電人嗎？」or 「對啊，他究竟是誰啊？」
        update()
        check_mouse()
        # screen.blit(bright_image, (0,0))
        update()
        check_mouse()
        screen.blit(dia_2_2, (0,0)) # Bright:「呵呵，他是《電神》是我們組織的統治者」
        update()
        check_mouse()
        # screen.blit(player_image, (0,0))
        update()
        check_mouse()
        screen.blit(dia_2_3, (0,0)) # 你：「組織？什麼組織」
        update()
        check_mouse()
    def dia_3(self):
        dia_3_0 = load("images\\dia\\dia_3_0.png")
        dia_3_1 = load("images\\dia\\dia_3_1.png")
        dia_3_2 = load("images\\dia\\dia_3_2.png")
        dia_3_3 = load("images\\dia\\dia_3_3.png")
        dia_3_4 = load("images\\dia\\dia_3_4.png")
        dia_3_5 = load("images\\dia\\dia_3_5.png")
        dia_3_6 = load("images\\dia\\dia_3_6.png")
        dia_3_0 = scale(dia_3_0, (1280, 720))
        dia_3_1 = scale(dia_3_1, (1280, 720))
        dia_3_2 = scale(dia_3_2, (1280, 720))
        dia_3_3 = scale(dia_3_3, (1280, 720))
        dia_3_4 = scale(dia_3_4, (1280, 720))
        dia_3_5 = scale(dia_3_5, (1280, 720))
        dia_3_6 = scale(dia_3_6, (1280, 720))
        # screen.blit(foxyy_image, (0,0)) # foxyy 開心表情
        update()
        check_mouse()
        screen.blit(dia_3_0, (0,0)) # foxyy：「我們是CRC！」
        update()
        check_mouse()
        screen.blit(playerbright_image, (0,0)) # player 和 bright 若有所思
        update()
        check_mouse()
        screen.blit(dia_3_1, (0,0)) # (看著突然出現的女子，你跟Bright都若有所思）
        update()
        check_mouse()
        # screen.blit(player_image, (0,0)) # player 驚嚇表情
        update()
        check_mouse()
        screen.blit(dia_3_2, (0,0)) # 你：（怎麼突然有人冒出來）
        update()
        check_mouse()
        # screen.blit(bright_image, (0,0)) # bright 驚嚇表情
        update()
        check_mouse()
        screen.blit(dia_3_3, (0,0)) # Bright：（他…怎麼會出現在這裡）
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 開心表情
        update()
        check_mouse()
        screen.blit(dia_3_4, (0,0)) # foxyy：「CRC，又稱為電算社，我們擁有能改變世界的電算之力！」
        update()
        check_mouse()
        screen.blit(dia_3_5, (0,0)) # foxyy：「簡單來說，就是程式設計。如果精通這項能力，就會擁有很強大的力量，例如發射閃電之類的喔！」
        update()
        check_mouse()
        screen.blit(player_image, (0,0)) # player 和 bright 開心表情
        update()
        check_mouse()
        screen.blit(dia_3_6, (0,0)) # （你聽完後對程式擁有了更濃厚的興趣，同時Bright似乎也有意教導你）
        update()
        check_mouse()
    def dia_4(self):
        dia_4_0 = load("images\\dia\\dia_4_0.png")
        dia_4_1 = load("images\\dia\\dia_4_1.png")
        dia_4_2 = load("images\\dia\\dia_4_2.png")
        dia_4_0 = scale(dia_4_0, (1280, 720))
        dia_4_1 = scale(dia_4_1, (1280, 720))
        dia_4_2 = scale(dia_4_2, (1280, 720))
        # screen.blit(bright_image, (0,0)) # bright 得意表情
        update()
        check_mouse()
        screen.blit(dia_4_0, (0,0)) # Bright：「我可是教導程式的高手呢！只要十分鐘，我便能把所有的基礎都教會你！」
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 可愛表情
        update()
        check_mouse()
        screen.blit(dia_4_1, (0,0)) # foxyy：「人家也來幫你吧！」
        update()
        check_mouse()
        # screen.blit(player_image, (0,0)) # player 安心表情
        update()
        check_mouse()
        screen.blit(dia_4_2, (0,0)) # （看來這裡還是有很多善良的人呢，你放心了許多）
        update()
        check_mouse()
    def dia_5(self):
        dia_5_0 = load("images\\dia\\dia_5_0.png")
        dia_5_1 = load("images\\dia\\dia_5_1.png")
        dia_5_2 = load("images\\dia\\dia_5_2.png")
        dia_5_0 = scale(dia_5_0, (1280, 720))
        dia_5_1 = scale(dia_5_1, (1280, 720))
        dia_5_2 = scale(dia_5_2, (1280, 720))
        # screen.blit(player_image, (0,0)) # player 電流
        update()
        check_mouse()
        screen.blit(dia_5_0, (0,0)) # （在Bright和foxyy的教導之下，你很快就學會基礎的程式設計，並感覺到有股電流在你的身體裡流竄）
        update()
        check_mouse()
        # screen.blit(bright_image, (0,0)) # bright 開心表情
        update()
        check_mouse()
        screen.blit(dia_5_1, (0,0)) # Bright：「學的這麼快，看來你擁有很強的潛力呢。不過，我能教的都教完了，如果你想學更多，就到三樓去找更多高手請教吧，但是要注意，有些人並不歡迎外人打擾。」
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 驚嚇表情
        update()
        check_mouse()
        screen.blit(dia_5_2, (0,0)) # foxyy：「放心，人家會陪著你上去~」
        update()
        check_mouse()
    def dia_6(self):
        dia_6_0 = load("images\\dia\\dia_6_0.png")
        dia_6_1 = load("images\\dia\\dia_6_1.png")
        dia_6_2 = load("images\\dia\\dia_6_2.png")
        dia_6_3 = load("images\\dia\\dia_6_3.png")
        dia_6_4 = load("images\\dia\\dia_6_4.png")
        dia_6_5 = load("images\\dia\\dia_6_5.png")
        dia_6_6 = load("images\\dia\\dia_6_6.png")
        dia_6_7 = load("images\\dia\\dia_6_7.png")
        dia_6_8 = load("images\\dia\\dia_6_8.png")
        dia_6_9 = load("images\\dia\\dia_6_9.png")
        dia_6_10 = load("images\\dia\\dia_6_10.png")
        dia_6_11 = load("images\\dia\\dia_6_11.png")
        dia_6_12 = load("images\\dia\\dia_6_12.png")
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
        update()
        check_mouse()
        screen.blit(dia_6_0, (0,0)) # （你和foxyy來到了三樓）
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 開心表情
        update()
        check_mouse()
        screen.blit(dia_6_1, (0,0)) # foxyy：「我們去右邊的教室吧！」
        update()
        check_mouse()
        # screen.blit(bamboo_image, (0,0)) # bamboo 殺氣背影配刀
        update()
        check_mouse()
        screen.blit(dia_6_2, (0,0)) # (一進去教室，你看到有名女子正坐在講桌電腦旁擦著手上的刀)
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 普通表情
        update()
        check_mouse()
        screen.blit(dia_6_3, (0,0)) # foxyy:是學術組的Bamboo，看來真的遇到高手了
        update()
        check_mouse()
        # screen.blit(bamboo_image, (0,0)) # bamboo 殺氣臉
        update()
        check_mouse()
        screen.blit(dia_6_4, (0,0)) # (Bamboo望了你們一眼）
        update()
        check_mouse()
        screen.blit(dia_6_5, (0,0)) # Bamboo:「怎麼會有外人前來拜訪」
        update()
        check_mouse()
        # screen.blit(player_image, (0,0)) # player 普通表情
        update()
        check_mouse()
        screen.blit(dia_6_6, (0,0)) # 你：「早安，為了雪恥，請教我更進階的程式以面對電神，請885」or「ㄜ...我來學精深的程式，助我打敗電神」
        update()
        check_mouse()
        # screen.blit(bamboo_image, (0,0)) # bamboo 殺氣表情
        update()
        check_mouse()
        screen.blit(dia_6_7, (0,0)) # Bamboo:「聽你一說，你想請託我協助你們挑戰電神？所以你們其實是入侵者吧」
        update()
        check_mouse()
        # screen.blit(foxyybamboo_image, (0,0)) # foxyy 冒汗表情 bamboo 握刀       
        update()
        check_mouse()
        screen.blit(dia_6_8, (0,0)) # （foxyy正想解釋，但Bamboo已經拔刀奔來）
        update()
        check_mouse()
        # screen.blit(bamboo_image, (0,0)) # bamboo 殺氣表情
        update()
        check_mouse()
        screen.blit(dia_6_9, (0,0)) # Bamboo:「沒想到你們竟能從電神手中逃過一劫，不過在下是不會放過任何入侵者的」
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 冒汗表情
        update()
        check_mouse()
        screen.blit(dia_6_10, (0,0)) # foxyy:「（指著門）快點離開，危險！」
        update()
        check_mouse()
        # screen.blit(bamboo_image, (0,0)) # bamboo 殺氣表情
        update()
        check_mouse()
        screen.blit(dia_6_11, (0,0)) # Bamboo:「別想逃，”竹林叢生”」
        update()
        check_mouse()
        # screen.blit(manybamboo_image, (0,0)) # 一堆竹子
        update()
        check_mouse()
        screen.blit(dia_6_12, (0,0)) # （門口前瞬間長出一堆竹子，賭住了唯一的出口，看來只能戰鬥了）
        update()
        check_mouse()
    def dia_7(self):
        dia_7_0 = load("images\\dia\\dia_7_0.png")
        dia_7_1 = load("images\\dia\\dia_7_1.png")
        dia_7_2 = load("images\\dia\\dia_7_2.png")
        dia_7_3 = load("images\\dia\\dia_7_3.png")
        dia_7_4 = load("images\\dia\\dia_7_4.png")
        dia_7_5 = load("images\\dia\\dia_7_5.png")
        dia_7_6 = load("images\\dia\\dia_7_6.png")
        dia_7_7 = load("images\\dia\\dia_7_7.png")
        dia_7_8 = load("images\\dia\\dia_7_8.png")
        dia_7_9 = load("images\\dia\\dia_7_9.png")
        dia_7_10 = load("images\\dia\\dia_7_10.png")
        dia_7_11 = load("images\\dia\\dia_7_11.png")
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
        update()
        check_mouse()
        screen.blit(dia_7_0, (0,0)) # （你不斷閃過Bamboo的斬擊，Bamboo開始感到心急）
        update()
        check_mouse()
        # screen.blit(bamboo_image, (0,0)) # bamboo 憤怒表情
        update()
        check_mouse()
        screen.blit(dia_7_1, (0,0)) # Bamboo:可惡，區區入侵者在下居然不能解決
        update()
        check_mouse()
        screen.blit(dia_7_2, (0,0)) # Bamboo:《程式枷鎖》
        update()
        check_mouse()
        # screen.blit(playerRRR_image, (0,0)) # player + 枷鎖
        update()
        check_mouse()
        screen.blit(dia_7_3, (0,0)) # （突然有一條寫滿程式的繩子將你綁住，使你無法動彈）
        update()
        check_mouse()
        # screen.blit(player_image, (0,0)) # player 問號表情
        update()
        check_mouse()
        screen.blit(dia_7_4, (0,0)) # 你：「這是什麼東西」
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 嚴肅表情
        update()
        check_mouse()
        screen.blit(dia_7_5, (0,0)) # foxyy:「程式枷鎖⋯⋯，除非你找出這程式的bug，否則這不會解開」
        update()
        check_mouse()
        # screen.blit(bamboo_image, (0,0)) # bamboo 殺氣表情
        update()
        check_mouse()
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
        update()
        check_mouse()
        screen.blit(dia_7_9, (0,0)) # foxyy:「這種程式，找出bug有什麼難的」
        update()
        check_mouse()
        # screen.blit(bamboo_image, (0,0)) # bamboo 驚訝表情
        update()
        check_mouse()
        screen.blit(dia_7_10, (0,0)) # （Bamboo驚訝的看著foxyy，過了幾秒後發現原來foxyy其實是自己人）
        update()
        check_mouse()
        screen.blit(dia_7_11, (0,0)) # Bamboo:原來是foxyy，這代表你不是入侵者吧
        update()
        check_mouse()
    def dia_8(self):
        dia_8_0 = load("images\\dia\\dia_8_0.png")
        dia_8_1 = load("images\\dia\\dia_8_1.png")
        dia_8_0 = scale(dia_8_0, (1280, 720))
        dia_8_1 = scale(dia_8_1, (1280, 720))
        # screen.blit(fire_image, (0,0)) # fire 輕視表情
        update()
        check_mouse()
        screen.blit(dia_8_0, (0,0)) # Fire:「你怎麼又上來了，還想再被電爆嗎？」
        update()
        check_mouse()
        screen.blit(dia_8_1, (0,0)) # Fire:「以你這種程度，根本不用電神出馬，我一個人就能解決你了」
        update()
        check_mouse()
    def dia_9(self):
        dia_9_0 = load("images\\dia\\dia_9_0.png")
        dia_9_0 = scale(dia_9_0, (1280, 720))
        # screen.blit(fire_image, (0,0)) # fire 驚訝表情
        update()
        check_mouse()
        screen.blit(dia_9_0, (0,0)) # Fire:「沒想到你竟然能答出這些問題⋯，是我太大意了⋯⋯」
        update()
        check_mouse()
    def dia_10(self):
        dia_10_0 = load("images\\dia\\dia_10_0.png")
        dia_10_1 = load("images\\dia\\dia_10_1.png")
        dia_10_2 = load("images\\dia\\dia_10_2.png")
        dia_10_3 = load("images\\dia\\dia_10_3.png")
        dia_10_4 = load("images\\dia\\dia_10_4.png")
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
        update()
        check_mouse()
        screen.blit(dia_10_2, (0,0)) # foxyy:「電神？他現在正在這間教室裡啊」
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 女裝
        update()
        check_mouse()
        screen.blit(dia_10_3, (0,0)) # 你不了解她說的意思，直到看見她手中的閃電，你才終於發現了異常。foxyy脱去女裝，周圍爆發出閃電
        update()
        check_mouse()
        screen.blit(dia_10_4, (0,0)) # foxyy:「好了，你的實力已經增強不少了，真是另人期待，開始最後的戰鬥吧！」
        update()
        check_mouse()
    def dia_11(self):
        dia_11_0 = load("images\\dia\\dia_11_0.png")
        dia_11_1 = load("images\\dia\\dia_11_1.png")
        dia_11_2 = load("images\\dia\\dia_11_2.png")
        dia_11_3 = load("images\\dia\\dia_11_3.png")
        dia_11_0 = scale(dia_11_0, (1280, 720))
        dia_11_1 = scale(dia_11_1, (1280, 720))
        dia_11_2 = scale(dia_11_2, (1280, 720))
        dia_11_3 = scale(dia_11_3, (1280, 720))
        # screen.blit(foxyy_image, (0,0)) # foxyy 倒地
        update()
        check_mouse()
        screen.blit(dia_11_0, (0,0)) # （你歷經了千辛萬苦，終於在最後一刻找到機會電爆foxyy，foxyy倒地不起）
        update()
        check_mouse()
        screen.blit(dia_11_1, (0,0)) # foxyy:我⋯竟然輸了
        update()
        check_mouse()
        # screen.blit(foxyy_image, (0,0)) # foxyy 欣慰表情
        update()
        check_mouse()
        screen.blit(dia_11_2, (0,0)) # （foxyy臉上並未出現任何不甘和憤怒，反而欣慰的笑了）
        update()
        check_mouse()
        screen.blit(dia_11_3, (0,0)) # foxyy:「我就知道你有這個潛力，當初放你一馬並教導你，就是為了激發深藏在你體內的電算之力，CRC之後就交給你了」
        update()
        check_mouse()