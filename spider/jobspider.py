# encoding=utf8
# 前程无忧 爬虫
__author__ = "崔译"

# 发送http、https请求
from urllib import request

# 用于解析处理HTML格式的字符串
from bs4 import BeautifulSoup

# 用于连接mysql数据库
import pymysql

# 用于连接redis数据库
import redis

# 用于Excel读写操作
from openpyxl import Workbook

# 导入time 模块
import time


# 确定要爬取的url
url = 'http://search.51job.com/list/070200,000000,0000,00,9,99,Java,2,{}.html'

# 模拟浏览器发送请求
# 模拟请求头信息
headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Connection":"keep-alive",
    "Host":"search.51job.com",
    "Referer":"http://search.51job.com/list/070200,000000,0000,00,9,99,Java,2,4.html",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"
}


# 进行爬取操作
def do_spider(page_no=1):
    # 创建请求对象，并且同时设置请求头
    req = request.Request(url.format(page_no), headers=headers)
    # 打开创建的请求，并读取响应的数据
    # 读取到的是bytes 类型
    html_bytes = request.urlopen(req).read()
    # print(type(html_bytes)) # =><class 'bytes'>
    # 将读取的内容转成str类型
    # str 将任意类型转换为字符串类型，第二个参数是字符集
    # 对于爬虫而言，该字符集是 爬取的网站的字符集
    html_code = str(html_bytes, "gbk")

    # file = open("template.html",mode="w",encoding="gbk")
    # file.write(html_code)
    return html_code


# 测试方法
def load_html():
    file = open("template.html",encoding="gbk")
    html_code = file.read()
    return html_code;


# 解析html
def parse_html(html):
    # 方式1  使用正则表达式
    # 方式2  使用Xpath  是爬虫框架scrapy 所必须的技术
    # 方式3  使用 Python 第三方模块 Beautifulsoup ==> bs4
    #               能够将html语法的字符串进行解析，使用其中的方法来处理html

    # 解析参数
    soup = BeautifulSoup(html, "html.parser")
    # print(type(soup))
    # 以下所有的方法都可以用于BeautifulSoup或者Tag类型

    # find("标签名") 返回第一个对应的标签  相当于  .标签名
    # print(soup.find("input"))
    # print(soup.input)


    # find_all() 用法和find一致，只是返回的是所有的满足条件的标签，包括子标签
    # print(soup.find_all("input"))
    # div = soup.find_all("div")[1]
    # print(div[1])
    # div_in = div.find_all("div")[0]
    # print(div_in)

    # select() 参数是Css选择器 返回的是 列表
    # 所有的css选择器都能用
    # fot = soup.select(".footer .nag")
    # print(fot)

    # get_text() 获取标签内容 获取标签中的所有文字，包括子标签中的文字
    # text = soup.select("#area_channel_layer .tle")[0].get_text()
    # print(str(text).strip())

    result_list = []
    content_div = soup.select("#resultList")[0]
    item_divs = content_div.select(".el")

    # 去除表头，由于range 本身就是左闭右开，所以不需要len-1
    for item_div_index in range(1,len(item_divs)):
        # 对应一条数据
        item_div = item_divs[item_div_index]
        # print(item_div.get_text().strip())
        # job = item_div.p.get_text().strip()
        spans = item_div.find_all("span")
        # 将数据封装成 字典
        result_item = {
            "job": spans[0].get_text().strip(),
            "company": spans[1].get_text().strip(),
            "address": spans[2].get_text().strip(),
            "salary": spans[3].get_text().strip(),
            "publishDate": spans[4].get_text().strip()
        }
        # 将字典（每条数据） 放到列表中
        result_list.append(result_item)
    return result_list


# 存储到mysql
def export_to_mysql(result):
    # 创建 连接信息的 字典
    config = {
        "host": "localhost",
        "port": 3306,  # 默认是3306，可以不写
        "user": "root",
        "passwd": "",
        "db": "python",
        "charset": "gbk"
    }
    # 获取Connection
    db = pymysql.connect(**config)
    # 获取游标对象（cursor）, 其实对应PreparedStatement对象
    cursor = db.cursor()
    try:
        # 遍历参数中的所有的数据
        for item in result:
            # 创建sql语句
            sql = '''
                insert into
                    t_jobs
                    (job,address,salary,company,publishDate)
                values 
                    ('%s','%s','%s','%s','%s')                  
            ''' % (item['job'],item['address'],item['salary'],item['company'],item['publishDate'])

            # 执行sql语句
            cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)

        db.rollback()
    db.close()


# 将数据导出到redis
def export_to_redis(result):
    # 连接到redis
    r = redis.Redis(host="localhost",port=6379,db=0,charset="gbk")
    for item in result:
        r.lpush("jobs", str(item))


# 从redis读取数据
def read_from_redis():
    r = redis.Redis(host="localhost", port=6379, db=0, charset="gbk" , decode_responses=True)
    print(r.lrange("jobs",0,-1))


# 导出到Excel文件中
def export_to_excel(result):
    # 创建工作表
    wb = Workbook()
    # 创建worksheet

    sheet = wb.create_sheet("招聘信息",0)
    # 向表格中添加一行数据
    # 参数是一个list
    sheet.append(["职位名","公司名","工作地点","薪资","发布时间"])
    # 写入数据
    for item in result:
        sheet.append([item['job'],item['company'],item['address'],item['salary'],item['publishDate']])

    # 将工作簿保存到本地文件系统
    wb.save("export.xlsx")



# code = do_spider()
code = load_html()
# print(code)
result = parse_html(code)
# print(result)
# export_to_mysql(result)
# export_to_redis(result)
# read_from_redis()
export_to_excel(result)
print("success..................")


# 完善代码，实现每4秒抓取一个页面。抓取前5页
# 将数据导出

