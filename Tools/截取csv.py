import os
import pandas as pd





# 检查是否成功更改工作目录
print(f"当前工作目录已更改为: {os.getcwd()}")




# 读取CSV文件
input_file = 'returns_LRR.csv'  # 替换为你的文件名和路径
output_file = 'returns_LRR_sample.csv'  # 输出的新文件名

# 使用pandas读取前10000行
n = 12212
df = pd.read_csv(input_file, nrows=n)

# 将截取的数据保存为新的CSV文件
df.to_csv(output_file, index=False)

print(f"前{n}行数据已保存至 {output_file}")
