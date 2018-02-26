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