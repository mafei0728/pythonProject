#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/12/30 22:32 
# @Author : mafei0728
# @Version：V 0.1
# @File : Test01.py
# @desc : 数学函数
import matplotlib.pyplot as plt
import numpy as np


def fun01():
    ax = plt.gca()
    # gca:get current axis得到当前轴
    # 设置图片的右边框和上边框为不显示
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # 挪动x，y轴的位置，也就是图片下边框和左边框的位置
    ax.spines['bottom'].set_position(('data', 0))  # data表示通过值来设置x轴的位置，将x轴绑定在y=0的位置
    ax.spines['left'].set_position(('axes', 0.5))  #

    """
    反比例函数
    :return:
    """
    x = np.linspace(-100, 100, 100)
    y = 1 / x
    plt.xticks(range(-100, 100)[::10])
    plt.plot(x, y)
    plt.show()


def fun02():
    x = np.linspace(1, 100, 100)
    y = np.sqrt(x)
    plt.xticks(range(-100, 100)[::5])
    plt.plot(x, y)
    plt.show()


def fun03():
    ax = plt.gca()
    # gca:get current axis得到当前轴
    # 设置图片的右边框和上边框为不显示
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # 挪动x，y轴的位置，也就是图片下边框和左边框的位置
    ax.spines['bottom'].set_position(('data', 0))  # data表示通过值来设置x轴的位置，将x轴绑定在y=0的位置
    ax.spines['left'].set_position(('axes', 0.5))  #
    x = np.linspace(-100, 100, 100)
    y = np.power(x, 2)
    plt.xticks(range(-100, 100)[::10])
    plt.plot(x, y)
    plt.show()


def fun04():
    ax = plt.gca()
    # gca:get current axis得到当前轴
    # 设置图片的右边框和上边框为不显示
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # 挪动x，y轴的位置，也就是图片下边框和左边框的位置
    ax.spines['bottom'].set_position(('data', 0))  # data表示通过值来设置x轴的位置，将x轴绑定在y=0的位置
    ax.spines['left'].set_position(('axes', 0.5))  #
    x = np.linspace(-10, 10, 100)
    y = 10* np.power(x, 2) + 2 * x + 1
    plt.xticks(range(-100, 100)[::10])
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    fun04()
