import car_links as cl
import money_data as md
from datetime import datetime

def car_details(url):         #Returns first part of the details
    soup=cl.soup_return(url)
        
    details=soup.find_all('div',{'class':'product-properties-value'})
    details_list=[]
    for detail in details:
        details_list.append(detail.text)
    del details_list[12]
    
    if len(details_list)>13:
        if len(details_list)==15:
            details_list[13]=1
            details_list[14]=1
        elif len(details_list)==14 and details_list[13]=='Kreditdədir':
            details_list[13]=1
            details_list.append(0)
        else:
            details_list[13]=0
            details_list.append(1)
    else:
        details_list.extend([0,0])
    
    data_updated=soup.find_all('div',{'class':'product-statistics'})
    date=data_updated[0].findChildren('p')[1].text.lstrip('Yeniləndi: ').split()
    
    months={'Yanvar':1,'Fevral':2,'Mart':3,'Aprel':4,
            'May':5,'İyun':6,'İyul':7,'Avqust':8,
            'Sentyabr':9,'Oktyabr':10,'Noyabr':11,'Dekabr':12}
      
    date[1]=str(months[date[1]])
    details_list.extend([int(date[1]),int(date[2])])
    date= '-'.join(date)
    date = datetime.strptime(date, '%d-%m-%Y')
     
    details_list.append(date)
     
    return details_list,soup

   
def extra_details(details,soup):    #Returns rest of the details
    
    all_extras=['Yüngül lehimli disklər', 'ABS', 'Lyuk', 'Yağış sensoru',
                'Mərkəzi qapanma', 'Park radarı', 'Kondisioner', 
                'Oturacaqların isidilməsi', 'Dəri salon', 'Ksenon lampalar',
                'Arxa görüntü kamerası', 'Yan pərdələr', 'Oturacaqların ventilyasiyası']
    
    extras=soup.find_all('p',{'class':'product-extras-i'})
    extra_details=[extra.text for extra in extras]
    
    for option in all_extras:
        if option in extra_details:
            details.append(1)
        else:
            details.append(0)
    
    return details

def modify_str(s):   #Example 78 000 -> int 78.000
    s=s.split()[:-1]
    s=int(''.join(s))
    return s

def filtered_data(data):              #data=Car details
    data[3]=int(data[3])              #Buraxilis ili
    data[6]=float(data[6][:-2])       #Muherrikin Hecmi
    data[7]=int(data[7][:-5])         #Muherrikin Gucu
    data[9]=modify_str(data[9])    #Yurus
    
    #Price 
    usd, eur = md.currency(md.url)
    cur=data[12][-1]
    prc=modify_str(data[12])
    if cur=="$":
        prc*=usd
    elif cur=="€":
        prc*=eur
    data[12]=prc           
    return data










