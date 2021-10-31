import car_details as cd
import car_links as cl
import pandas as pd
import time

t1=time.time()

f=open('all_car_model_links.txt','r')
model_links=[i.rstrip('\n') for i in f.readlines()]
list_of_car_links=[]   #list of car links

print("*******************************************************************")
print("*******************************************************************")
print("*******************************************************************")

for link in model_links[0:34]:
    list_of_car_links+=cl.all_page_cars(link)

print("******************************************")
print("First Porsion Done, Waiting the Second... ")
print("******************************************")

for link in model_links[34:68]:
    list_of_car_links+=cl.all_page_cars(link)
    
print("******************************************")
print("Second Porsion Done, Waiting the Third... ")
print("******************************************")

for link in model_links[68:102]:
    list_of_car_links+=cl.all_page_cars(link)

print("******************************************")
print("Third Porsion Done, Waiting the Fourth... ")
print("******************************************")

for link in model_links[102:136]:
    list_of_car_links+=cl.all_page_cars(link)

print("**********************************************")
print("All Porsions Done, Waiting for Details part... ")
print("**********************************************")

print("*******************************************************************")
print("*******************************************************************")
print("*******************************************************************")

dic={}   
all_car_details=[]
len(list_of_car_links)-len(all_car_details)

t3=time.time()
t_1000=time.time()
t_5000=time.time()
t_10000=time.time()
for i in list_of_car_links[11001:]:   #Change
    try:
        det,soup=cd.car_details(i)
        result=cd.filtered_data(cd.extra_details(det,soup))
        print("*",end=" ")
        index_i=list_of_car_links.index(i)
        if index_i%500==0:
            print(result)
        if index_i%1000==0:
            print("\n##########################################")
            print("time for {}:{} (in minutes) :: {}".format(index_i-1000,index_i,(time.time()-t_1000)/60))
            t_1000=time.time()
        if index_i%5000==0:
            print("\n##########################################")
            print("time for {}:{} (in minutes) :: {}".format(index_i-5000,index_i,(time.time()-t_5000)/60))
            t_5000=time.time()
        if index_i%10000==0:
            print("\n##########################################")
            print("time for {}:{} (in minutes) :: {}".format(index_i-10000,index_i,(time.time()-t_10000)/60))
            t_10000=time.time()
        dic[i]=result
        all_car_details.append(result)
    except:
        pass


t2=time.time()
print((t2-t1)/3600)
print((t2-t3)/60)
print(len(all_car_details))

columns=["City", "Brand", "Model", "ProdYear", "BanType", "Color", "EngVol", "EngPow", "FuelType",
         "RideDist", "Gearbox", "Transmission", "Price", "Credit", "Barter", "AnnMonth", "AnnYear",
         "AnnDateTime", "YungulLehimliDiskler", "ABS", "Lyuk", "RainSensor", "MerkeziQapanma",
         "ParKRadar", "Condisioner", "SeatHeat", "LeatherSalon", "KsenonLamps",
         "BackVisionCam", "YanPerdeler", "SeatVentilation"]

#Writing to DataFrame
df=pd.DataFrame(all_car_details,columns=columns)

df.to_csv("cars_turbo_az.csv")
# df.to_csv("src\cars_turbo_az.csv") 






