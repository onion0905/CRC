import tkinter as tk
import tkinter.messagebox as msg

class Q2():
    def __init__(self):
        self.base = tk.Tk()
        self.base.title("問題四")
        self.text = tk.StringVar()
        self.base.geometry("800x650")
        self.proc = 0
        self.choose = False
        # beware, there are lots of space in the text
        self.t = '''
現在 foxyy 拿出一排重量不一的蘋果排成一列，但他們的大小並不一樣，
你只知道他們已經把蘋果按照重量由左至右排序過了。
你剛跟電神戰鬥完，突然感到口乾舌燥，急著想拿一顆蘋果吃掉，
但 foxyy 想到了一個好玩的遊戲。他請你找到一顆重量剛剛好為 w 的蘋果，當你找到它就可以把它吃掉。
因為你快渴死了，所以你想要在最快時間內找到 foxyy 指定的蘋果。
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
        msg.showerror("哎呀錯ㄌ", "你正準備這樣做的時候，Foxyy 趕快跳出來阻止你這麼做\n因為在你找到對的蘋果之前，你會因為找太久就渴死了。\n再看看有沒有更快的搜尋方法吧！")
    def op2(self):
        msg.showerror("哎呀錯ㄌ", "Foxxy 都快哭了，他好不容易幫你照重量排序好結果又被你打亂了！\n大小跟重量沒有絕對關係，所以不能用大小來判斷重量啦！\n好在好心的 Foxyy 又幫你把蘋果照重量排序好了，再試另一個答案吧！")
    def op3(self):
        msg.showinfo("恭喜答對:D", "好耶你答對了，你吃到了 foxxy 精心幫你挑選最好吃的蘋果！")
        self.base.destroy()
    def op4(self):
        msg.showerror("哎呀錯ㄌ", "Foxxy 苦著臉拜託你好好看完選項再應答\n也千萬不要想著靠他幼稚園就會的東西把他電爛，那是不可能的事的啦！")

q2 = Q2()