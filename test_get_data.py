#Test Get data from website
#Use Full Xpath for reference location to click and get data by class
#Find class name from Dev tools windows in Google Chrome

from selenium import webdriver
import time
import bs4

#Open Url with Google chrome browser
driver = webdriver.Chrome()
url = "https://shopee.co.th/%E0%B8%A3%E0%B8%96%E0%B9%80%E0%B8%82%E0%B9%87%E0%B8%99%E0%B8%99%E0%B9%89%E0%B8%B3-3-%E0%B8%A5%E0%B9%89%E0%B8%AD-%E0%B8%A3%E0%B8%96%E0%B9%80%E0%B8%82%E0%B9%87%E0%B8%99-3-%E0%B8%A5%E0%B9%89%E0%B8%AD-6-%E0%B8%9B%E0%B8%B5%E0%B9%8A%E0%B8%9A-%E0%B8%82%E0%B8%99%E0%B8%B2%E0%B8%94-50-x-80-%E0%B8%8B%E0%B8%A1.-%E0%B8%A5%E0%B9%89%E0%B8%AD-PVC-(%E0%B8%A5%E0%B9%89%E0%B8%AD%E0%B8%94%E0%B8%B3%E0%B8%A2%E0%B8%B2%E0%B8%87%E0%B8%95%E0%B8%B1%E0%B8%99)-%E0%B8%A3%E0%B8%AB%E0%B8%B1%E0%B8%AA-300-i.123904486.7397001367?sp_atk=4f760262-e2f8-4340-b013-33fff8910042&xptdk=4f760262-e2f8-4340-b013-33fff8910042"
driver.get(url)

# Select language on pop-up #Check Button Full Xpath From Dev tools 'Element'
thai_button = driver.find_element("xpath", '/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button')
thai_button.click()

time.sleep(3) #Wait time depend on loading time website

#Select type product if have more than 1 type #Check Class From Dev tools 'Element'
select_item = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div[4]/div/div[2]/div/div[1]/div/button[1]')
select_item.click()

data = driver.page_source
soup = bs4.BeautifulSoup(data, 'html.parser')

price = soup.find_all('div', {'class': 'X0xUb5'}) #Check Class From Dev tools 'Element'
all_price_list = []
for price in price:
    all_price_list.append(price.text)
print(all_price_list)

product_name = soup.find_all('div', {'class': 'YPqix5'}) #Check Class From Dev tools 'Element'
all_product_list = []
for product in product_name:
    all_product_list.append(product.text)
print('All Product :', all_product_list)

time.sleep(5)
