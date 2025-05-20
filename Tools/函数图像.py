import numpy as np
import matplotlib.pyplot as plt


# 定义一元函数
def my_function(x):
    return 6 - (1.2 - 0.1 * x) / (0.1 * (1.2 ** x) + 0.1)


# 生成输入数据
x = np.linspace(0, 30, 100)  # 在 -5 到 5 之间生成 100 个均匀分布的点

# 计算函数值
y = my_function(x)

# 绘制图像
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = 6 - (1.2 - 0.1 * x) / (0.1 * (1.2 ** x) + 0.1)')
plt.grid(True)
plt.show()
