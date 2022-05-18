import requests
from bs4 import BeautifulSoup

url = "https://kutinasi-hobbyjoy.com/"

htm = requests.get(url)

bs = BeautifulSoup(htm.content, "html.parser")
print(bs)
