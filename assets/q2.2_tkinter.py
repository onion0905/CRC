import tkinter as tk
import tkinter.messagebox as msg

class Q2():
    def __init__(self):
        self.base = tk.Tk()
        self.base.title("問題三")
        self.text = tk.StringVar()
        self.base.geometry("600x500")
        self.proc = 0
        self.choose = False
        # beware, there are lots of space in the text
        self.t = '''
有了變數的基礎，Foxyy 請你實作「拿出一個兩位數的兩個數字、分別輸出」。
a 為該兩位數，現在請你輸出 a 的十位數和個位數，中間輸出一個空格，行尾輸出空格。
Foxyy 先幫你寫好了一些 code，如下：

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

q2 = Q2()