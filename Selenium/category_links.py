import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

start=time.time()
url='https://turbo.az'

def select_func():
    """Collects link of car categoires."""      
    response=requests.get(url)    
    html_ici=response.content    
    soup=BeautifulSoup(html_ici,'html.parser')    
    select=soup.find('select',{'class':'select optional', 'name':'q[make][]'})
    return select

value_numbers=[]

options=select_func().find_all("option")
for i in range(1,len(options)):
    value_numbers.append(options[i]['value'])
     
path="Selenium\ChromeWebDriver\chromedriver.exe"  
driver=webdriver.Chrome(path)
driver.get(url) 

links_of_car_categories=[]

for value in value_numbers:
    select = Select(driver.find_element_by_id('q_make'))
    select.select_by_value(value)
    driver.find_element_by_xpath('//button[normalize-space()="Axtar"]').click()
    links_of_car_categories.append(driver.current_url)

driver.quit()

#Writing links to txt file
f=open('Selenium\all_car_model_links.txt','w')
 
for link in links_of_car_categories:
    f.write(link+'\n')
f.close()

stop=time.time()
print("Time: ", stop-start)