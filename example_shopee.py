from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import bs4
import pandas as pd

driver = webdriver.Chrome()
# url = "https://shopee.co.th/%E0%B8%A3%E0%B8%96%E0%B9%80%E0%B8%82%E0%B9%87%E0%B8%99%E0%B8%AA%E0%B8%B2%E0%B8%A1%E0%B8%A5%E0%B9%89%E0%B8%AD-%E0%B8%A3%E0%B8%96%E0%B9%80%E0%B8%82%E0%B9%87%E0%B8%99%E0%B8%99%E0%B9%89%E0%B8%B3-3-%E0%B8%A5%E0%B9%89%E0%B8%AD-%E0%B8%82%E0%B8%99%E0%B8%B2%E0%B8%94-10-%E0%B8%9B%E0%B8%B5%E0%B9%8A%E0%B8%9B-%E0%B8%A5%E0%B9%89%E0%B8%AD%E0%B9%84%E0%B8%99%E0%B8%A5%E0%B9%88%E0%B8%AD%E0%B8%99-%E0%B8%A5%E0%B9%89%E0%B8%AD%E0%B9%81%E0%B8%A1%E0%B9%87%E0%B8%81%E0%B8%8B%E0%B9%8C-%E0%B8%82%E0%B8%99%E0%B8%B2%E0%B8%94-60-x-120-%E0%B9%80%E0%B8%8B%E0%B8%99%E0%B8%95%E0%B8%B4%E0%B9%80%E0%B8%A1%E0%B8%95%E0%B8%A3--i.536315.10838056881?sp_atk=33bf6b66-4eec-4113-bc5b-fc2c0556fba3&xptdk=33bf6b66-4eec-4113-bc5b-fc2c0556fba3"
driver.get("http://shopee.co.th")

thai_button = driver.find_element("xpath", '/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button')
thai_button.click()

# Find elemect in shadow root in html
close_button = driver.execute_script('return document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector("div.shopee-popup__close-btn")')
close_button.click()

# Search in shopee website
search = driver.find_element("xpath", '/html/body/div[1]/div/header/div[2]/div/div[1]/div[1]/div/form/input')
search.send_keys('โต๊ะปรับระดับไฟฟ้า')
# Press enter
search.send_keys(Keys.ENTER)


# Set Zoom view website
driver.execute_script("document.body.style.zoom='10%'")
time.sleep(3)

# Get from HTML
datas = driver.page_source

# Tranfer data to beautifulsoup type
soup = bs4.BeautifulSoup(datas, 'html.parser')


#Get All Product name from website
all_product = soup.find_all('div', {'class': 'ie3A+n bM+7UW Cve6sh'})
all_product_list = []
for product in all_product:
    all_product_list.append(product.text)
print('All Product :', all_product_list)

#Get All Price  from website
all_price = soup.find_all('div', {'class': 'vioxXd rVLWG6'})
all_price_list = []
for price in all_price:
    all_price_list.append(price.text)
print(all_price_list)

#Get All Amount from website
all_sale = soup.find_all('div', {'class': 'r6HknA uEPGHT'})
all_sale_list = []
for sale in all_sale:
    all_sale_list.append(sale.text)
print(all_sale_list)

#Transfer data to table
shopee_data = pd.DataFrame([all_product_list,all_price_list,all_sale_list])
shopee_data = shopee_data.transpose()
shopee_data.columns = ['title', 'price', 'amount']

shopee_data.to_excel(r'C:\Users\Bankdomo\PycharmProjects\compare_price\shopee_table.xlsx')

time.sleep(3)
