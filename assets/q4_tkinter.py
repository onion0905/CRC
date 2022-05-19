import tkinter as tk
import tkinter.messagebox as msg

class Q4():
    def __init__(self):
        self.base = tk.Tk()
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

q4 = Q4()