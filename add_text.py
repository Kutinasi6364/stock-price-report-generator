import os
from tkinter import filedialog


def input_check():
    f_check = input("テキストファイルの参照:r  新規作成:c を入力してください")
    if f_check == "r":
        mode = "a"
        f_typ = [("テキストファイル", "*.txt")]
        r_dir = "/home/kutinasi6364_0126/Python"
        f_data = filedialog.askopenfilename(filetypes=f_typ, initialdir=r_dir)
        return f_data, mode
    elif f_check == "c":
        mode = "w"
        f_data = input("新規作成するファイル名を入力してください:")
        if os.path.exists("./" + str(f_data)):
            print("同名のファイルが存在します。")
            return input_check()
        return f_data, mode
    else:
        print("入力した値が無効です")
        return input_check()


def file_make(f_data, txt, mode):
    with open(f_data, mode) as wt:
        wt.write(txt)


def file_opn(f_data):
    with open(f_data, "r") as rt:
        print(rt.read())


(f_data, mode) = input_check()
txt = input("テキストに追加する文字を入力してください:")
file_make(f_data, txt, mode)
file_opn(f_data)
