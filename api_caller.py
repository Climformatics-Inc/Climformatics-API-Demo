import requests
import json
import pandas  
zone = 'zone1' # 'zone1', 'zone2', 'zone3', 'zone4', 'zone5', 'zone6'
variable = 'FWI' # 'FWI', 'temp', 'rh', 'ws'
time_scale = 'hourly' # 'hourly', 'monthly', 'daily'

## date range: 2017-05-01 00:00:00 to 2023-05-01 00:00:00
## UI link: https://6i7vehp3glxjkfaxo4vkwe25lu0cnrhs.lambda-url.us-west-1.on.aws/
year = '2022'
month = '10'
day = '01'
hour = '04' 

fut_year = '2022'
fut_month = '10'
fut_day = '30'
fut_hour = '00' 


link = f'https://6i7vehp3glxjkfaxo4vkwe25lu0cnrhs.lambda-url.us-west-1.on.aws/predict?zone={zone}&start_time={year}-{month}-{day}%20{hour}%3A00%3A00&end_time={fut_year}-{fut_month}-{fut_day}%20{fut_hour}%3A00%3A00&variable={variable}&time_scale={time_scale}'
response = requests.get(link)

print(response.json())