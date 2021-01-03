#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/3 21:23 
# @Author : mafei0728
# @Version：V 0.1
# @File : bar.py
# @desc :
# 1）准备数据
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

movie_name = ['雷神3：诸神黄昏', '正义联盟', '寻梦环游记']

first_day = [10587.6, 10062.5, 1275.7]
first_weekend = [36224.9, 34479.6, 11830]

x = range(len(movie_name))

# 2）创建画布
plt.figure(figsize=(20, 8), dpi=100)

# 3）绘制柱状图
plt.bar(x, first_day, width=0.2, label="首日票房")
plt.bar([i + 0.2 for i in x], first_weekend, width=0.2, label="首周票房")

# 显示图例
plt.legend()

# 修改x轴刻度显示
plt.xticks([i + 0.1 for i in x], movie_name)

# 4）显示图像
plt.show()
