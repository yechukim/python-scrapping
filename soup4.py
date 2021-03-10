import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

# 가져온 html 문서를 lxml (parser)를 통해서 soup 객체로 만듦
soup = BeautifulSoup(res.text, "lxml")
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1)