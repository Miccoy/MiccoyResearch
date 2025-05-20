# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 07:46:51 2024

@author: Miccoy
"""

# 定义样本数据
sample_data = [1.4,1.43,1.44,1.44,1.44,1.45,1.45,1.47,1.48,1.5]

# 计算样本均值
n = len(sample_data)
sample_mean = sum(sample_data) / n

# 计算样本方差
variance_numerator = sum((x - sample_mean) ** 2 for x in sample_data)
# print(variance_numerator)
sample_variance = variance_numerator / (n - 1)
# print(sample_variance)
# 计算样本标准差
sample_std_deviation = sample_variance ** 0.5

print("样本均值:", sample_mean)
print("样本方差:", sample_variance)
print("样本标准差:", sample_std_deviation)