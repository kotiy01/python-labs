import tkinter as tk
# coding=utf-8
fo = open("config.txt",
          mode = "rt")

global DATA

DATA = ""

TEXTAREA_1 = ""
TEXTAREA_2 = ""
TEXTAREA_3 = ""
TEXTAREA_4 = ""

for line in fo:
    if line == "\n":
        continue
    DATA = DATA + line

def get_info_func():
    info = tk.Tk()

    info.geometry("300x100")
    info.title("Вывод информации")
    info.resizable(width=False,
                   height=False)

    DATA_INFO = ""

    for i in range(amountLine()):
        if e2.get() in DATA.split("\n")[i].split(".")[1]:
            DATA_INFO = DATA.split("\n")[i].split(".")[1]
            break

    i_label_1 = tk.Label(info,
                         text = "Наименование товара: " + DATA_INFO.split(",")[0])
    i_label_2 = tk.Label(info,
                         text = "Производитель товара: " + DATA_INFO.split(",")[1])
    i_label_3 = tk.Label(info,
                         text = "Цена товара: " + DATA_INFO.split(",")[2])
    i_label_4 = tk.Label(info,
                         text = "Вес/ количество товара: " + DATA_INFO.split(",")[3])

    i_label_1.pack()
    i_label_2.pack()
    i_label_3.pack()
    i_label_4.pack()

    info.mainloop()
def amountLine():
    AMOUNT_LINES = 0
    with open("config.txt", "r") as file:
        for linears in file:
            AMOUNT_LINES
            AMOUNT_LINES += 1
    return AMOUNT_LINES

def delete_memory_func():
    DATA = ""
    with open("config.txt", "r") as file:
        for line in file:
            if line == "\n":
                continue
            DATA = DATA + line

    DATA_RESP = ""
    DATA_SPLIT = DATA.split("\n")
    DATA = ""

    a = ""

    for i in range(amountLine()):
        if DATA_SPLIT[i] != DATA_SPLIT[int(d_e_1.get()) - 1]:
            DATA = DATA + DATA_SPLIT[i] + "\n"
    print(DATA)

    for i in range(amountLine() - 1):
        a = a + (str(i + 1) + ". " + DATA.split("\n")[i].split(".")[1]) + "\n"
    with open("config.txt", "w") as file:
        file.write(a)
    print(a)
def delete_memory():
    delete = tk.Tk()

    delete.geometry("300x300")
    delete.title("Удаление данных")
    delete.resizable(width=False,
                   height=False)

    global d_e_1

    d_label_1 = tk.Label(delete,
                         text = "Укажите номер элемента, который необходимо удалить")
    d_e_1 = tk.Entry(delete,
                     width = 20)
    d_btn_1 = tk.Button(delete,
                        text = "Удалить",
                        command = delete_memory_func)
    d_label_1.pack()
    d_e_1.pack()
    d_btn_1.pack()

    delete.mainloop()
def add_memory_func():
    DATA = ""
    with open("config.txt", "r") as file:
        for line in file:
            if line == "\n":
                continue
            DATA = DATA + line

    AMOUNT_LINES = 0

    with open("config.txt", "r") as file:
        for linears in file:
            AMOUNT_LINES
            AMOUNT_LINES += 1

    with open("config.txt", "w") as file:
        file.write(DATA + "\n" + str(AMOUNT_LINES + 1) + ". " + a_e_1.get() + ", " + a_e_2.get() + ", " + a_e_3.get() + ", " + a_e_4.get())

def add_memory():

    global a_e_1
    global a_e_2
    global a_e_3
    global a_e_4

    add = tk.Tk()

    add.geometry("300x300")
    add.title("Добавление данных")
    add.resizable(width=False,
                   height=False)

    a_label_1 = tk.Label(add,
                         text = "Название товара")
    a_label_2 = tk.Label(add,
                         text = "Название продавца")
    a_label_3 = tk.Label(add,
                         text = "Стоимость")
    a_label_4 = tk.Label(add,
                         text = "Вес/ количество")

    a_e_1 = tk.Entry(add,
                     width = "20")
    a_e_2 = tk.Entry(add,
                     width = "20")
    a_e_3 = tk.Entry(add,
                     width = "20")
    a_e_4 = tk.Entry(add,
                     width = "20")

    a_btn1 = tk.Button(add,
                       text = "Добавить",
                       command = add_memory_func)

    a_label_1.pack()
    a_e_1.pack()
    a_label_2.pack()
    a_e_2.pack()
    a_label_3.pack()
    a_e_3.pack()
    a_label_4.pack()
    a_e_4.pack()
    a_btn1.pack()

    add.mainloop()

def edit_text():
    EDIT_AREA = DATA.split("\n")[int(e1.get()) - 1].split(".")[1].split(",")

    '''print(EDIT_AREA[0]) # Имя товара
    print(EDIT_AREA[1]) # Магазин
    print(EDIT_AREA[2]) # Цена
    print(EDIT_AREA[3]) # Вес'''

    NAME_TH = e_e_1.get()
    SHOP_TH = e_e_2.get()
    COST_TH = e_e_3.get()
    WEIGHT_TH = e_e_4.get()

    EDIT_TEXT = DATA.split("\n")[int(e1.get()) - 1]\
        .replace(EDIT_AREA[0], " " + NAME_TH)\
        .replace(EDIT_AREA[1], " " + SHOP_TH)\
        .replace(EDIT_AREA[2], " " + COST_TH)\
        .replace(EDIT_AREA[3], " " + WEIGHT_TH)

    e_label_1["text"] = EDIT_TEXT

    with open("config.txt", "w") as file:
        file.write(DATA.replace(DATA.split("\n")[int(e1.get()) - 1], EDIT_TEXT))

def sort_alphabet():
    mas = []
    for i in range(amountLine()):
        mas.append(DATA.split("\n")[i].split(".")[1].split(",")[0].replace(" ", ""))
    SORTED_MAS = sorted(mas)

    SPLITED_DATA = DATA.split("\n")

    REPLACED = ""

    for i in range(amountLine()):
        for j in range(amountLine()):
            if SORTED_MAS[i] in SPLITED_DATA[j]:
                '''DATA.split("\n")[i].split(".")[1].split(",")[0] = DATA.split("\n")[j].split(".")[1].split(",")[0]
                DATA.split("\n")[i].split(".")[1].split(",")[1] = DATA.split("\n")[j].split(".")[1].split(",")[1]
                DATA.split("\n")[i].split(".")[1].split(",")[2] = DATA.split("\n")[j].split(".")[1].split(",")[2]
                DATA.split("\n")[i].split(".")[1].split(",")[3] = DATA.split("\n")[j].split(".")[1].split(",")[3]'''

                EDIT_TEXT1 = DATA.split("\n")[i] \
                    .replace(DATA.split("\n")[i].split(".")[1].split(",")[0], DATA.split("\n")[j].split(".")[1].split(",")[0]) \
                    .replace(DATA.split("\n")[i].split(".")[1].split(",")[1], DATA.split("\n")[j].split(".")[1].split(",")[1]) \
                    .replace(DATA.split("\n")[i].split(".")[1].split(",")[2], DATA.split("\n")[j].split(".")[1].split(",")[2]) \
                    .replace(DATA.split("\n")[i].split(".")[1].split(",")[3], DATA.split("\n")[j].split(".")[1].split(",")[3])

                '''DATA.split("\n")[j].split(".")[1].split(",")[0] = PREVIOUS_DATA.split(".")[1].split(",")[0]
                DATA.split("\n")[j].split(".")[1].split(",")[1] = PREVIOUS_DATA.split(".")[1].split(",")[1]
                DATA.split("\n")[j].split(".")[1].split(",")[2] = PREVIOUS_DATA.split(".")[1].split(",")[2]
                DATA.split("\n")[j].split(".")[1].split(",")[3] = PREVIOUS_DATA.split(".")[1].split(",")[3]'''
                REPLACED = REPLACED + EDIT_TEXT1 + "\n"
    with open("config.txt", "w") as file:
        file.write(REPLACED)

def find_open_window():
    if e1.get() in DATA:

        global e_e_1
        global e_e_2
        global e_e_3
        global e_e_4

        global e_label_1

        edit = tk.Tk()

        num = int(e1.get())

        edit.geometry("300x300")
        edit.title("Редактирование данных")
        edit.resizable(width=False,
                       height=False)
        e_label_1 = tk.Label(edit,
                             text = DATA.split("\n")
                             [num - 1])
        e_label_2 = tk.Label(edit,
                             text = "Изменение названия товара")
        e_e_1 = tk.Entry(edit,
                         width = "20")
        e_label_3 = tk.Label(edit,
                             text = "Изменение продавца товара")
        e_e_2 = tk.Entry(edit,
                         width = "20")
        e_label_4 = tk.Label(edit,
                             text = "Изменение цены товара")
        e_e_3 = tk.Entry(edit,
                         width = "20")
        e_label_5 = tk.Label(edit,
                             text = "Изменение количества товара")
        e_e_4 = tk.Entry(edit,
                         width = "20")
        e_btn_1 = tk.Button(edit,
                     text = "Применить изменения",
                     command = edit_text)

        e_label_1.pack()

        e_label_2.pack()
        e_e_1.pack()
        e_label_3.pack()
        e_e_2.pack()
        e_label_4.pack()
        e_e_3.pack()
        e_label_5.pack()
        e_e_4.pack()
        e_btn_1.pack()

        edit.mainloop()
    else:
        print("error")

root = tk.Tk()

root.geometry("300x330")
root.title("Главное окно")
root.resizable(width=False,
               height=False)

top_frame = tk.Frame()
top_frame.pack()

foot_frame = tk.Frame()
foot_frame.pack(side = "bottom")

label_1 = tk.Label(root,
                   text = DATA,
                   fg = "blue")
e1 = tk.Entry(root,
             width = "20")
button_1 = tk.Button(root,
                     text = "Найти ячейку памяти",
                     command = find_open_window)
button_2 = tk.Button(root,
                     text = "Добавление ячейки памяти",
                     command = add_memory)
button_3 = tk.Button(root,
                     text = "Удаление ячейки памяти",
                     command = delete_memory)

label_2 = tk.Label(root,
                   text = "Введите название товара")
e2 = tk.Entry(root, width = 20)
button_4 = tk.Button(root,
                     text = "Получить информацию",
                     command = get_info_func)
button_5 = tk.Button(root,
                     text = "Сортировка по алфавиту",
                     command = sort_alphabet)
label_1.pack()
e1.pack()
button_1.pack()
button_2.pack()
button_3.pack()
label_2.pack()
e2.pack()
button_4.pack()
button_5.pack()

root.mainloop()
