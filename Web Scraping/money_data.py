import requests
from bs4 import BeautifulSoup
from datetime import date

today = date.today()

#Creating link for special day
url='https://kapitalbank.az/en/currency-rates/{}'.format(today.strftime("%d-%m-%Y"))  

def currency(url):             #Returns todays currency for dollar and euro
    response=requests.get(url)
    html_inside=response.content
    soup=BeautifulSoup(html_inside, 'html.parser')
    values=soup.find_all('div',{'class':'d-flex text-nowrap'})
    USD=float(values[1].text.strip())
    EUR=float(values[10].text.strip())
    return USD, EUR


