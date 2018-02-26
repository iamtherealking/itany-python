# encoding=utf8
# 前程无忧 爬虫
__author__ = "崔译"

# 发送http、https请求
from urllib import request

# 用于解析处理HTML格式的字符串
from bs4 import BeautifulSoup

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


def do_spider():
    page_no = 1
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
    # page_no += 1

    # file = open("template.html",mode="w",encoding="gbk")
    # file.write(html_code)
    return html_code


def load_html():
    file = open("template.html",encoding="gbk")
    html_code = file.read()
    return html_code;


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


    # text = soup.select("#area_channel_layer .tle")[0].get_text()
    # print(str(text).strip())
    pass


# code = do_spider()
code = load_html()
# print(code)
parse_html(code)

