import urllib.robotparser
import requests
from bs4 import BeautifulSoup

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
    # response = requests.get(crawl_url)
    # 解析するURLと解析するパーサーを渡す
    # soup = BeautifulSoup(response.content, "html.parser")
    soup = BeautifulSoup(open("scraping-sample.html"), "html.parser")
    article_title = soup.find_all(
        "a", attrs={"class": "entry-card-wrap a-wrap border-element cf"}
    )

    for at in article_title:
        print(at.attrs["title"])
        print(at.attrs["href"])


if check_crawling():
    scraping()
else:
    print("このページはクローリング禁止です")
