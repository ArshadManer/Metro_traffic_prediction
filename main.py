import pandas as pd
import random
import pickle
import sys
import os
import socket
import warnings
warnings.filterwarnings('ignore')

class AuthorizedModel:
    def __init__(self, model):
        self.model = model
        self.authorized_ips = ['172.16.251.35','172.16.20.196']

    def predict(self, x):
        ip_address = socket.gethostbyname(socket.gethostname())
        if ip_address in self.authorized_ips:
            return self.model.predict(x)
        else:
            raise Exception("Unauthorized user")

base_path = os.getcwd()

with open(os.path.join(base_path,'Metro_traffic_prediction/saved_models/model_en.pickle'), 'rb') as f:
    model = pickle.load(f)

with open(os.path.join(base_path,'Metro_traffic_prediction/saved_models/encoder.pickle'), 'rb') as f:
    encoder = pickle.load(f)
        
weather_main = ['Clear','Cloudy','Rainy']
holiday = [0, 1]
temp = [0, 40]
rain = [0, 50]
snow = random.random()
cloud = [0, 100]
time_cat = [0,1,2,3,4]
day = [0,1,2,3,4,5,6]
month = [0,1,2,3,4,5,6,7,8,9,10,11]
year = [2012,2013,2014,2015,2016,2017,2018]

def get_cat_data(data_list: list):
    return data_list[random.randint(0, len(data_list) - 1)]

def get_num_data(num_list):
    return random.randint(num_list[0], num_list[1])

def random_value():
    df = pd.DataFrame(columns=['holiday', 'temp', 'rain_1h', 'snow_1h', 'clouds_all','Day', 'Month','Year','time_category'],
                      data=[[get_cat_data(holiday), get_num_data(temp), get_num_data(rain), snow, get_num_data(cloud),
                             get_num_data(day),get_num_data(month),get_num_data(year),get_num_data(time_cat)]])
    cat_data = pd.DataFrame(columns=['weather_main'], data=[get_cat_data(weather_main)])

    X_encoded = pd.DataFrame(encoder.transform(cat_data).toarray(), columns=encoder.get_feature_names_out())
    df_final = pd.concat([df, X_encoded], axis=1)
    print("expected traffic_volume is : ",model.predict(df_final))


def enter_cat_value(options, field):
    print(f"Choose from for option {field}")
    for i in range(len(options)):
        print(f"{i+1} {options[i]}")

    while True:
        opt = int(input("Enter value: "))
        if 0 < opt <= len(options):
            return opt - 1
        else:
            print("You have entered wrong value")


def enter_number_value(range_value, field=""):
    value = float(input(f"Enter value for {field} range {range_value}: "))
    if range_value[0] <= value <= range_value[1]:
        return value
    else:
        print("You have entered wrong value")
        enter_number_value(range_value, field)


def values():
    df = pd.DataFrame(columns=['holiday', 'temp', 'rain_1h', 'snow_1h', 'clouds_all', 'Day', 'Month','Year','time_category'],
                      data=[[holiday[enter_cat_value(holiday, "Holiday")], enter_number_value(temp, "Temperature"),
                             enter_number_value(rain, "Rain"), enter_number_value([0, 1], "Snow"),
                             enter_number_value(cloud,"Cloud"),time_cat[enter_cat_value(time_cat,"time_category")],
                             day[enter_cat_value(day,"Day")],month[enter_cat_value(month,"Month")],year[enter_cat_value(year,"Year")]]])
    
    cat_data = pd.DataFrame(columns=['weather_main'], data=[weather_main[enter_cat_value(weather_main, "Weather")]])
    
    X_encoded = pd.DataFrame(encoder.transform(cat_data).toarray(), columns=encoder.get_feature_names_out())
    df_final = pd.concat([df, X_encoded], axis=1)
    print(df_final)
    print("expected traffic_volume is : ",model.predict(df_final))
    


if __name__ == "__main__":
    print("OPTIONS: \n"
          "1. Enter your values for each field \n"
          "2. For random value check\n"
          )

    while True:
        option = int(input("Enter your choice: "))
        if option == 1:
            values()
            sys.exit(0)
        if option == 2:
            random_value()
            sys.exit(0)    
        else:
            print("You have entered wrong value")
