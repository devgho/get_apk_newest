#!bin/python
#encoding:utf-8

import requests
from lxml import etree
import sys,os
sys.path.append(".")
from dl import download

def check(path="apks/dldl_9you/",serial="8130690"):
    resp = requests.get("https://www.wandoujia.com/apps/"+serial)
    _element = etree.HTML(resp.text)
    version =  str(_element.xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/dl/dd[3]/text()")[0]).replace(u"\xa0",u"")
    if not os.path.exists(path+version+".apk"):
        url = _element.xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[3]/a[1]/@href")[0] #没找到与页面中版本匹配的包的话就爬
        download(url, version+".apk", path)

def main():
    check("apks/sgs_9you/",serial="6561883")

if __name__ == "__main__":
    main()