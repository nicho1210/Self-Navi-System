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

#creating a list include the category of the parking_data
categories = ['id', 'area', 'name', 'summary', 'address', 'tel', 'payex', 'serviceTime', 'tw97x', 'tw97y', 'totalcar', 'totalmotor', 'FareInfo']

#create a excel that the first rows are the categories
df = pd.DataFrame(columns = categories)
df.to_excel('parking_data.xlsx', index = False)

for i in range(0, 1690):
    list_temp = []
    for cat in categories:
        #print(list2[0][0][cat])
        list_temp.append(list2[0][i][cat])
        #add the list to the next row of the excel
    df.loc[i] = list_temp
    df.to_excel('parking_data.xlsx', index = False)

