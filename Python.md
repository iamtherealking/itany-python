# Python

## 主讲：崔译

## 一、什么是Python

简单并且简约的语言。伪代码式的特征，能让程序员 更加专注于  **解决问题**，而不是语言本身 

开源( open source / free )

> a  = 用户输入一个数
>
> 如果 a  对2 取余  结果为0 
>
> ​	输出 偶数
>
> 否则
>
> ​	输出 奇数

- 跨平台

  **如果不使用系统依赖性的特征** ，Python 能够再任何一种平台上运行

- 解释性

  不需要字节码文件，直接从源代码运行

  > 在程序内部，Python会将源代码转换为字节码，然后转换为机器语言

- 面向对象

- 可扩展性

  对C 或者C++程序具有良好的支持

- 可嵌入性

  可以在C或者C++代码中 嵌入 Python

- 丰富的库（jar）

## 二、Python环境搭建

[Python官网](https://www.python.org)

### 1、windows 

- 下载安装包
- 安装

### 2、mac os

> $> brew install python3

### 3、linux

> $> sudo apt-get install python3

### 4、 Python2 or Python3 ?

Python2 和 3 在社区中都处于 活跃状态，但是更建议大家使用3

## 三、HelloWorld

> 向编程之神所称颂的传统咒语，愿他能够保佑你更好的学习这门语言

```python
$>  python
>>> print("HelloWorld") # python3
>>> print "HelloWorld"  # python2
```

```python
>>> import this
>>> # Python之禅
```

创建 hello.py 文件,输入以下内容

```python
# encoding=utf-8
# 这是Python的注释

__author__ = "崔译"

for i in range(1,10):
	for j in range(1,i + 1):
		print("{}*{}={}".format(i,j,i*j),end=" ")
	print()
```

在文件所在路径下，执行以下命令

```powershell
$> python hello.py
```

## 四、数据类型

**Python 是强 面向对象的，认为所有的一切都是对象，包括数字**

### 1、数字类型

```python
# encoding=utf-8

__author__ = "崔译"

# Python不区分整数和小数，整数没有范围
age = 22
age = 2200000000
print(age)

age = 22.2
print(age)

age = 5E2
print(age)

# 字符串数字转换
num_str = "3333"
print(type(num_str))
num_int = int(num_str)
print(type(num_int), num_int)
```

### 2、字符串类型

```python
# encoding=utf-8

__author__ = "崔译"

# python中存在字符串类型 ，使用 一对单引号 或者 一对双引号  或者 一对 三个单引号 表示
str1 = 'abc'

str2 = "abc"

# 在python中， 上述两种表现方式 没有区别

# 对于 一对 三个单引号  用于表示 多行文本
str3 = '''这是一个字符串
这是一个可以换行的字符串
这真的是可以换行的
'''

print(str3)

# 字符串方法
some_str = "  askldajksdjaklds  "

# 长度
print(len(some_str))

# trim
print("-"+some_str+"-")
print("-"+some_str.strip()+"-")

# 模板字符串
new_str = "我叫做{0},今年{1}岁,住在:{2}".format("abc", 22 , "南京")
print(new_str)
new_str = "我叫做{},今年{}岁,住在:{}".format("abc2", "aba", "南京")
print(new_str)

new_str = "我叫做{name},今年{age}岁,住在:{address}".format(name="abc2", address="aba", age="南京")
print(new_str)

# 常用方法  类比java 推断
```

## 五、Python的编码规范

### 1、逻辑行  和  物理行

- 物理行

  Physical line 

  在编写程序过程中，程序员看到的一行

- 逻辑行

  Logical Line 逻辑行

  Python 看到的每个语句

一个物理行中包含多个逻辑行

**Python会假定每一个物理行 对应一个逻辑行**

**即：Python鼓励每行最多只有一个语句**

如果 非要在一行中写两个语句，此时 必须使用 **;** 隔离

一个逻辑行中包含多个物理行

- 显式链接（使用\进行物理行的连接）
- 隐式链接

### 2、缩进

**空白区 在Python中 （各行的开头）非常重要！非常重要！非常重要！**

即，我们讲的缩进

在逻辑行（每个语句）前保留空白区（缩进），用以确定各个逻辑行之间的级别和分组

**在Python中，不使用{} 表示一个代码块，用相同的缩进表示在一个代码块中**

```python
for i in range(1, 10):
    print(i)
	print("hello")

for i in range(1, 10):
    print(i)
print("hello")

```

## 六、运算符

```python
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

```

## 七、程序结构

### 1、分支

```python
# encoding=utf-8
# 程序结构
__author__ = "崔译"

# 分支
num = int(input("请输入一个数\n"))
if num % 2 == 0 and num != 0:# 注意此处的:
    print("{}是一个偶数".format(num))
    print("if.........")
elif num == 0:
    print("0...")
    print("elif.......")
else:
    print("{}是一个奇数".format(num))
    print("else.......")

# 练习  输入一个0-99的数字，90以上 优秀  70-89 良好  60-69 及格 60以下不及格

```

### 2、循环结构

#### 2-1 while循环

```python
i = 1
while True:
    print(i)
    i = i + 1
    if i >= 10:
        break
```

#### 2-2 for 循环

```python
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)
```

## 八、函数

### 1、定义方式

```python
def 函数名(参数列表):
    函数体
    函数体
    函数体
```

```python
def sysout(target):
    print(target)
def plus(x, y):
    return x + y    
def sysout(target):
    print(target)
sysout("abc")
def do_nothing():
    pass
result = plus(3, 4)
print(result)
```

### 2、关于参数

#### 2-1 参数的默认值

```python
# 可以为参数设置默认值
def load_users(page_no=1):
    print(page_no)


# => 4
load_users(4)

# => None
load_users(None)

# 如果方法参数有默认值，那么在调用该函数的时候，可以不传该参数，该参数此时会使用默认值。0
load_users()


def multi(x=1, y=2):
    return x * y


print(multi())
print(multi(3, 4))
# 注意按参数顺序赋值
print(multi(3))

```

#### 2-2 关键字参数

```python
def multi(x=1, y=2):
    return x * y

# 给y参数赋值，不给x赋值
print(multi(y=3))
```

#### 2-3 可变长参数

```python
def test_args(name,*addrs):
    print(name)
    for item in addrs:
        print(item)
test_args("老王", "隔壁", "楼下隔壁", "楼上隔壁", "各种隔壁")
```

### 3、**DocStrings**

>Python中有一个  甚是优美 的功能，叫做文档字符串(Documentation Strings)
>
>简称DocStrings 
>
>是一个应该在定义函数时要使用的功能，能够帮助我们更快的理解该函数所完成的功能

**令人惊叹的是，当程序在运行过程中，可以通过以下代码获取到DocStrings**

```python
def load_data(page_no,page_size):
    '''
    加载数据
    :param page_no: 第几页
    :param page_size: 每页几条数据
    :return: 结果元组
    '''
    arr = []
    return arr


print(load_data.__doc__)

print("".strip.__doc__)
```

练习：

> 定义一个 calc 方法，方法接收一个 整数n
>
> 求 1 + 2 + 3 + 4 .... + X <= n 的 X 的最大值
>
> 将最大值返回
>
> n 由 用户在控制台 输入

## 九、Python的模块

Python 模块，是一个py文件，包含了Python对象的定义 和 Python 语句、函数

定义一个py文件，叫做pymath.py

```python
# encoding=utf-8
# Python模块

__author__ = "崔译"
# 一个py文件就是一个 模块
# 一个模块可以被其他模块导入

# 加
def plus(x, y):
    return x + y


# 减
def mins(x, y):
    return x - y


# 乘
def multiply(x, y):
    return x * y


# 除
def devide(x, y):
    return x / y


```

在其他模块中，使用pymath模块的方式

```python
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
```

**当导入一个模块的时候，Python解释器对模块的搜索顺序**

1. 当前目录

2. PYTHONPATH

3. 查看默认路径

   >Unix : /usr/local/lib/python

## 十、Python中的包

必须存在一个 \_\_init\_\_.py文件，用于标识该文件夹是一个Python包

这个文件可以是一个空文件

## 十一、Python的面向对象

### 1、Python类的定义

```python
class Student:
    pass

s = Student()
print(s)
```

### 2、类的构造方法

```python
class Student:

    # 是类的构造方法
    # 方法名__init__(self)
    # self 是this对象
    # self 名称可以改变 但是不建议修改
    # !!! 一个类中所有成员方法的第一个参数都是self
    #     但是，在调用类中的方法的时候，不需要为self传值,由Python解释器传值
    def __init__(self):
        pass
```

### 3、成员属性

```python
class Student:
    # Python的成员属性，不需要声明在类中
    # 直接在init方法中使用self.属性名  声明成员属性
    def __init__(self,name="",age=""):
        self.id = None
        self.name = name
        self.age = age
        self.score = None
        pass

s = Student()
s1 = Student()
# 可以对Python对象进行属性扩展
s.addr = "南京"
print(s.addr)
print(s1.addr) # 报错
```

### 4、成员方法

```python
 class Student:
    def some_method(self):
        pass
```

### 5、静态属性

```python
class Student:

    # 类的静态属性
    some_static_attr = 1
    
    
# Python 一定要使用类名访问静态属性
print(Student.some_static_attr)

s = Student()
# 找的是s的成员属性，由于成员属性不存在，找了静态属性 >> 1
print(s.some_static_attr)
# 为s添加一个成员属性，值是2
s.some_static_attr = 2
# s存在成员属性，值是2
print(s.some_static_attr)

print(Student.some_static_attr)
```

### 6、静态方法

```python
class Student:
    @classmethod
    def static_method(cls):
        print(cls)
        pass

Student.static_method()
```

## 十二、异常

```python
# print(1 / 0)


# try:
#     print(1 / 0)
#     print("正常执行")
#     pass
# except:
#     # 捕获所有异常
#     print("出异常了")
#     pass
# finally:
#     # 不论是否有异常，都会执行
#     print("执行结束")
#     pass

# try:
#     # print(1 / 0)
#     s = None
#     s.strip()
#     print("正常执行")
#     pass
# except ZeroDivisionError:
#     # 捕获所有异常
#     print("出异常了")
#     pass
# except AttributeError:
#     print("出了AttributeError")
# finally:
#     # 不论是否有异常，都会执行
#     print("执行结束")
#     pass

try:
    print(1 / 0)
    # s = None
    # s.strip()
    print("正常执行")
    pass
except (ZeroDivisionError, AttributeError) as e:
    print("出异常了", e)

# try:
#     print(1 / 0)
#     # s = None
#     # s.strip()
#     print("正常执行")
#     pass
# except ZeroDivisionError as e:
#     # 捕获所有异常
#     print("出异常了",e)
#     pass
# except AttributeError as e:
#     print("出了AttributeError",e)
# finally:
#     # 不论是否有异常，都会执行
#     print("执行结束")
#     pass

class SomeException(BaseException):
   pass



try:
    s = input("请输入\n")
    # 比的是地址  是否是同一个对象
    # if s is "abc":
    # 比的是值
    if s == "abc":
        # 抛出异常
        raise SomeException()

except SomeException:
    print("出异常了")
```

## 十三、IO

```python
print("")
input("请输入")

# encoding=utf-8
# 文件读写操作

__author__ = "崔译"


# 向文件中写内容
def do_write():
    '''
        获取文件对象
        存在mode的参数,决定文件的打开方式
        'r'       只读 (默认)
        'w'       写, 覆盖原有数据
        'x'       创建新文件，写
        'a'       打开文件,如果文件存在，追加内容，如果不存在，创建新文件
        'b'       二进制数据
        't'       文本数据（默认）
        '+'       打开文件，读写操作
        所有模式可以连在一起使用
    '''
    file = open("test.txt", mode="w", encoding="utf-8")
    # 写入数据
    m = input("输入内容\n")
    file.write(m)
    # 关闭
    file.close()
    pass


# 从文件中读取数据
def do_read():
    # 获取文件
    # file = open("test.txt",encoding="utf-8")
    # read方法存在参数n，表示读取的文件长度，如果n不提供或者提供负值，则读取整个文件
    # str = file.read()
    # s = file.readline()
    # print(s)
    # file.close()
    s = open("test.txt",encoding="utf-8").read()
    print(s)


# do_write()
do_read()
```

## 十四、数据结构

数据结构：Data Structures ， 只是一种结构，用于存储数据

### 1、列表

**类似于JavaScript中的数组**

```python
# Python中的列表

# 定义
ls = []
print(ls)

ls = [1,2,3,2,2]
print(ls)

# 添加
ls.append(6)
ls.append(7)
ls.append(2)
ls.append(2)
print(ls)


# 删除
ls.remove(6)
print(ls)


# 修改
ls[3] = "aaa"
print(ls)

# 查询
# 查询-1 根据下标查询
item = ls[2]
print(item)

# 查询-2 查询下标
idx = ls.index("aaa")
print(idx)

# print(ls.index("ddd")) 不存在  报错

# 查询-3 查询某个元素在列表中出现的次数
# 查询1在列表中出现的次数
count = ls.count(1)
print(count)

count = ls.count(2)
print(count)


print("=====================================")

print(ls)
# 删除并返回 列表的最后一个元素
# pop存在参数index 指定删除并返回的元素的下标（从0开始）
item = ls.pop()
print(ls,";item:",item)

# 反转 列表
ls.reverse()
print(ls)

# 排序
ls = [345,34,65,4,2,34,65,6,6789,1]
ls.sort()
print(ls)

ls = ["asdasd","as","sfgkldjfklgsjdfg","aaaa"]
ls.sort()
print(ls)

ls.sort(key=lambda x:len(x))
print(ls)


ls = [2,45,-67,-3,25,-56]

ls.sort(key=lambda x:abs(x))

print(ls)
```

### 2、元组

Tuple

近似的看成 **枚举**

```python
# 元组类型
zoo = ('elephant', 'chicken', 'dog')

# 只能通过下标访问
print(zoo[1])
```

### 3、字典

dictionary .  java中的  **Map**  ,  更加 类似于  JSON 对象

```python
# 字典

# 定义一个空字典
dic = {}

# 定义一个有内容的字典
dic = {
    "username": "老王",
    "address": "隔壁"
}

print(dic)

# 增
dic['age'] = 99
print(dic)
# 删
del dic['age']
print(dic)
item = dic.pop("address")
print(item)

print(dic)

# 改
print(dic)
dic['username'] = "呵呵"
print(dic)

# 查
print("---查询---")
print(dic['username'])
print(dic.get("username"))

# 清空
dic.clear()
print(dic)

# 遍历
dic = {
    "username": "老王",
    "address": "隔壁"
}
print("遍历----方式1")
keys = dic.keys()
for i in keys:
    print(i)

print("遍历----方式2")
values = dic.values()
for i in values:
    print(i)


print("遍历----方式3")
items = dic.items()
for i in items:
    print(i[0],i[1])
```

### 4、集合

java中的 Set ， **无序不可重复**

```python
s = set([1,2,3,4])
# 添加
s.add()
# 删除
s.remove(2)
```

### 5、**序列**

#### 5-1 形态

序列主要有三种形态： 

- 列表
- 元组
- 字符串

#### 5-2 主要功能

- 资格测试
- 索引操作

#### 5-3 资格测试

Membership Test

使用 in 或者 not in 语法 判断 一个 元素是否在 序列中

```python
ls = [12,45,76,787,5896789,"dasasd"]

tp = ("aaa","bbb","ccc")

st = "ahfsdjka是shdfjk"


# 资格测试
# print(45 in ls)
# print(45 not in ls)
# print("aaa" in tp)
# print("aaa" not in tp)
# print("sdj" in st)
# print("sdj" not in st)

# for i in ls:
#     print(i, end=",")
# print()
# for i in tp:
#     print(i,end=",")
# print()
# for i in st:
#     print(i,end=",")
```



#### 5-4 索引操作（**切片操作**）

```python

# 序列

ls = [12,45,76,787,5896789,"dasasd"]

tp = ("aaa","bbb","ccc")

st = "ahfsdjka是shdfjk"

# 切片操作

# 使用 下标访问内容
# print(ls[1])
# print(tp[1])
# print(st[3])

# 使用 下标访问，下标为 负值  从后向前索引，从-1开始
# print(ls[-1])
# print(tp[-1])
# print(st[-1])

# 使用下标区间访问 [m,n)
# print(ls[2:5])
# print(tp[1:2])
# print(st[3:9])

# 使用下标区间访问
# print(ls[2:])
# print(st[:12])

# print(st[1:-1])
# print(st[:])


# 切片操作可以提供第三个参数，表示 步长step
st = "0123456789"
# print(st[::2])

print(st[::-1])

newls = ls[::-1]
print(ls)
print(newls)

```

