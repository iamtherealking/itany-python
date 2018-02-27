# 爬取图片 以及 JSON 的处理

from urllib import request,parse
import json


def img_spider():
    url = "http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?{}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"
    }

    page_no = 0
    while True:
        params = {
            "category": "壁纸",
            "tag": "全部",
            "start": page_no * 50,
            "len": 50,
            "width": 1024,
            "height": 768
        }
        params = parse.urlencode(params)
        # print(params)
        req = request.Request(url.format(params), headers=headers)
        json_code = request.urlopen(req).read().decode("GBK")
        # print(json_code)
        json_obj = json.loads(json_code)
        print("正在爬取第{}到第{}张图片".format(json_obj['startIndex'], json_obj['startIndex'] + 50))
        if len(json_obj['all_items']) <= 0:
            break
        for item in json_obj['all_items']:
            pic_url = item['pic_url']
            name = pic_url[pic_url.rindex("/") + 1:]
            # print(name)
            ori_pic_url = item['ori_pic_url']
            suffiex = ori_pic_url[ori_pic_url.rindex(".") + 1:]
            # print(name,suffiex,sep="")
            print(pic_url)
            try:
                request.urlretrieve(pic_url, "images/{}.{}".format(name, suffiex))
            except Exception as e:
                print(e)
                continue

        page_no += 1


img_spider()
