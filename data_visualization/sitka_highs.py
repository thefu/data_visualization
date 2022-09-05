import csv
from datetime import datetime

import matplotlib.pyplot as plt
filename = 'sitka_weather_2018_simple.csv'
"""打开这个文件，并将返回结果的文件对象赋值给f，然后调用csv,reader()并将前面存储的文件对象作为实参传递给它，
从而创建一个与该文件相关联的阅读器对象，这个阅读器对象被复制给了reader"""
with open(filename) as f:
    reader = csv.reader(f)
    # 模块csv包含函数next()，调用它并传入阅读器对象时，它将返回文件中的下一行，在上述代码中，只调用了next()一次，因此得到的是文件的第一行
    header_row =next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# 根据最高温度绘制图形
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

plt.style.use('seaborn')
plt.rcParams["font.sans-serif"]=["KaiTi"]
plt.rcParams["axes.unicode_minus"] = True

# 设置图形的格式
ax.set_title("2018年每日最高温度", fontsize=24)
ax.set_xlabel('', fontsize=16)
# 调用fig.autofmt_xdate()来绘制倾斜的日期标签，以免其彼此重叠，
fig.autofmt_xdate()
ax.set_ylabel("温度（F）", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

"""reader处理文件中以逗号分割第一行的数据，并将每一项数据都作为一个元素存储在列表中，文件头STATION表示记录数据的气象站的编码，"""