import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas


chrome_driver_path = "/Users/macbook/chrome driver /chromedriver_mac64/chromedriver"

driver_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_service)
driver.get("https://ngxgroup.com/exchange/data/equities-price-list/")

time.sleep(5)
show_all = driver.find_element(By.CSS_SELECTOR,'.selection span')
time.sleep(5)
show_all.click()
time.sleep(2)

show_all2 = driver.find_elements(By.CSS_SELECTOR, 'label select option')
show_all2[20].click()



table_heads = driver.find_elements(By.CSS_SELECTOR, "thead tr th")
heads = [head.text for head in table_heads]
heads[1]=heads[1].replace("\n"," ")
data_dict = {}
table_body = driver.find_elements(By.CSS_SELECTOR, "tbody tr")

for i in table_body:
    i_data=i.find_elements(By.CSS_SELECTOR, "td")
    i_data_list=[data.text for data in i_data]
    data_dict[f"{table_body.index(i)}"]=i_data_list


data = pandas.DataFrame.from_dict(data_dict, orient='index',
                       columns=heads)
with open('stock price for today.csv', 'w') as file:
    file.write(data.to_csv())
print(data)

