import requests
import pandas
import setting



def get_profiles(user_id, access_token):
    url = 'https://api.vk.com/method/users.get?user_ids={}&fields={}&access_token={}&v=5.80'
    #ids = ','.join(str(user) for user in user_id) пока сделаем для одного юзера
    fields = ['first_name', 'last_name', 'sex', 'city', 'bdate', 'education']
    fd = ','.join(fields)

    json_response = requests.get(url.format(user_id, fd, access_token)).json()

    if json_response.get('error'):
        #print(json_response.get('error'))
        return 'такого аккаунта нет, либо закрытый аккаунт'
    users_d = json_response['response']
    df = pandas.DataFrame(users_d)
    a = df.iloc[0, :].to_string(header=False, index=True)
    return a






#ids = 15631

#users_d = get_profiles(ids, setting.token_vk_api)

#print(users_d)
#df.to_csv('file1.csv', encoding='utf-8')
