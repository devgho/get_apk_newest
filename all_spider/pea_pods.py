#!bin/python
#encoding:utf-8

import requests
from lxml import etree  
import sys,os
sys.path.append(".")
from dl import download

def check(path="dldl_9you/",serial="8130690"):
    fullpath = os.path.join("apks/",path)
    resp = requests.get("https://www.wandoujia.com/apps/"+serial, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50"})
    _element = etree.HTML(resp.text)
    try:
        print(resp.text)
        version =  str(_element.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/dl/dt[contains(text(),"版本")]/following-sibling::dd[1]/text()')[0]).replace(u"\xa0",u"")
        url = _element.xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[3]/a[1]/@href")[0]
        download(url, version+".apk", fullpath)
    except IndexError:
        check(path,serial)
    

def main():
    check("wzry/",serial="6648837")

if __name__ == "__main__":
    main()