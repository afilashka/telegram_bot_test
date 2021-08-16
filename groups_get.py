#работающий кусок команды для вывода сообществ Томска по ключевым словам

import pandas as pd
import numpy as np

import json
import requests
import time

def groups_search(key_word, count, token):
    url = 'https://api.vk.com/method/groups.search?q={}&sort=2&count={}&access_token={}&v=5.80'
    col_names =  ['id', 'name', 'screen_name', 'is_closed', 'type','photo_50' , 'photo_100', 'photo_200']
    my_df1  = pd.DataFrame(columns = col_names)

    for key in key_words:
        time.sleep(1)
        json_response = requests.get(url.format(key, city_id, token)).json()
        i = i + 1
        if json_response.get('error'):
            print(json_response.get('error'))
            print('error in step '&i)
        else:
            a = json_response['response']
        b    = a['items']
        d = a['count']
        if d != 0:
            c = pd.DataFrame(b)
            my_df1 = my_df1.append(c, ignore_index=True)
my_df1 = my_df1.drop(['photo_50' , 'photo_100', 'photo_200' ], axis = 1)
print(my_df1)

my_df1.to_excel('veg_tomsk4.xlsx', encoding='utf-8')