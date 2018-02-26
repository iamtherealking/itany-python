
def sysout(target):
    print(target)


sysout("abc")


def plus(x, y):
    return x + y


def do_nothing():
    pass


result = plus(3, 4)
print(result)


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

print(multi(y=3))


def test_args(name,*addrs):
    print(name)
    for item in addrs:
        print(item)


test_args("老王", "隔壁", "楼下隔壁", "楼上隔壁", "各种隔壁")


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


