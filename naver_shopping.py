import requests
from bs4 import BeautifulSoup

url = "https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EC%9B%90%ED%94%BC%EC%8A%A4&pagingIndex=2&pagingSize=40&productSet=total&query=%EC%9B%90%ED%94%BC%EC%8A%A4&sort=rel&timestamp=&viewType=list"

headers ={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}

res = requests.get(url,headers= headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
items = soup.find_all("li", attrs={"class": "basicList_item__2XT81"})

for item in items:
  name = item.find("a",attrs={"class":"basicList_link__1MaTN"}).get_text()
  ad = item.find("button", attrs={"class":"ad_ad_stk__12U34"})
  # 광고 상품 제외 
  if ad:
    ad = ad.get_text()
    print("--광고 상품 제외--")
    continue
  price = item.find("span", attrs={"class":"price_num__2WUXn"}).get_text()
  review = item.find("em",attrs={"em":"basicList_num__1yXM9"})
  if review:
    review = review.get_text()
  else:
    review = "0"

  #thumb = item.a['href']
  print("상품명",name)
  print("가격",price)
  print("리뷰 수: ",review)