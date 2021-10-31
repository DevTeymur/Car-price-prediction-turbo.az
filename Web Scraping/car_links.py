import requests
from bs4 import BeautifulSoup

main_page='https://turbo.az'

def soup_return(url):
    response=requests.get(url)
    html_inside=response.content 
    soup=BeautifulSoup(html_inside, 'html.parser')
    return soup

def car_links(soup):    #returns car links in one page
    pr=soup.find_all('a',{'class':'products-i-link'})
    l=[]
    for i in pr:
        if '/autos/' in i['href']:
            l.append(main_page+(i['href']))
    return l

def next_page(url,page_n=None):  #returns page's soup and next page's url
    soup=soup_return(url)
    next_page_script=soup.find_all('a',{'rel':'next'})
    if len(next_page_script)==0:
        return None
        
    if page_n!=None:
        if "/autos?page={}".format(page_n) not in next_page_script[0]['href']:
            next_page_url=main_page+next_page_script[0]['href']
            return soup_return(next_page_url),next_page_url
        else:
            return None
    else:
        try:                  #for all pages long run time
            next_page_url=main_page+next_page_script[0]['href']
            return soup_return(next_page_url),next_page_url
        except:
            return None

def all_page_cars(url,page_n=None):  #returns cars in all pages
    all_cars_links=[] 
    soup=soup_return(url)
    while True:
        all_cars_links+=car_links(soup)
        if next_page(url,page_n)!=None:
            soup,url=next_page(url,page_n)
        else:
            break
    return list(set(all_cars_links))


######## NOT IN USE ########
def all_car_models(url):    #returns link of different car models
    soup=soup_return(url)
    car_names=soup.find_all('a',{'class':'makes--name'})
    # print(car_names)
    cars=[]
    for car in car_names:
        cars.append(main_page+car['href'])
    return cars




    
    