# encoding=utf8
# 前程无忧 爬虫
__author__ = "崔译"

# 发送http、https请求
from urllib import request


# 用于解析处理HTML格式的字符串
from bs4 import BeautifulSoup

# 用于Excel读写操作
from openpyxl import Workbook

import requests


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


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").content


def do_spider(page_no=1):
    # req = request.Request(url.format(page_no), headers=headers)

    # 创建一个代理
    proxy = request.ProxyHandler({
        "sock5":get_proxy()
    })
    # 创建
    opener = request.build_opener(proxy)
    # 注册opener
    request.install_opener(opener)

    html_bytes = request.urlopen(url.format(page_no)).read()
    html_code = str(html_bytes, "gbk")
    print("爬取到第{}页数据".format(page_no))
    return html_code



# 解析html
def parse_html():
    result_list = []
    page_no = 1
    while True:
        html = do_spider(page_no)
        soup = BeautifulSoup(html, "html.parser")

        content_div = soup.select("#resultList")[0]
        item_divs = content_div.select(".el")
        if len(item_divs) <= 1:
            break
        for item_div_index in range(1,len(item_divs)):
            item_div = item_divs[item_div_index]
            spans = item_div.find_all("span")
            result_item = {
                "job": spans[0].get_text().strip(),
                "company": spans[1].get_text().strip(),
                "address": spans[2].get_text().strip(),
                "salary": spans[3].get_text().strip(),
                "publishDate": spans[4].get_text().strip()
            }
            result_list.append(result_item)
        page_no += 1
    return result_list


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
# export_to_excel(result)
# print("success..................")


result = parse_html()
export_to_excel(result)
