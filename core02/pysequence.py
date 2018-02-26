
# 序列

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
print()


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


