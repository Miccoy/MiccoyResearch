# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 07:44:56 2024

@author: Miccoy
"""

import numpy as np

# 定义样本数据
sample_data = [1.4, 1.43, 1.44, 1.44, 1.44, 1.45, 1.45, 1.47, 1.48, 1.5]

# 计算样本均值
sample_mean = np.mean(sample_data)

# 计算样本方差
sample_variance = np.var(sample_data, ddof=1)

# 计算样本标准差
sample_std_deviation = np.std(sample_data, ddof=1)

print("样本均值:", sample_mean)
print("样本方差:", sample_variance)
print("样本标准差:", sample_std_deviation)
