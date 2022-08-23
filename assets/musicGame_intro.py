import tkinter as tk
import tkinter.messagebox as msg

class MusicGameIntro():
    def __init__(self):
        self.base = tk.Tk()
        self.base.title("提示")
        self.text = tk.StringVar()
        self.base.geometry("450x200")
        self.proc = 0
        self.choose = False
        self.t = '''
        接下來 Bamboo 會不斷地向你丟出美乃滋 (不要問為什麼)
        因為美乃滋是一種樂器，所以在美乃滋向你襲來的時候，同時會有音樂播出。
        為了抵擋 Bamboo 的攻擊，你必須接住美乃滋
        按下 d、f、j、k 來接住對應位置的美乃滋吧！ (對啦其實就是音遊)
        ps: 如果你有帶有線耳機的話，接上電腦吧！
        音樂：ウミユリ海底譚 / n-buna
        '''
        
        self.text.set(self.t)
        self.label = tk.Label(self.base, textvariable=self.text)
        self.button = tk.Button(self.base, text = "我懂了", command=self.op4)
        self.label.pack()
        self.button.pack()
        self.base.mainloop()


    def op4(self):
        self.base.destroy()

q2 = MusicGameIntro()