#Get Data Name, Price, Type of a Product From Shopee Website

from selenium import webdriver
import time
import bs4
import pandas as pd
import config

all_price_list = []
all_product_list = []
all_type_list = []

myURL = "https://shopee.co.th/%E0%B8%A3%E0%B8%96%E0%B9%80%E0%B8%82%E0%B9%87%E0%B8%99%E0%B8%AA%E0%B8%B2%E0%B8%A1%E0%B8%A5%E0%B9%89%E0%B8%AD-%E0%B8%A3%E0%B8%96%E0%B9%80%E0%B8%82%E0%B9%87%E0%B8%99%E0%B8%99%E0%B9%89%E0%B8%B3-3-%E0%B8%A5%E0%B9%89%E0%B8%AD-%E0%B8%82%E0%B8%99%E0%B8%B2%E0%B8%94-10-%E0%B8%9B%E0%B8%B5%E0%B9%8A%E0%B8%9B-%E0%B8%A5%E0%B9%89%E0%B8%AD%E0%B9%84%E0%B8%99%E0%B8%A5%E0%B9%88%E0%B8%AD%E0%B8%99-%E0%B8%A5%E0%B9%89%E0%B8%AD%E0%B9%81%E0%B8%A1%E0%B9%87%E0%B8%81%E0%B8%8B%E0%B9%8C-%E0%B8%82%E0%B8%99%E0%B8%B2%E0%B8%94-60-x-120-%E0%B9%80%E0%B8%8B%E0%B8%99%E0%B8%95%E0%B8%B4%E0%B9%80%E0%B8%A1%E0%B8%95%E0%B8%A3--i.536315.10838056881?sp_atk=33bf6b66-4eec-4113-bc5b-fc2c0556fba3&xptdk=33bf6b66-4eec-4113-bc5b-fc2c0556fba3"

#Button For Select Type Product
button = ["/html/body/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div[4]/div/div[2]/div/div[1]/div/button[1]","/html/body/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div[4]/div/div[2]/div/div[1]/div/button[2]"]

driver = webdriver.Chrome()
driver.get(myURL)
time.sleep(5)

# Select language on pop-up
thai_button = driver.find_element("xpath", '/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button')
thai_button.click()
time.sleep(3)

datas = driver.page_source
soup = bs4.BeautifulSoup(datas, 'html.parser')
all_type_item = soup.find_all('div', {'class': 'flex items-center HiGScj'}) #Check Class Full Xpath From Dev tools 'Element'

name_type_list = []
name_type = soup.find_all('button', {'class': 'product-variation product-variation--selected'})

for name in name_type:
    name_type_list.append(name.text)
    print('All name type :', name_type_list)
    time.sleep(5)
#print('All name type :', name_type_list)

if all_type_item:
    #Product have 2 type
    for i in button:
        select_item = driver.find_element('xpath',i)
        select_item.click()
        datas = driver.page_source
        soup = bs4.BeautifulSoup(datas, 'html.parser')

        price = soup.find_all('div', {'class': 'X0xUb5'}) #Check Class Full Xpath From Dev tools 'Element'
        for price in price:
            all_price_list.append(price.text)
        print(all_price_list)

        product_name = soup.find_all('div', {'class': 'YPqix5'}) #Check Class Full Xpath From Dev tools 'Element'
        for product in product_name:
            all_product_list.append(product.text)
        print('All Product :', all_product_list)

        select_item.click() #Unclick
#No Type of Product
else:
    product_name = soup.find_all('div', {'class': 'YPqix5'}) #Check Class Full Xpath From Dev tools 'Element'
    for product in product_name:
        all_product_list.append(product.text)
    print('All Product :', all_product_list)

    price = soup.find_all('div', {'class': 'X0xUb5'}) #Check Class Full Xpath From Dev tools 'Element'
    for price in price:
        all_price_list.append(price.text)
    print(all_price_list)
print(price)

