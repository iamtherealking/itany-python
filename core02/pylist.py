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