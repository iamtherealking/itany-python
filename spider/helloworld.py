
# 从urllib模块中导入request子模块
from urllib import request


url = "http://www.baidu.com/"

req = request.Request(url)

html_code = request.urlopen(req).read()

html_text = str(html_code, "utf-8")

target = open("baidu.html", mode="w", encoding="utf-8")

target.write(html_text)

print("over...............")