import urllib.robotparser
import requests
from bs4 import BeautifulSoup
import csv

robot_url = "https://kutinasi-hobbyjoy.com/robots.txt"
crawl_url = "https://kutinasi-hobbyjoy.com/"

# クローリング可能かチェック
def check_crawling():
    ur = urllib.robotparser.RobotFileParser()
    ur.set_url(robot_url)
    ur.read()
    result = ur.can_fetch("*", crawl_url)
    return result


# URLから必要な情報の抽出
def scraping():
    # URLから情報を取得
    response = requests.get(crawl_url)
    # 解析するURLと解析するパーサーを渡す
    soup = BeautifulSoup(response.content, "html.parser")

    article_title = soup.find_all(
        "a", attrs={"class": "entry-card-wrap a-wrap border-element cf"}
    )
    return article_title

    # for at in article_title:
    #    print(at.attrs["title"])
    #    print(at.attrs["href"])


def create_csv(article_title):
    with open("title-url.csv", "w") as cf:
        cf = csv.writer(cf, delimiter=",")
        cf.writerow(["記事タイトル", "URL"])
        for at in article_title:
            cf.writerow([at.attrs["title"], at.attrs["href"]])


if check_crawling():
    article_title = scraping()
    create_csv(article_title)
else:
    print("このページはクローリング禁止です")
