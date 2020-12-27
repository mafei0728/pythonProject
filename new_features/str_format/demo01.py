
1  # !/usr/bin/env python
2  # _*_ coding: utf-8 _*_
3  # @Time : 2020/12/2 21:42
4  # @Author : mafei0728
5  # @Version：V 0.1
6  # @File : demo01.py
7  # @desc :


class Def:

    def fun01(self):
        self
        a = 12
        b = "mafei"
        print(f"{a}, {b}")

    def li(self):
        self
        k1 = ["a", "b"]

    def ma(self):
        self
        k = {"1":"b"}
        print(k.keys())


if __name__ == '__main__':
    d = Def()
    d.ma()
