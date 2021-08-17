# работающий кусок команды для вывода сообществ  по ключевому слову
# сортировка по отношению дневной посещаемости к количеству пользователей;



import pandas as pd
import numpy as np

import requests
#import time
import setting


def groups_search(key_word, count, token):
    url = 'https://api.vk.com/method/groups.search?q={}&sort=2&count={}&access_token={}&v=5.80'
    col_names = ['id', 'name', 'screen_name', 'is_closed', 'type', 'photo_50', 'photo_100', 'photo_200']
    my_df_temp = pd.DataFrame(columns=col_names)
    #time.sleep(0.3)
    json_response = requests.get(url.format(key_word, count, token)).json()

    if json_response.get('error'):
        print(json_response.get('error'))
    else:
        a = json_response['response']
        b = a['items']
        d = a['count']
    if d != 0:
        c = pd.DataFrame(b)
        my_df_temp = my_df_temp.append(c, ignore_index=True)


    my_df_temp = my_df_temp.drop(['photo_50', 'photo_100', 'photo_200'], axis=1)
    return my_df_temp


group = groups_search('жимолость', '20', setting.token_vk_api)
print(group)