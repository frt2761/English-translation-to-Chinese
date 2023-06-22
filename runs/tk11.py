from tkinter import *
import subprocess
from tkinter import Tk
def run_another_file():
    subprocess.Popen(['python', 'translation.py'])

# 初始化，画布大小
root = Tk()
root.geometry('340x540')
# 调用翻译
# 文字提示
lb2 = Label(root, text="输入需要翻译的文本")
lb2.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.05)

# 输入需要翻译的文本
inp3 = Entry(root)
inp3.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.15)

# 翻译按钮
btn1 = Button(root, text='翻译', command=run_another_file())
btn1.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.1)

# 翻译的结果
txt = Text(root)
txt.place(rely=0.7, relheight=0.2)

root.mainloop()
