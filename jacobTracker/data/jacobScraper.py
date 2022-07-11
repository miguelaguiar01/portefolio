import urllib.request
from datetime import datetime
import calendar
import json
import time
import re

year = 218
url = 'https://hypixel-skyblock.fandom.com/api.php?action=query&format=json&prop=revisions&titles=Jacob%27s_Farming_Contest/Events/Year%20' + str(year) + '&formatversion=2&rvprop=content&rvslots=*'
urllib.request.urlretrieve(url, 'jacobTracker/data/jacob_raw.json')

file = open('jacobTracker/data/jacob_raw.json')
data = json.load(file)
table = data['query']['pages'][0]['revisions'][0]['slots']['main']['content']
table_row = table.split(' || ')

crop_name = ["Cactus","Carrot","Cocoa Beans","Melon","Mushroom","Nether Wart","Potato","Pumpkin","Sugar Cane","Wheat"]
cont = 0
arr = []
for i in range(len(table_row)):
    if(table_row[i][0] != '<' and table_row[i][1] != '|'):
        cont += 1
        #print(str(i) + ' ' + table_row[i] + '\n')
        arr.append(table_row[i])
        
res = []
for idx in range(len(arr)):
    if(idx % 3 == 0):
        res[idx:idx + 3] = [' | '.join(arr[idx:idx + 3])]

final = []
for i in range(124):
    col = res[i].split(' | ')
    time = col[1].split(', ')[1]
    crops = []
    crop_a = crops.append(col[2].split('ID|')[1].split('}}')[0])
    crops_b = crops.append(col[2].split('ID|')[2].split('}}')[0])
    crops_c = crops.append(col[2].split('ID|')[3].split('}}')[0])

    date = datetime.strptime(time, "%d %b %Y %H:%M:%S")
    timestamp = date.timestamp() + 3600

    dict = {
        'season': col[0].split(',')[0],
        'year': col[0].split(',')[-1],
        'time': timestamp,
        'crops': crops,
    }
    final.append(dict)

jsonString = json.dumps(final, indent=4)
jsonFile = open("jacobTracker/data/jacob_data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()


