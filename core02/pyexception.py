
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

# class SomeException(BaseException):
#    pass
#
#
#
# try:
#     s = input("请输入\n")
#     # 比的是地址  是否是同一个对象
#     # if s is "abc":
#     # 比的是值
#     if s == "abc":
#         # 抛出异常
#         raise SomeException()
#
# except SomeException:
#     print("出异常了")

