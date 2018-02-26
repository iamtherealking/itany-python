# encoding=utf-8
# 程序结构
# __author__ = "崔译"
#
# # 分支
# num = int(input("请输入一个数\n"))
# if num % 2 == 0 and num != 0:# 注意此处的:
#     print("{}是一个偶数".format(num))
#     print("if.........")
# elif num == 0:
#     print("0...")
#     print("elif.......")
# else:
#     print("{}是一个奇数".format(num))
#     print("else.......")
#
# # 练习  输入一个0-99的数字，90以上 优秀  70-89 良好  60-69 及格 60以下不及格
#
#
#
#
# # 循环结构
i = 1
while True:
    print(i)
    i = i + 1
    if i >= 10:
        break

for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)


