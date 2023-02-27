#Get Data Name, Price, Type of Products in config.py

from selenium import webdriver
import time
import bs4
import pandas as pd
import config

all_price_list = []
all_product_list = []
all_type_list = []

#Button of 2 type #Check Button Full Xpath From Dev tools 'Element'
button = ["/html/body/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div[4]/div/div[2]/div/div[1]/div/button[1]","/html/body/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div[4]/div/div[2]/div/div[1]/div/button[2]"]

#Loop to get All Product in Store
for link in config.CA:
    #Open link
    driver = webdriver.Chrome()
    driver.get(link)
    time.sleep(5)

    # Select language on pop-up #Check Button Full Xpath From Dev tools 'Element'
    thai_button = driver.find_element("xpath", '/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button')
    thai_button.click()
    time.sleep(3)

    # For check Product have more than 1 type
    datas = driver.page_source
    soup = bs4.BeautifulSoup(datas, 'html.parser')
    all_type_item = soup.find_all('div', {'class': 'flex items-center bR6mEk'}) #Check Class From Dev tools 'Element'

    if all_type_item:
        # Product have 2 type
        for i in button:
            select_item = driver.find_element('xpath', i) #Find Type Product From Button Type
            select_item.click()
            time.sleep(3)
            datas = driver.page_source
            soup = bs4.BeautifulSoup(datas, 'html.parser')

            product_name = soup.find_all('div', {'class': '_44qnta'}) #Check Class From Dev tools 'Element'
            for product in product_name:
                all_product_list.append(product.text)
            print('All Product :', all_product_list)

            price = soup.find_all('div', {'class': 'pqTWkA'}) #Check Class From Dev tools 'Element'
            for price in price:
                all_price_list.append(price.text)
            print(all_price_list)

            #Choice Type for select of product
            name_type = soup.find_all('button', {'class': 'product-variation product-variation--selected'}) #Get Name Type From Selected Type
            for name in name_type:
                all_type_list.append(name.text)
            print('All name type :', all_type_list)

            select_item.click()  # Unclick
            time.sleep(3)


    else: # No Type of Product
        product_name = soup.find_all('div', {'class': '_44qnta'}) #Check Class From Dev tools 'Element'
        for product in product_name:
            all_product_list.append(product.text)
        print('All Product :', all_product_list)

        price = soup.find_all('div', {'class': 'pqTWkA'}) #Check Class From Dev tools 'Element'
        for price in price:
            all_price_list.append(price.text)
        print(all_price_list)

        # Choice Type for select of product
        name_type = soup.find_all('button', {'class': 'product-variation'})
        for name in name_type:
            all_type_list.append(name.text)
        print('All name type :', all_type_list)

        time.sleep(3)

    time.sleep(3)
    driver.quit()

shopee_data = pd.DataFrame([all_product_list,all_type_list,all_price_list])
shopee_data = shopee_data.transpose()
shopee_data.columns = ['Title', 'Type','Price']

#Write Data To Excel in Sheet Name 'CA'
with pd.ExcelWriter(r'C:\Users\Bankdomo\OneDrive\Documents\Udomsub\Document\compare_price.xlsm',
                    mode='a') as writer:
    shopee_data.to_excel(writer, sheet_name='CA')