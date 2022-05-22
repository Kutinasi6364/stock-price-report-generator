import csv
import time

from bs4 import BeautifulSoup
import requests
import urllib.robotparser


# 各URLの設定
robot_url = "https://minkabu.jp/robots.txt"
basic_url = "https://minkabu.jp/stock/"

# 証券番号のリストを作成
code_list = [
    "8316",
    "9436",
    "8424",
    "8306",
    "4502",
    "9986",
    "8096",
    "7995",
    "4327",
    "8898",
    "7751",
    "8591",
    "8053",
    "8425",
    "8566",
    "9433",
]

item = []

# クローリング可能かチェック
def check_crawling(url):
    ur = urllib.robotparser.RobotFileParser()
    ur.set_url(robot_url)
    ur.read()
    result = ur.can_fetch("*", url)
    return result


# スクレイピングの実行
def scraping(url, b):
    # 証券番号を最初に追加する
    item_list = [b]

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # 配当金抽出
    item_value = soup.find_all(
        "dd", attrs={"class": "ly_vamd_inner ly_colsize_9_fix fwb tar wsnw"}
    )
    # 株価抽出
    item_price = soup.find("div", attrs={"class": "stock_price"}).text

    # 抽出した文字の整形
    item_price = item_price.replace(",", "")
    item_price = item_price.replace("\n", "")
    item_price = item_price.replace(" ", "")
    item_price = item_price.replace("円", "")

    # 株価と配当金をリストに追加
    item_list.append(float(item_price))
    item_list.append(item_value[3].string.replace("%", ""))
    return item_list


# CSVファイルに書き込み
def create_csv(item):
    # 項目名の設定
    # list = ["証券コード", "株価", "配当利回り"]
    with open("investment.csv", "w") as cf:
        cf = csv.writer(cf, delimiter=",")
        # cf.writerow(list)
        for w in item:
            cf.writerow(w)


# 全ての証券番号の情報を抜き出す
for b in code_list:
    # 指定した証券番号のURLを作成
    url = basic_url + b
    if check_crawling(url):
        # 証券番号、株価、配当金をリストに追加
        item.append(scraping(url, b))
        print(b + "抽出完了")
        time.sleep(2)
    else:
        print("このページはクローリング禁止です")
# CSVファイルの作成
create_csv(item)
print("出力完了")
