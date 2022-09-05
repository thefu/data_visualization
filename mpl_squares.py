import matplotlib.pyplot as plt

plt.style.use('seaborn')
plt.rcParams["font.sans-serif"]=["KaiTi"]
plt.rcParams["axes.unicode_minus"] = True

# 创建一个名为input_values的列表，在其中存储输入值，squares列表的数据为输出值
input_values = [1, 2, 3, 4, 5]

# 创建一个名为squares的列表，在其中存储要用来制作图表的数据，
squares = [1, 4, 9, 16, 25]


# 调用subplots函数，这个函数可在一张图表中绘制一个或多个图表，
fig, ax = plt.subplots()

# 设置图表标题并给坐标加上标签
ax.plot(input_values, squares, linewidth=3)

ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值得平方", fontsize=24)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

plt.show()