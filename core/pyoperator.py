# encoding=utf-8
# python 运算符
__author__ = "崔译"

# python 支持的运算符
# + - * / % += -= *= /=
# > < == != >= <=

# 次方 js中ES6新特性 也支持 **
result = 2 ** 3
print(result)

# python3 中 / 是有小数的
result = 1 / 3
print(result)

# // 除取整
result = 1 // 3
print(result)

# % 取余
result = 5 % 2
print(result)
# 注意，和java的区别
result = -5 % 2
print(result)

result = -5 // 2
print(result)

# 布尔类型  True False
print(1 > 3)
print(False)

# 空类型
some_thing = None
print(some_thing == None)
print(some_thing is None)
print(some_thing is not None)

# 逻辑运算符
# & 并且  | 或者
print((1 < 2) & (2 < 4))

print(True | False)
print(False)

# and  or not
print(False and True)
print(False or True)
print(not True)

# 比较运算符 > < 可以连用
a = 2
print(3 > a > 1)

# 比较运算符 可以用于字符串
print("abc" > "def")
print("dfbc" > "def")
print("中" > "国")

# 字符串可以 * 一个数字

a = "abc"
result = a * 10
print(result)

# 注意！！！！！！！！！  Python中 没有 ++ 和 --
