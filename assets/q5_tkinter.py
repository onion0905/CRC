import tkinter as tk
import tkinter.messagebox as msg

class Q5():
    def __init__(self):
        self.base = tk.Tk()
        self.base.title("最終決戰！！！！")
        self.text = tk.StringVar()
        self.base.geometry("600x400")
        self.proc = 0
        self.choose = False
        # beware, there are lots of space in the text
        self.t = '''
Foxyy / 電神狂妄地笑著，他準備拿他幼稚園就會的雜湊來電爛你。
請運用你的計算能力算出 Foxyy / 電神究竟說了些什麼！

已知一個英文字（例：car）是由一個一個英文字母所組成
我們定義 w_1 是字串中倒數第一個字母，w_2 是字串中倒數第二個字母...
而各個英文字母會被轉換成它在 alphabet 裡的順序，如 'a' = 1。
則 car 的 w_1 = 18, w_2 = 1, w_3 = 3
它會被雜湊成 w_1 * p^1 + w_2 * p^2 + w_3 * p^3 +...
若 p = 31，則雜湊值為 18 * (31^1) + 1 * (31^2) + 3 * (31^3) = 90892。

Foxyy / 電神現在對你說 "3963598"，請問他是什麼意思？
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
        msg.showerror("哎呀錯ㄌ", "沒有油飯可以卡啦 > <，自己想辦法去找油飯")
    def op2(self):
        msg.showerror("哎呀錯ㄌ", "拉麵好ㄘ，但答案不是這個ㄛ")

    def op3(self):
        msg.showerror("哎呀錯ㄌ", "你不弱 :angry:")
    def op4(self):
        msg.showinfo("恭喜答對:D", "沒錯！你真電~~~")
        self.base.destroy()

q5 = Q5()