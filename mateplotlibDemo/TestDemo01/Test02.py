1  # !/usr/bin/env python
2  # _*_ coding: utf-8 _*_
3  # @Time : 2020/12/27 23:20
4  # @Author : mafei0728
5  # @Version：V 0.1
6  # @File : Test02.py
7  # @desc :
import numpy as np


def f_std(arr: list) -> float:
    return round(np.std(arr, ddof=1), 4)


def f_mean(arr: list) -> float:
    return round(np.mean(arr), 4)


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    print(np.mean(a).tolist())
