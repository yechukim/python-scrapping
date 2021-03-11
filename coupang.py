import requests
from bs4 import BeautifulSoup

# page 1 - 5 
# 쿠팡 원피스 검색 
for page in range(1,2):
  url = "https://www.coupang.com/np/search?q=%EC%9B%90%ED%94%BC%EC%8A%A4&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(page)

  res = requests.get(url)
  res.raise_for_status()
  soup = BeautifulSoup(res.text,"lxml")

  items = soup.find_all("li",attrs={"class":"search-product"})
  for item in items:
    name = item.find("div", attrs={"class":"name"}).get_text()
    price = item.find("strong",attrs={"class":"price-value"}).get_text()
    
    delivery_free = item.find("div", attrs={"class":"badge badge-delivery"})
    if delivery_free:
      print("무료배송상품!")


