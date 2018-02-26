# Python爬虫

## 主讲：崔译

## 一、爬虫是什么

> 是一段代码，用于获取网页上的信息
>
> 几乎所有主流的高级程序设计语言都能实现爬虫

## 二、爬虫的实现原理

**通过代码 模拟浏览器向服务器发送Http/Https/...请求**

**（服务器是无法判断请求来源的），然后对响应的HTML页面进行数据处理**

- 请求的发送
- 响应数据的处理
- 效率优化

## 三、HelloWorld

### 1、导入对应模块

> java: class 文件是由 JVM  解释，运行的
>
> ​	 JVM（JRE） 存在于 JDK   中
>
> python: py文件  是由  Python解释器（interpreter）解释运行
>
> ​		Python的模块 是由 解释器中的pip模块安装的

- urllib 模块

### 2、编写Python代码

```python
# 从urllib模块中导入request子模块
from urllib import request

url = "http://www.baidu.com/"

req = request.Request(url)

html_code = request.urlopen(req).read()

html_text = str(html_code, "utf-8")

target = open("baidu.html", mode="w", encoding="utf-8")

target.write(html_text)

print("over...............")
```

## 四、一个完整的爬虫



