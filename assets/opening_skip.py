import tkinter as tk
import tkinter.messagebox as msg

class OpeningSkip():
    def __init__(self):
        self.base = tk.Tk()
        self.base.title("")
        self.text = tk.StringVar()
        self.base.geometry("200x150")
        self.proc = 0
        self.choose = False
        self.t = '''
        確定跳過前導劇情？
        '''
        
        self.text.set(self.t)
        self.label = tk.Label(self.base, textvariable=self.text)
        self.buttonY = tk.Button(self.base, text = "確定", command=self.yes)
        self.buttonN = tk.Button(self.base, text = "繼續看", command=self.no)
        self.label.pack()
        self.buttonY.pack()
        self.buttonN.pack()
        self.base.mainloop()
        self.skip = False


    def yes(self):
        self.skip = True
        self.base.destroy()

    def no(self):
        self.base.destroy()

q2 = OpeningSkip()