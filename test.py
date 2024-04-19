import requests
import pandas as pd

def fetch_parking_data_from_free_api():
    url = "https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_alldesc.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']  # 确保此处路径正确
    else:
        return "Failed to retrieve data with status code: " + str(response.status_code)

# 使用此函数来获取数据
parking_data = fetch_parking_data_from_free_api()

#determine the type of the parking_data
print(type(parking_data))


#print the first data from the parking_data
for key in parking_data:
    print(key)
    #print(parking_data[key])
    
#make a list to save the data from the second key of the parking_data
list1 = []
for key in parking_data:
    if key == 'UPDATETIME':
        list1.append(parking_data[key])
print(list1)

#make a list to save the data from the second key of the parking_data
list2 = []
for key in parking_data:
    if key == 'park':
        list2.append(parking_data[key])
print(type(list2))

count = 0
for i in list2[0]:
    count += 1
    print(i['id'])
print(count)