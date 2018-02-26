class Student:

    # 类的静态属性
    some_static_attr = 1

    # 是类的构造方法
    # 方法名__init__(self)
    # self 是this对象
    # self 名称可以改变 但是不建议修改
    # !!! 一个类中所有成员方法的第一个参数都是self
    #     但是，在调用类中的方法的时候，不需要为self传值,由Python解释器传值

    # Python的成员属性，不需要声明在类中
    # 直接在init方法中使用self.属性名  声明成员属性
    def __init__(self,name="",age=""):
        self.id = None
        self.name = name
        self.age = age
        self.score = None
        pass

    def some_method(self):
        pass

    @classmethod
    def static_method(cls):
        print(cls)
        pass

Student.static_method()

# s = Student()
# # s.some_method()
# s1 = Student()
# # 可以对Python对象进行属性扩展
# s.addr = "南京"
# print(s.addr)
#
# print(s1.addr)
#
# # print(s)


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