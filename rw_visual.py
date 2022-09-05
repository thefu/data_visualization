import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:

    rw = RandomWalk(50000)
    rw.fill_walk()
    plt.style.use('classic')

    """创建图表时，可传递参数figsize以指定生成的图形的尺寸，需要给参数figsize指定一个元组
        向Matplotlib指出绘图窗口的尺寸，单位为英寸
        Matplotlib假定屏幕分辨率为100像素1英寸，如果上述代码指定的如表尺寸不合适，
        可辊距需要调整数字吗，如果知道当前系统的分辨率，
        可通过参数dpi向plot.subplots()传递该分辨率，以有效的利用屏幕空间
    """
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 突出起点和终点
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk ? (y/n): ")
    if keep_running == 'n':
        break