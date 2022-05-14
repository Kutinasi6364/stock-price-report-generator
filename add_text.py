tex = input("テキストに追加する文字を入力してください:")

with open("newtext.txt", "r") as nt:
    nt.write(tex)
    print(nt.read())
