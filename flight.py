from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

browser = webdriver.Chrome("/Users/yechubot/Downloads/chromedriver")

url = "https://flight.naver.com/flights/"
browser.get(url)

browser.find_element_by_link_text("미주").click()
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()

browser.find_element_by_link_text("가는날 선택").click()
browser.find_elements_by_link_text("17")[0].click()
browser.find_elements_by_link_text("18")[1].click()

browser.find_element_by_link_text("항공권 검색").click()