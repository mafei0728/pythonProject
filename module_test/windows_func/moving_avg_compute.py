import math

1  # !/usr/bin/env python
2  # _*_ coding: utf-8 _*_
3  # @Time : 2020/12/10 19:41
4  # @Author : mafei0728
5  # @Version：V 0.1
6  # @File : moving_avg_compute.py
7  # @desc :
from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql import Window
from pyspark.sql.types import *
import os
import pandas as pd
import numpy as np


class TestDemo01:
    def __init__(self):
        self.spark = SparkSession.builder.appName("test").master("local[*]").getOrCreate()
        self.spark.sparkContext.setLogLevel("ERROR")
        self.url = "jdbc:mysql://hadoop01:3306/test?rewriteBatchedStatements=true"
        self.user = "root"
        self.password = "mafei0728"

    @staticmethod
    def std_j(arr: list) -> list:
        flag = [j for i in arr for j in i]
        return flag

    @staticmethod
    def f_mean(arr: list) -> float:
        return round(np.mean(arr).tolist(), 4)

    @staticmethod
    def f_std(arr: list) -> float:
        return round(np.std(arr, ddof=1).tolist(), 4)

    def fun01(self):
        properties = {'user': self.user, 'password': self.password}
        df = self.spark.read.jdbc(self.url, "v1_test", properties=properties)
        #
        w = Window.partitionBy("id").orderBy("test_date")
        df = df.withColumn("num", f.row_number().over(w))
        # 5为一个点
        df = df.withColumn("modulus", ((f.col("num") - 1) / 5).cast(IntegerType()) + 1)
        df = df.groupby("id", "modulus").agg(
            f.min("test_date").alias("min_date"),
            f.max("test_date").alias("max_date"),
            f.collect_list("test_value").alias("value_arr")
        )
        df = df.filter(f.size('value_arr') == 5)
        # st1
        w01 = Window.partitionBy("id").orderBy("modulus").rangeBetween(0, 0)
        w02 = Window.partitionBy("id").orderBy("modulus").rangeBetween(2, 2)
        w03 = Window.partitionBy("id").orderBy("modulus").rangeBetween(0, 2)
        df = df.withColumn("c1", f.collect_list('value_arr').over(w01))
        df = df.withColumn("c2", f.collect_list('value_arr').over(w02))
        df = df.withColumn("c3", f.collect_list('value_arr').over(w03))
        df = df.withColumn("g_id", f.min("modulus").over(w03))
        df = df.filter(f.size('c3') == 3)
        # df.show(truncate=False)
        # 二维矩阵拍平求均值,方差.
        flatten_v1 = f.udf(self.std_j, ArrayType(IntegerType()))
        df = df.withColumn("flatten1", flatten_v1(f.col('c1')))
        df = df.withColumn("flatten2", flatten_v1(f.col('c2')))
        df = df.withColumn("flatten3", flatten_v1(f.col('c3')))
        df.show(truncate=False)
        mean = f.udf(self.f_mean, DoubleType())
        std = f.udf(self.f_std, DoubleType())
        df = df.withColumn("std1", std(f.col('flatten1')))
        df = df.withColumn("mean1", mean('flatten1'))
        df = df.withColumn("std2", std('flatten2'))
        df = df.withColumn("mean2", mean('flatten2'))
        df = df.withColumn("std3", std('flatten3'))
        df = df.withColumn("mean3", mean('flatten3'))
        df.show(truncate=False)


if __name__ == '__main__':
    t = TestDemo01()
    t.fun01()
