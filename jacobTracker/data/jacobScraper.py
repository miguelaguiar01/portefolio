from datetime import datetime
import calendar
import json
import time

file = open('imported_raw.json')
data = json.load(file)
crops = ["Cactus","Carrot","Cocoa","Melon","Mushroom","Wart","Potato","Pumpkin","Sugar","Wheat"]
crop_name = ["Cactus","Carrot","Cocoa Beans","Melon","Mushroom","Nether Wart","Potato","Pumpkin","Sugar Cane","Wheat"]

arr = []

for i in range(124):
    time = data[i]['Earth Time (GMT/UTC)'].split(' ')[1:]
    crop = []
    for j in range(len(data[i]['Crops'].split(" "))):
        for k in range(len(crops)):
            if(data[i]['Crops'].split(" ")[j] == crops[k]):
                crop.append(crop_name[k])  
    date = datetime.strptime(" ".join(time), "%d %b %Y %H:%M:%S")
    timestamp = date.timestamp()

    dict = {
        'season': data[i]['SkyBlock Date'].split(',')[0],
        'year': data[i]['SkyBlock Date'].split(',')[-1],
        'time': timestamp,
        'crops': crop,
    }
    arr.append(dict)
jsonString = json.dumps(arr, indent=4)
jsonFile = open("jacob_data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()
