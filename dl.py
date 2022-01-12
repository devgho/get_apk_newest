#!bin/python
#encoding:utf-8

import requests
from lxml import etree
import os
import re
import json
from platform import system


def download(url,filename,path):
    if not os.path.exists(path):
        os.mkdir(path)
    with open(path+filename, "wb") as f:
        f.write(requests.get(url).content)
    package = os.popen("aapt dump badging "+path+filename+("|findstr " if system()=="Windows" else "|grep ")+"package").read()
    name = re.search(r"name='(?P<v>.*?)'",package,re.I).group("v")
    version_code = re.search(r"versioncode='(?P<v>.*?)'",package,re.I).group("v")
    version_name = re.search(r"versionname='(?P<v>.*?)'",package,re.I).group("v")
    last_filename = f'{name}_{version_code}.apk'
    info = {
        "version_code":version_code,
        "version_name":version_name,
        "last_filename":last_filename
    }
    info_json = json.dumps(info)
    with open(path+"/"+name+".json","w",encoding="utf8") as f:
        f.write(info_json)
    

def main():
    resp = requests.get("https://www.wandoujia.com/apps/8130690")
    _element = etree.HTML(resp.text)
    version =  str(_element.xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/dl/dd[3]/text()")[0]).replace(u"\xa0",u"")
    version="2.3.1"
    if os.path.exists(version+".apk"):
        pass
    else:
        url = _element.xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[3]/a[1]/@href")[0] #没找到与页面中版本匹配的包的话就爬
        download(url, version+".apk","apks/dldl_9you/")

if __name__ == "__main__":
    main()