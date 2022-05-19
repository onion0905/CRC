import tkinter as tk
import tkinter.messagebox as msg

class Q2():
    def __init__(self):
        self.base = tk.Tk()
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

q2 = Q2()