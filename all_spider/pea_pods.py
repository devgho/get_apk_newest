#!bin/python
#encoding:utf-8

import requests
from lxml import etree  
import sys,os
sys.path.append(".")
from dl import download

def check(path="dldl_9you/",serial="8130690"):
    fullpath = "apks/"+path
    resp = requests.get("https://www.wandoujia.com/apps/"+serial)
    _element = etree.HTML(resp.text)
    try:
        version =  str(_element.xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/dl/dd[3]/text()")[0]).replace(u"\xa0",u"")
        url = _element.xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[3]/a[1]/@href")[0]
        download(url, version+".apk", fullpath)
    except IndexError:
        check(path,serial)
    

def main():
    check("sgz_9you/",serial="7956134")

if __name__ == "__main__":
    main()