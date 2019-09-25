# 创建两个不同的组
from tkinter import *
from tkinter import ttk
import os

path = os.getcwd() + "\\number.txt"

alist = []

for i in range(10):
    for j in range(i, 10):
        for k in range(j, 10):
            for l in range(k, 10):
                num = (str(i) + str(j) + str(k) + str(l))
                alist.append(num)


def callCheckbutton1():
    print(alist)


def callCheckbutton2():
    alist2 = []
    for i in alist:
        for j in i:
            if i.count(j) > 2:
                if i not in alist2:
                    alist2.append(i)
                    continue
    for i in alist2:
        alist.remove(i)
    print(alist)


def callCheckbutton3():
    alist2 = []
    for eachNumber in alist:
        for i, ele in enumerate(eachNumber):
            if i > 0 and ele == eachNumber[i - 1]:
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
    print(alist, var, "callCheckbutton4")


def callCheckbutton4_2(event):
    var = comb2.get()
    alist2 = []
    for i in alist:
        if var in i:
            alist2.append(i)
    for i in alist2:
        alist.remove(i)
    print(alist, var, "callCheckbutton4_2")


def callCheckbutton4_3(event):
    var = comb3.get()
    alist2 = []
    for i in alist:
        if var in i:
            alist2.append(i)
    for i in alist2:
        alist.remove(i)
    print(alist, var, "callCheckbutton4_3")


def callCheckbutton4_4(event):
    var = comb4.get()
    alist2 = []
    for i in alist:
        if var in i:
            alist2.append(i)
    for i in alist2:
        alist.remove(i)
    print(alist, var, "callCheckbutton4_4")


def callCheckbutton5(event):
    global alist
    var = comb5.get()
    alist2 = []
    for i in alist:
        if var in i:
            alist2.append(i)
    print(alist2, var, "callCheckbutton5")
    alist = alist2


def callCheckbutton5_2(event):
    global alist
    var = comb5_2.get()
    alist2 = []
    for i in alist:
        if var in i:
            alist2.append(i)
    print(alist2, var, "callCheckbutton5_2")
    alist = alist2


def callCheckbutton5_3(event):
    global alist
    var = comb5_3.get()
    alist2 = []
    for i in alist:
        if var in i:
            alist2.append(i)
    print(alist2, var, "callCheckbutton5_3")
    alist = alist2


def callCheckbutton6(event):
    global alist
    var = comb6.get()
    alist2 = []
    for i in alist:
        if int(i[0]) + int(i[1]) + int(i[2]) + int(i[3]) < int(var):
            alist2.append(i)
    print(alist2, "callCheckbutton6")
    alist = alist2


def callCheckbutton7(event):
    global alist
    var = comb7.get()
    alist2 = []
    for i in alist:
        if int(i[0]) + int(i[1]) + int(i[2]) + int(i[3]) > int(var):
            alist2.append(i)
    print(alist2, "callCheckbutton7")
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
    print(alist, "callCheckbutton8")


def callCheckbutton8_3(event):
    var = comb8_3.get()
    var1 = comb8_4.get()
    alist2 = []
    print(var, var1)
    if var == '':
        print("第一个数为空")
    else:
        for i in alist:
            if var in i and var1 in i:
                alist2.append(i)
        for i in alist2:
            alist.remove(i)
    print(alist, "callCheckbutton8_3")


def callCheckbutton8_5(event):
    var = comb8_5.get()
    var1 = comb8_6.get()
    alist2 = []
    print(var, var1)
    if var == '':
        print("第一个数为空")
    else:
        for i in alist:
            if var in i and var1 in i:
                alist2.append(i)
        for i in alist2:
            alist.remove(i)
    print(alist, "callCheckbutton8_5")


def callCheckbutton8_7(event):
    var = comb8_7.get()
    var1 = comb8_8.get()
    alist2 = []
    print(var, var1)
    for i in alist:
        if var in i and var1 in i:
            alist2.append(i)
    for i in alist2:
        alist.remove(i)
    print(alist, "callCheckbutton8_7")


# def callCheckbutton9():
#     global alist
#     var = t1.get()
#     a,b,c = var.split(',')
#     alist2 = []
#     for i in alist:
#         if a in i and b not in i and c not in i:
#             alist2.append(i)
#         if b in i and a not in i and c not in i:
#             alist2.append(i)
#         if c in i and a not in i and b not in i:
#             alist2.append(i)
#     alist = alist2
#     print(alist, "callCheckbutton9")


def callCheckbutton9(event):
    global alist
    a = comb9.get()
    b = comb9_2.get()
    c = comb9_3.get()

    alist2 = []
    for i in alist:
        if a in i and b not in i and c not in i:
            alist2.append(i)
        if b in i and a not in i and c not in i:
            alist2.append(i)
        if c in i and a not in i and b not in i:
            alist2.append(i)
    alist = alist2
    print(alist, "callCheckbutton9")


def clear():
    lb.delete(0, 800)  # 最多只有715个数字，清空800个


def run1():
    print(len(alist),alist)
    # value1.set(alist)
    for j in range(0,len(alist),15):
        lb.insert(END, alist[j:j+15])
    with open(path, "w+") as f:
        for i in alist:
            f.write(i)
            f.write("\r\n")


root = Tk()
root.title('Number Generator')
root.geometry("1000x600")

value1 = StringVar()
value1.set('')

# 显示区域
show = Label(textvariable=value1, anchor='nw', bg='white', font=('宋体', 10), bd=10)
show.place(x=500, y=10, width=500, height=550)

var = StringVar()
lb = Listbox(root,  listvariable=var)
lb.place(x=500, y=10, width=1000, height=550)

# 创建两个组，不同的组，各个按钮互不影响。
Label(root, text="为避免发生错误，以下9个条件，请从上到下进行选择").place(x=-33, y=12, width=500, height=20)
Label(root, text="").grid()
Checkbutton(root, text="1.A(0...9)/B(0...9)C(0...9)D(0...9);(四个数都是0-9中选择;)", command=callCheckbutton1).place(x=-15, y=39, width=500, height=20)
Checkbutton(root, text="2.A=B不等于C、D;(只允许两个数相同)", command=callCheckbutton2).place(x=-62, y=62, width=500, height=20)
Checkbutton(root, text="3.A不等于B不等于C不等于D(四个数不同)", command=callCheckbutton3).place(x=-56, y=85, width=500, height=20)

Label(root, text="4.A\B\C\D排除掉一个数,请输入你要排除的数字：").place(x=-43, y=108, width=500, height=20)
comb = ttk.Combobox(root, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb.place(x=75, y=131, width=40, height=20)
comb.bind("<<ComboboxSelected>>", callCheckbutton4)

comb2 = ttk.Combobox(root, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb2.place(x=75, y=154, width=40, height=20)
comb2.bind("<<ComboboxSelected>>", callCheckbutton4_2)

comb3 = ttk.Combobox(root, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb3.place(x=75, y=177, width=40, height=20)
comb3.bind("<<ComboboxSelected>>", callCheckbutton4_3)

comb4 = ttk.Combobox(root, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb4.place(x=75, y=200, width=40, height=20)
comb4.bind("<<ComboboxSelected>>", callCheckbutton4_4)

Label(root, text="5.A\B\C\D中必有一个数,请输入必有的数字：").place(x=-55, y=223, width=500, height=20)
comb5 = ttk.Combobox(root, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb5.place(x=75, y=246, width=40, height=20)
comb5.bind("<<ComboboxSelected>>", callCheckbutton5)

comb5_2 = ttk.Combobox(root, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb5_2.place(x=75, y=269, width=40, height=20)
comb5_2.bind("<<ComboboxSelected>>", callCheckbutton5_2)

comb5_3 = ttk.Combobox(root, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb5_3.place(x=75, y=292, width=40, height=20)
comb5_3.bind("<<ComboboxSelected>>", callCheckbutton5_3)

Label(root, text="6.四个数之和小于多少，请输入你希望小于的数字：").place(x=-40, y=315, width=500, height=20)
comb6 = ttk.Combobox(root, values=[x for x in range(37)])
comb6.place(x=75, y=337, width=40, height=20)
comb6.bind("<<ComboboxSelected>>", callCheckbutton6)

Label(root, text="7.四个数之和大于多少，请输入你希望大于的数字：").place(x=-20, y=360, width=460, height=20)
comb7 = ttk.Combobox(root, values=[x for x in range(37)])
comb7.place(x=75, y=383, width=40, height=20)
comb7.bind("<<ComboboxSelected>>", callCheckbutton7)

Label(root, text="8.A\B\C\D不能同时存在的两个数,输入选择的两个数：(每一排对应两个数字)").place(x=57, y=406, width=440, height=20)
comb8 = ttk.Combobox(root, width=15, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb8.place(x=75, y=429, width=40, height=20)
comb8_2 = ttk.Combobox(root, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb8_2.place(x=210, y=429, width=40, height=20)
comb8_2.bind("<<ComboboxSelected>>", callCheckbutton8)
comb8_3 = ttk.Combobox(root, width=15, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb8_3.place(x=75, y=452, width=40, height=20)
comb8_4 = ttk.Combobox(root, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb8_4.place(x=210, y=452, width=40, height=20)
comb8_4.bind("<<ComboboxSelected>>", callCheckbutton8_3)
comb8_5 = ttk.Combobox(root, width=15, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb8_5.place(x=75, y=475, width=40, height=20)
comb8_6 = ttk.Combobox(root, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb8_6.place(x=210, y=475, width=40, height=20)
comb8_6.bind("<<ComboboxSelected>>", callCheckbutton8_5)
comb8_7 = ttk.Combobox(root, width=15, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb8_7.place(x=75, y=498, width=40, height=20)
comb8_8 = ttk.Combobox(root, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb8_8.place(x=210, y=498, width=40, height=20)
comb8_8.bind("<<ComboboxSelected>>", callCheckbutton8_7)


Label(root, text="9.A\B\C\D中存在下列数之一,请手动输入这三个数：").place(x=-35, y=520, width=500, height=20)
comb9 = ttk.Combobox(root, width=14, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb9.place(x=75, y=542, width=40, height=20)
comb9_2 = ttk.Combobox(root, width=14, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb9_2.place(x=210, y=542, width=40, height=20)
comb9_3 = ttk.Combobox(root, width=14, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
comb9_3.place(x=345, y=542, width=40, height=20)
comb9_3.bind("<<ComboboxSelected>>", callCheckbutton9)

Button(root, text='清空结果', command=clear).place(x=650, y=565, width=75, height=30)

Button(root, text='点击查看结果', command=run1).place(x=180, y=565, width=100, height=30)

root.mainloop()
