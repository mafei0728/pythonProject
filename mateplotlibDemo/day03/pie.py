#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/3 21:32 
# @Author : mafei0728
# @Version：V 0.1
# @File : pie.py
# @desc :
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

movie_name = ['雷神3：诸神黄昏', '正义联盟', '东方快车谋杀案', '寻梦环游记', '全球风暴', '降魔传', '追捕', '七十七天', '密战', '狂兽', '其它']

place_count = [60605, 54546, 45819, 28243, 13270, 9945, 7679, 6799, 6101, 4621, 20105]
# 1）准备数据
movie_name = ['雷神3：诸神黄昏', '正义联盟', '东方快车谋杀案', '寻梦环游记', '全球风暴', '降魔传', '追捕', '七十七天', '密战', '狂兽', '其它']

place_count = [60605, 54546, 45819, 28243, 13270, 9945, 7679, 6799, 6101, 4621, 20105]

# 2）创建画布
plt.figure(figsize=(20, 8), dpi=100)

# 3）绘制饼图
plt.pie(place_count, labels=movie_name, autopct="%1.2f%%",
        colors=['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c', 'g', 'y'])

# 显示图例
plt.legend(loc=4)

# 添加标题
plt.title("电影排片占比")

# 4）显示图像
plt.show()
