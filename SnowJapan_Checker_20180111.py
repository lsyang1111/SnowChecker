import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import json
import time
import re   # import正規表示式

def main():
    url = "https://www.snowjapan.com/japan-ski-resorts/area/furano-hokkaido"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    img_ul = soup.find_all('td', {"class": "grid-snow-depth"})
    for ul in img_ul:
        snow = ul.get_text()
        snowCM = re.sub("\D", "", snow) # 用正規表示式, 把數字的部分留下來
        print(snowCM)    # 因為img_ul可能不只一行, 所以需要用for去做

if __name__ == "__main__":
    main()
    # 程式進入點