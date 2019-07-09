import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r'C:\\driver\\cr\\chromedriver.exe')
driver.get('https://www.flipkart.com/')
time.sleep(3)

driver.get('https://www.flipkart.com/search?q=apple&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')


data= driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[2]/div/div[1]/div[2]').get_attribute('innerHTML')
soup_level1=BeautifulSoup(data, 'html.parser')

search_result1 = soup_level2.findAll("div", {"class": "_1UoZlX"}, recursive=True)

for n in search_result1:
    product_name2 = n.find('div', {'class':'_3wU53n'})
    print product_name2.text
    print '------------'