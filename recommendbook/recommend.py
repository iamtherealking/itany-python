# 基于协同过滤算法的图书推荐系统

# Python Data Analysis Library
# Python 数据分析库
import pandas as pd

import numpy as np

from sklearn.metrics.pairwise import pairwise_distances

def do_recommend():
    # 1、获取数据集
    # csv comma-separated values
    # 逗号分割值（字符分割值）
    # 一种以文本形式存储数据的 格式
    # 张三,12,南京
    # 标准csv文件以,分割，但是，也可以以其他任意字符分割
    data_frame = pd.read_csv(
        "test.csv",
        sep="::",
        names=["user_name", "book_id", "rate"],
        engine="python")

    # print(data_frame.groupby("user_name").count())

    # 1.5 清洗数据


    # 2、创建矩阵 (用户id,图书id) ==> rate
    n_user = data_frame.user_name.unique().shape[0]
    n_book = data_frame.book_id.unique().shape[0]
    # print(n_user, n_book)
    matrix = np.zeros((n_user, n_book))
    # matrix[0][0] = 3?
    # 45874270::3234345::5
    pairwise_distances(matrix,metric="cosine")
    pass


do_recommend()

