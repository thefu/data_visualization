import matplotlib.pyplot as plt

x_values = range(1 ,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)


plt.rcParams["font.sans-serif"]=["KaiTi"]
plt.rcParams["axes.unicode_minus"] = True
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
ax.axis([0, 1100, 0, 1100000])

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

# 第一个实参指定要以什么文件名保存图表，这个文件将存储到scatter_squares.py所在的目录
# 第二个实参指定将图表多余的空白区域裁剪掉，如果要保存图表周围多余的空包区域，只需要省略这个实参即可
plt.savefig('squares_plot.png', bbox_inches='tight')
