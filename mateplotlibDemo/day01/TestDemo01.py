# !/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/12/29 21:23
# @Author : mafei0728
# @Version：V 0.1
# @File : TestDemo01.py
# @desc :
import random

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def test01():
    plt.figure()
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.show()


def test02():
    # 1）创建画布，并设置画布属性
    plt.figure()
    # 2）保存图片到指定路径
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.show()
    plt.savefig("test.png")


def test03():
    # 画出温度变化图

    # 准备x, y坐标的数据
    x = range(60)
    y_shanghai = [random.uniform(15, 18) for i in x]

    # 1）创建画布
    plt.figure(figsize=(20, 8), dpi=180)

    # 2）绘制折线图
    plt.plot(x, y_shanghai)

    # 3）显示图像
    plt.show()


def test04():
    # 画布属性
    plt.figure(figsize=(20, 8), dpi=80)
    # 网格属性
    plt.grid(True, linestyle='--', alpha=0.5)
    # x, y轴属性
    plt.xlabel("时间")
    plt.ylabel("温度")
    # 标题
    plt.title("中午11点0分到12点之间的温度变化图示")
    # 修改x,y轴坐标的刻度显示
    x = range(60)
    x_axis = range(60)[::5]
    x_axis_label = ["11点{}分".format(i) for i in x][::5]
    plt.xticks(x_axis, x_axis_label)

    y_axis = [i for i in range(40)]
    plt.yticks(y_axis[::5])

    x_shanghai = [random.uniform(10, 20) for i in x]

    plt.plot(x, x_shanghai, label="上海")

    # 增加另外一个图像
    y_wuhan = [random.uniform(1, 10) for i in x]
    z_sanya = [random.uniform(20, 40) for i in x]
    # linestyle '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
    plt.plot(x, y_wuhan, color="r", linestyle='dotted', label="武汉")
    plt.plot(x, z_sanya, color="b", linestyle='--', label='三亚')
    # 3）显示图像
    plt.legend(loc="best")
    plt.show()


def test05():
    # 准备x, y坐标的数据
    x = range(60)
    y_shanghai = [random.uniform(15, 18) for i in x]
    # 增加北京的温度数据
    y_beijing = [random.uniform(1, 3) for i in x]

    # 1）创建画布
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=80)

    # 2）绘制折线图
    # plt.plot(x, y_shanghai)
    # plt.plot(x, y_shanghai, label="上海")
    axes[0].plot(x, y_shanghai, label="上海")
    # 使用多次plot可以画多个折线
    # plt.plot(x, y_beijing, color='r', linestyle='--', label="北京")
    axes[1].plot(x, y_beijing, color='r', linestyle='--', label="北京")

    # 显示图例
    # plt.legend(loc="best")
    axes[0].legend()
    axes[1].legend()

    # 增加以下两行代码
    # 构造x轴刻度标签
    x_ticks_label = ["11点{}分".format(i) for i in x]
    # 构造y轴刻度
    y_ticks = range(40)

    # 修改x,y轴坐标的刻度显示
    # plt.xticks(x[::5], x_ticks_label[::5])
    # plt.yticks(y_ticks[::5])
    axes[0].set_xticks(x[::5], x_ticks_label[::5])
    axes[0].set_yticks(y_ticks[::5])
    axes[1].set_xticks(x[::5], x_ticks_label[::5])
    axes[1].set_yticks(y_ticks[::5])

    # 添加网格显示
    # plt.grid(True, linestyle='--', alpha=0.5)
    axes[0].grid(True, linestyle='--', alpha=0.5)
    axes[1].grid(True, linestyle='--', alpha=0.5)

    # 添加x轴、y轴描述信息及标题
    # plt.xlabel("时间")
    # plt.ylabel("温度")
    # plt.title("中午11点0分到12点之间的温度变化图示")
    axes[0].set_xlabel("时间")
    axes[0].set_ylabel("温度")
    axes[0].set_title("上海中午11点0分到12点之间的温度变化图示")
    axes[1].set_xlabel("时间")
    axes[1].set_ylabel("温度")
    axes[1].set_title("北京中午11点0分到12点之间的温度变化图示")

    # 3）显示图像
    plt.show()


if __name__ == '__main__':
    test04()
