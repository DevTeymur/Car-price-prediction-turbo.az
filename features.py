import pandas as pd
from lightgbm import LGBMRegressor 
import os
from Machine_Learning.main import encoded_test_frame, test_predict, filter_car_details  

#df=pd.read_csv(r"C:\\Users\\User\\Desktop\\Turbo.az\\src\\Machine_Learning\\clean.csv")
#df=pd.read_csv(r"/home/tima/Desktop/Programming/Python/Turbo_az/Machine_Learning/clean.csv")
path = f'{os.path.abspath(os.path.join(os.path.dirname(__file__)))}/Machine_Learning/clean.csv'
df=pd.read_csv(path)

def get_model_brand():
    """Returns every brands' models in dictonary."""
    brands=list(df['Brand'].value_counts().index)
    brand_model_dict={}
    for brand in brands:
        brand_model_dict[brand]=list(df[df["Brand"]==brand]['Model'].value_counts().index)
    return brand_model_dict

def return_feature_list(col_name):
    """Returns data in columns."""
    list_=list(df[col_name].value_counts().sort_index(ascending=True).index)
    return list_

def get_price(form_list):
    """Returns predicted price in rounded in range."""
    print('Form list get price', form_list)
    filtered=filter_car_details(df, form_list)
    test, X, Y = encoded_test_frame(df, filtered)
    price = test_predict(LGBMRegressor, {'learning_rate': 0.3, 'max_depth': -3, 'n_estimators': 104}, test, X, Y)
    return round(int(price)-500, -3), round(int(price)+500, -3)

def brand_json_format_list(col_name):
    """Returns brands list in json format for dependent dropdowns."""
    json_list=[{'name': ' '}]
    for brand in df['Brand'].value_counts().sort_index(ascending=True).index:
        d={}
        d['name']=brand
        json_list.append(d)
    return json_list

def model_json_format_list(brand_name):
    """Returns models list in json format for dependent dropdowns."""
    json_list=[{'name': ' '}]
    for brand in df[df['Brand']==brand_name]['Model'].value_counts().sort_index(ascending=True).index:
        d={}
        d['name']=brand
        json_list.append(d)
    return json_list
