import pandas as pd
import joblib as j
from warnings import filterwarnings
filterwarnings('ignore')


def filter_car_details(df, input_list):
    """Filters car details that came from POST method."""
    column_list = list(df.columns)
    column_list.remove('Price')
    entry_names = [item[0] for item in input_list]
    false_options = list(set(column_list)-set(entry_names))
    filtered_list = input_list
    for op in false_options:
        filtered_list.append((op, '0'))
    l = []
    for i in filtered_list:
        try:
            if i[0]!="Model":
                l.append([i[0], float(i[1])])
            else:
                l.append([i[0], i[1]])
        except:
            l.append([i[0], i[1]])
    filtered_list = l.copy()
    return filtered_list


def encoded_test_frame(df1, filtered_list):
    """Encodes data along with main data. Returns encoded input dataframe, data and target dataframe."""
    df = df1.copy()
    columns = [col for col in df.columns]
    columns.remove('Price')
    ordered_option_list = []
    for col, opt in zip(columns, filtered_list):
        if col == opt[0]:
            ordered_option_list.append(opt[1])
        else:
            for i in filtered_list:
                if i[0] == col:
                    ordered_option_list.append(i[1])
    test = pd.DataFrame(columns=columns)
    test.loc[len(test)] = ordered_option_list
    data = df.copy()
    merged = pd.concat([data, test], keys=['data', 'test'], axis=0)
    merged = pd.get_dummies(merged, drop_first=True)
    test = merged.loc['test']
    encoded_data = merged.loc['data']
    X = encoded_data.drop('Price', axis=1)
    Y = encoded_data[['Price']]
    return test, X, Y

#Catboost - {'eta': 0.2, 'gamma': 0, 'max_depth': 6}
#LGBM - {'learning_rate': 0.3, 'max_depth': -3, 'n_estimators': 104}


def test_predict(algo, params, test_frame, X, Y):
    """Fits and predicts model and returns predicted price for test frame."""
    #model = algo(**params)
    #model.fit(X, Y)
    #j.dump(model, 'model.pkl')
    #predicted_price = model.predict(test_frame.drop('Price', axis=1))
    model = j.load('model.pkl')
    predicted_price = model.predict(test_frame.drop('Price', axis=1))
    print(f'Model: {type(model).__name__}')
    print(f'Price: {predicted_price[0]}')
    return predicted_price[0]
