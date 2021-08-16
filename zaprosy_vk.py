import requests
import pandas
import setting



def get_profiles(user_id, fields, access_token):
    url = 'https://api.vk.com/method/users.get?user_ids={}&fields={}&access_token={}&v=5.80'
    ids = ','.join(str(user) for user in user_id)
    fd = ','.join(fields)

    json_response = requests.get(url.format(ids, fd, access_token)).json()

    if json_response.get('error'):
        print(json_response.get('error'))
        return None
    users_d = json_response['response']
    df = pandas.DataFrame(users_d)
    return df

fd = ['first_name', 'last_name',  'city']
ids = [141536612, 139046077, 137464025, 109024405, 203137367, 191107635]

users_d = get_profiles(ids, fd, setting.token_vk_api)

a = users_d.iloc[0,:].to_string(header=False, index=True)
print(a)
#df.to_csv('file1.csv', encoding='utf-8')
