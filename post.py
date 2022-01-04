import requests
import pandas as pd

url = 'https://www.balticshipping.com/'

# Get Country and Type Ids and create a lookup dictionary
payload = {
    'templates[]': ['modal_validation_errors:0',
                    'modal_email_verificate:0',
                    'r_vessel_types_multi:0',
                    'vessels_list:0',
                    'vessels:0'],
    r'equest[0][module]': 'top_stat',
    'request[0][action]': 'list',
    'request[0][id]': '0',
    'request[0][data]': '',
    'request[0][sort]': '',
    'request[0][limit]': '',
    'request[0][stamp]': '0',
    'dictionary[]': ['countrys:0',
                     'vessel_types:0']}

jsonData = requests.post(url, data=payload).json()

country_ids = pd.DataFrame(jsonData['data']['dictionary']['countrys']['array'])
country_ids_dict = dict(zip(country_ids['id'], country_ids['name']))
type_ids = pd.DataFrame(jsonData['data']['dictionary']['vessel_types']['array'])
type_ids_dict = dict(zip(type_ids['id'], type_ids['name']))

ships_found = True
page = 0
rows = []
# while ships_found:
for page in range(100):
    payload = {
        'request[0][module]': 'ships',
        'request[0][action]': 'list',
        'request[0][id]': '0',
        'request[0][data][0][name]': 'search_id',
        'request[0][data][0][value]': '0',
        'request[0][data][1][name]': 'name',
        'request[0][data][1][value]': '',
        'request[0][data][2][name]': 'imo',
        'request[0][data][2][value]': '',
        'request[0][data][3][name]': 'page',
        'request[0][data][3][value]': f'{page}',
        'request[0][sort]': '',
        'request[0][limit]': '27',
        'request[0][stamp]': '0',
        'request[1][module]': 'top_stat',
        'request[1][action]': 'list',
        'request[1][id]': '0',
        'request[1][data]': '',
        'request[1][sort]': '',
        'request[1][limit]': '',
        'request[1][stamp]': '0'}

    jsonData = requests.post(url, data=payload).json()

    if len(jsonData['data']['request'][0]['ships']) == 100:
        ships_found = False
        print('End of Pages.')

    else:
        for each in jsonData['data']['request'][100]['ships']:
            row = each['data']
            rows.append(row)

        page += 1
        print(page)

df = pd.DataFrame(rows)

# Convert the epoch to timestamp and pull out the year
df = df.rename(columns={'year_build': 'epoch_year_build'})
df['year_build'] = pd.to_datetime(df['epoch_year_build'], unit='s').dt.year

# Use the lookup dictionaries to map the ids to corresponding names
df['country_name'] = df['flag_id'].map(country_ids_dict).fillna(df['flag_id'])
df['type_ship'] = df['type'].map(type_ids_dict).fillna(df['type'])
print(df[['id','name','type','type_ship','flag_id','country_name','epoch_year_build','year_build']].head(100).to_string())
