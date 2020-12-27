1  # !/usr/bin/env python
2  # _*_ coding: utf-8 _*_
3  # @Time : 2020/12/2 22:35
4  # @Author : mafei0728
5  # @Version：V 0.1
6  # @File : homework01.py
7  # @desc :
import time


def split_str(word: str) -> list:
    name = "马飞"
    list(map(lambda x: x + ":" + str(time.time()) + ":" + name, word.split("\"")))


if __name__ == '__main__':
    print(split_str("""我"爱"北"京"天"安"门"""))
