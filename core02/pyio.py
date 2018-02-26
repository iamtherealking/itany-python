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

