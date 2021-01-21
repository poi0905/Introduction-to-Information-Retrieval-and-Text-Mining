import csv
import tkinter as tk
from tkinter import ttk

# info[i][0] = index; info[i][2] = title; info[i][4] = text; info[i][6] = company; info[i][7] = feature_tag
info = []
with open('C:\\Users\\asdfg\\OneDrive\\桌面\\output1.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    next(rows)
    next(rows)
    for row in rows:
        info.append(row)

company = []
with open('C:\\Users\\asdfg\\OneDrive\\桌面\\oncomp.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    next(rows)
    for row in rows:
        company.append(row)

all_features = []
with open("C:\\Users\\asdfg\\OneDrive\\桌面\\all_feature.txt", 'r', encoding = 'utf8')as file:
    for l in file:
        all_features = l.split()

# 首頁
mainpage = tk.Tk()
mainpage.title("Final Project")
mainpage.geometry("400x300")    # 視窗大小
mainpage.configure(background="#EDCFA9")  # 視窗底色
mainpage.resizable(width=False, height=False)
label = tk.Label(mainpage, text='請問你要執行何種動作？', width=45, height=3,
                 font=('Arial', 12), background="#A47550")
label.grid(row=0, column=0)

# 查詢文章
def search_doc_title():
    first = tk.Toplevel(mainpage)
    first.geometry('750x405')
    first.title('查詢文章')
    first.configure(background="#EDCFA9")  # 視窗底色
    first.resizable(width=False, height=False)

    def click1():
        text.delete('0.0', 'end')
        choice = list1.get()
        count = 0
        for i in range(len(info)):
            if choice == info[i][2]:
                count += 1
        text.insert('insert', '相同標題文章數量:'+str(count)+"\n")
        text.insert('insert', '/' + '\n')
        for i in range(len(info)):
            if choice == info[i][2]:
                text.insert('insert', '文章編號:'+(info[i][0])+"\n")
                text.insert('insert', '-------------------------------------------------------------------------------' + '\n')
                text.insert('insert', (info[i][4]))
                text.insert('insert', '-------------------------------------------------------------------------------' + '\n')
                text.insert('insert', 'Tag:')
                info[i][7] = info[i][7].strip('[')
                info[i][7] = info[i][7].strip(']')
                text.insert('insert', (info[i][7])+"\n")
                text.insert('insert', '===============================================================================' + '\n')
    
    def click2():
        text.delete('0.0', 'end')
        choice = Entry1.get()
        for i in range(len(info)):
            if choice == info[i][0]:
                text.insert('insert', '文章編號:'+(info[i][0])+"\n")
                text.insert('insert', '-------------------------------------------------------------------------------' + '\n')
                text.insert('insert', (info[i][4]))
                text.insert('insert', '-------------------------------------------------------------------------------' + '\n')
                info[i][7] = info[i][7].strip('[')
                info[i][7] = info[i][7].strip(']')
                text.insert('insert', 'Tag:')
                text.insert('insert', (info[i][7])+"\n")

    # 下拉式選單
    # 輸標題的
    label1 = tk.Label(first, text='請選擇你想查詢的文章', font=('Arial', 10), background="#EDCFA9", pady=5)
    label1.grid(row=0, column=0)
    topic = []
    for i in range(len(info)):
        topic.append(info[i][2])
    list1 = ttk.Combobox(first, values = topic)
    list1.grid(row=1, column=0, padx=5)
    button = tk.Button(first, text='送出', command=click1)
    button.grid(row=2, column=0)
    # 輸index的
    Label2 = tk.Label(first, text='文章編號', font=('Arial', 10), background="#EDCFA9", pady=5)
    Label2.grid(row=3, column=0)
    Entry1 = tk.Entry(first, show=None)
    Entry1.grid(row=4, column=0, padx=5)
    button3 = tk.Button(first, text='送出', command=click2)
    button3.grid(row=5, column=0)

    text = tk.Text(first, height=30)
    text.grid(row=0, column=1, columnspan=16, rowspan=16, sticky=tk.W + tk.E + tk.N + tk.S, padx=5, pady=5)

# 查詢tag
def search_tag():
    first = tk.Toplevel(mainpage)
    first.geometry('750x405')
    first.title('查詢tag')
    first.configure(background="#EDCFA9")  # 視窗底色
    first.resizable(width=False, height=False)

    def click1():
        text.delete('0.0', 'end')
        choice = list1.get()
        count = 0
        for i in range(len(info)):
            if choice in info[i][7]:
                count += 1
        text.insert('insert', '相同tag之文章數量:'+str(count)+"\n")
        text.insert('insert', '/' + '\n')
        for i in range(len(info)):
            if choice in info[i][7]:
                text.insert('insert', '文章編號:'+(info[i][0])+"\n")
                text.insert('insert', (info[i][2])+"\n")
                text.insert('insert', '-------------------------------------------------------------------------------' + '\n')
    
    def click2():
        text.delete('0.0', 'end')
        choice = Entry1.get()
        count = 0
        for i in range(len(info)):
            if choice in info[i][7]:
                count += 1
        text.insert('insert', '相同tag之文章數量:'+str(count)+"\n")
        text.insert('insert', '/' + '\n')
        for i in range(len(info)):
            if choice in info[i][7]:
                text.insert('insert', '文章編號:'+(info[i][0])+"\n")
                text.insert('insert', (info[i][2])+"\n")
                text.insert('insert', '-------------------------------------------------------------------------------' + '\n')

    # 下拉式選單
    label1 = tk.Label(first, text='請選擇你想查詢的tag', font=('Arial', 10), background="#EDCFA9", pady=5)
    label1.grid(row=0, column=0)
    list1 = ttk.Combobox(first, values=all_features)
    list1.grid(row=1, column=0, padx=5)
    button = tk.Button(first, text='送出', command=click1)
    button.grid(row=2, column=0)
    # 輸tag的
    Label2 = tk.Label(first, text='tag名稱', font=('Arial', 10), background="#EDCFA9", pady=5)
    Label2.grid(row=3, column=0)
    Entry1 = tk.Entry(first, show=None)
    Entry1.grid(row=4, column=0, padx=5)
    button3 = tk.Button(first, text='送出', command=click2)
    button3.grid(row=5, column=0)

    text = tk.Text(first, height=30)
    text.grid(row=0, column=1, columnspan=16, rowspan=16, sticky=tk.W + tk.E + tk.N + tk.S, padx=5, pady=5)

# 查詢公司
def search_company():
    first = tk.Toplevel(mainpage)
    first.geometry('750x405')
    first.title('查詢公司')
    first.configure(background="#EDCFA9")  # 視窗底色
    first.resizable(width=False, height=False)

    def click1():
        text.delete('0.0', 'end')
        choice = list1.get()
        count = 0
        for i in range(len(info)):
            if choice in info[i][6]:
                count += 1
        text.insert('insert', '該公司文章數量:'+str(count)+"\n")
        text.insert('insert', '/' + '\n')
        for i in range(len(info)):
            if choice in info[i][6]:
                text.insert('insert', '文章編號:'+(info[i][0])+"\n")
                text.insert('insert', (info[i][2])+"\n")
                text.insert('insert', '-------------------------------------------------------------------------------' + '\n')

    def click2():
        text.delete('0.0', 'end')
        choice = Entry1.get()
        count = 0
        for i in range(len(info)):
            if choice in info[i][6]:
                count += 1
        text.insert('insert', '該公司文章數量:'+str(count)+"\n")
        text.insert('insert', '/' + '\n')
        for i in range(len(info)):
            if choice in info[i][6]:
                text.insert('insert', '文章編號:'+(info[i][0])+"\n")
                text.insert('insert', (info[i][2])+"\n")
                text.insert('insert', '-------------------------------------------------------------------------------' + '\n')

    # 下拉式選單
    label1 = tk.Label(first, text='請選擇你想查詢的公司', font=('Arial', 10), background="#EDCFA9", pady=5)
    label1.grid(row=0, column=0)
    company1 = []
    for i in range(len(company)):
        company1.append(company[i][1])
    list1 = ttk.Combobox(first, values = company1)
    list1.grid(row=1, column=0, padx=5)
    button = tk.Button(first, text='送出', command=click1)
    button.grid(row=2, column=0)
    # 輸tag的
    Label2 = tk.Label(first, text='公司名稱', font=('Arial', 10), background="#EDCFA9", pady=5)
    Label2.grid(row=3, column=0)
    Entry1 = tk.Entry(first, show=None)
    Entry1.grid(row=4, column=0, padx=5)
    button3 = tk.Button(first, text='送出', command=click2)
    button3.grid(row=5, column=0)

    text = tk.Text(first, height=30)
    text.grid(row=0, column=1, columnspan=16, rowspan=16, sticky=tk.W + tk.E + tk.N + tk.S, padx=5, pady=5)

button1 = tk.Button(mainpage, text='查詢文章', font=('Arial', 12), bg="#F2F0EC", fg="black", width=40, height=2, command=search_doc_title)
button1.grid(row=2, column=0, padx=5, pady=5)
button2 = tk.Button(mainpage, text='查詢tag', font=('Arial', 12), bg="#F2F0EC", fg="black", width=40, height=2, command=search_tag)
button2.grid(row=3, column=0, padx=5, pady=5)
button3 = tk.Button(mainpage, text='查詢公司', font=('Arial', 12), bg="#F2F0EC", fg="black", width=40, height=2, command=search_company)
button3.grid(row=4, column=0, padx=5, pady=5)
button4 = tk.Button(mainpage, text='離開', font=('Arial', 12), bg="#F2F0EC", fg="black", width=40, height=2, command=exit)
button4.grid(row=5, column=0, padx=5, pady=5)

mainpage.mainloop()
