import json

# 探索数据的结构。
filename = 'eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
"""首先导入模块json，以便恰当地加载文件中的数据，并将其存储到all_eq_data中，函数json.load()将数据转换为Python能够处理的格式，这里是一个庞大的字典，
    创建一个文件，以便将这些数据以易于阅读的方式写入其中，函数json.dump()接受一个JSON数据对象和一个文件对象，并将数据写入这个文件中，参数indent=4让dump()
    使用与数据结构匹配的缩进量来设置数据的格式
"""
all_eq_dicts = all_eq_data['features']

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(titles[:10])
print(lons[:10])
print(lats[:10])

