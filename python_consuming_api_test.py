import pandas as pd


import requests
import json
url="https://api.covid19api.com/summary"
response = requests.get(url).text
response_info = json.loads(response)
#print(response_info)
#print(type(response_info))
country_list = []
for country_info in response_info['Countries']:
    country_list.append([country_info['Country'],country_info['TotalConfirmed']])
#print(country_list)
country_df=pd.DataFrame(data=country_list,columns=['Country','Total_Confirmed'])
country_df.head(10)
print(country_df)



