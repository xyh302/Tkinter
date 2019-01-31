# 创建两个不同的组
from tkinter import *
from tkinter import ttk
import os

path = os.getcwd()+"\\number.txt"

alist = []

for i in range(10):
    for j in range(i, 10):
        for k in range(j, 10):
            for l in range(k, 10):
                num = (str(i)+str(j)+str(k)+str(l))
                alist.append(num)


def callCheckbutton1():
    print(alist)


def callCheckbutton2():
    alist2 = []
    for eachNumber in alist:
        for i,ele in enumerate(eachNumber):
            if i > 0 and ele == eachNumber[i-1]:
                if eachNumber not in alist2:
                    alist2.append(eachNumber)
                continue
    for i in alist2:
        alist.remove(i)
    print(alist)
           

def callCheckbutton4(event):
    var = comb.get()
    alist2 = []
    for i in alist:
        if var in i:
            alist2.append(i)
    for i in alist2:
        alist.remove(i)
    print(alist,"callCheckbutton4")


def callCheckbutton5(event):
    global alist
    var = comb5.get()
    alist2 = []
    for i in alist:
        if var in i:
            alist2.append(i)
    print(alist2,"callCheckbutton5")
    alist = alist2


def callCheckbutton6(event):
    global alist
    var = comb6.get()
    alist2 = []
    for i in alist:
        if int(i[0])+int(i[1])+int(i[2])+int(i[3]) < int(var ):
            alist2.append(i)
    print(alist2,"callCheckbutton6")
    alist = alist2


def callCheckbutton7(event):
    global alist
    var = comb7.get()
    alist2 = []
    for i in alist:
        if int(i[0])+int(i[1])+int(i[2])+int(i[3]) > int(var):
            alist2.append(i)
    print(alist2,"callCheckbutton7")
    alist = alist2


def callCheckbutton8(event):
    var = comb8.get()
    var1 = comb8_2.get()
    alist2 = []
    print(var, var1)
    for i in alist:
        if var in i and var1 in i:
            alist2.append(i)
    for i in alist2:
        alist.remove(i)
    print(alist,"callCheckbutton8")


def callCheckbutton9(event):
    global alist
    var = comb9.get()
    alist2 = []
    for i in alist:
        if var in i:
            alist2.append(i)
    print(alist2,"alist")
    alist = alist2


def run1():
    with open(path, "w+") as f:
        for i in alist:
            f.write(i)
            f.write("\r\n")
 
root = Tk()
root.title('数字生成器')

v = StringVar()

vlang = IntVar()
vos = IntVar()
vlang.set(1)  # 第一个组初始值为1
vos.set(2)  # 第一个组初始值为2
# 创建两个组，不同的组，各个按钮互不影响。
Label(root, text="为避免发生错误，以下9个条件，请从上到下进行选择").grid()
Label(root, text="第一项默认必选，第2-9项不填默认不选").grid()
Label(root, text="").grid()
Checkbutton(root, text="1.A(0...9)/B(0...9)C(0...9)D(0...9);(四个数都是0-9中选择;)", command=callCheckbutton1).grid()
Checkbutton(root, text="2.A=B不等于C、D;(只允许两个数相同)", command=callCheckbutton2).grid()
Checkbutton(root, text="3.A不等于B不等于C不等于D(四个数不同)", command=callCheckbutton2).grid()

Label(root, text="4.A\B\C\D排除掉一个数,请输入你要排除的数字：").grid()
comb = ttk.Combobox(root,values=[0,1,2,3,4,5,6,7,8,9])
comb.grid()
comb.bind("<<ComboboxSelected>>",callCheckbutton4)

Label(root, text="5.A\B\C\D中必有一个数,请输入必有的数字：").grid()
comb5 = ttk.Combobox(root,values=[0,1,2,3,4,5,6,7,8,9])
comb5.grid()
comb5.bind("<<ComboboxSelected>>",callCheckbutton5)

Label(root, text="6.四个数之和小于多少，请输入你希望小于的数字：").grid()
comb6 = ttk.Combobox(root,values=[x for x in range(37)])
comb6.grid()
comb6.bind("<<ComboboxSelected>>",callCheckbutton6)

Label(root, text="7.四个数之和大于多少，请输入你希望大于的数字：").grid()
comb7 = ttk.Combobox(root,values=[x for x in range(37)])
comb7.grid()
comb7.bind("<<ComboboxSelected>>",callCheckbutton7)

Label(root, text="8.A\B\C\D不能同时存在的两个数，请输入你选择的第一个数：").grid()
comb8 = ttk.Combobox(root,values=[0,1,2,3,4,5,6,7,8,9])
comb8.grid()
#comb8.bind("<<ComboboxSelected>>",callCheckbutton8)
comb8_2 = ttk.Combobox(root,values=[0,1,2,3,4,5,6,7,8,9])
comb8_2.grid()
comb8_2.bind("<<ComboboxSelected>>",callCheckbutton8)

Label(root, text="9.A\B\C\D中存在(1、2、3)三者之一,请输入第一个数：").grid()
comb9 = ttk.Combobox(root,values=[1,2,3])
comb9.grid()
comb9.bind("<<ComboboxSelected>>",callCheckbutton9)

Button(root, text='确定(点击确定查看结果)', command=run1).grid()
lbl = Label(root,text='结果写入桌面的number.txt')
lbl.grid()

 
root.mainloop()

