# encoding=utf-8
# Python模块

__author__ = "崔译"


# 导入pymath模块
# 导入方式

# 方式1  import 模块名(文件名去掉后缀)
# 一般用于引入系统模块
# import core02.pymath
# import sys
# import os


# 方式2 import 模块名(文件名去掉后缀) as 别名
# import core02.pymath as math
# math.plus()

# 方式3   from 模块名 import 特定方法
# 一般用于引入第三方模块（包括自己开发的模块）
# from core02.pymath import plus
from core02.pymath import plus, mins

# 方式4
# 导入模块中所有方法,不建议使用该方式
# from core02.pymath import *

print(plus(2, 3))
print(mins(3, 5))




