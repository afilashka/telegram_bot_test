import requests

import pandas

fields = ['first_name', 'last_name', 'sex', 'city', 'bdate', 'education']
token = '48fd71c748fd71c748fd71c7b6488584d0448fd48fd71c729e44ec3fed16423d006fe2a'
users = [141536612, 139046077, 137464025, 109024405, 203137367, 191107635]

def get_profiles(user_id, fields, access_token):
    url = 'https://api.vk.com/method/users.get?user_ids={}&fields={}&access_token={}&v=5.80'
    json_response = requests.get(url.format(user_id, fields, access_token)).json()
    if json_response.get('error'):
        print(json_response.get('error'))
        return None
    return json_response['response']

ids = ','.join(str(user) for user in users)
fd = ','.join(fields)

users_d = get_profiles(ids, fd, token)
df = pandas.DataFrame(users_d)

print(df)

df.to_csv('file1.csv', encoding='utf-8')
