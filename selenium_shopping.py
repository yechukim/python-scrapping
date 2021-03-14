from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

browser = webdriver.Chrome("/Users/yechubot/Downloads/chromedriver")
browser.maximize_window()

url = "https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EC%9B%90%ED%94%BC%EC%8A%A4&pagingIndex=2&pagingSize=40&productSet=total&query=%EC%9B%90%ED%94%BC%EC%8A%A4&sort=rel&timestamp=&viewType=list%22"
browser.get(url)

interval = 2
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(interval)

    cur_height = browser.execute_script("return document.body.scrollHeight")

    if cur_height == prev_height:
        break

    prev_height = cur_height

    soup = BeautifulSoup(browser.page_source, "lxml")

    items = soup.find_all("li", attrs={"class": "basicList_item__2XT81"})
    # print(len(items))

    for item in items:
        title = item.find("a", attrs={"class": "basicList_link__1MaTN"})[
            'title']
        price = item.find(
            "span", attrs={"class": "price_num__2WUXn"}).get_text()
        ads = item.find("button", attrs={"class": "ad_ad_stk__12U34"})
        if ads:
            ads = ads.get_text()
            print("***광고 제품입니다***")
        link = item.find(
            "a", attrs={"class": "thumbnail_thumb__3Agq6"})['href']
        print(f'제품명 : {title}')
        print(f'가격 : {price}')
        print(f'링크:{link}')
        print("-"*10)

    browser.quit()

