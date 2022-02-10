#!bin/python
#encoding:utf-8

import sys
import os
sys.path.append(".")    #可以用os.get_cwd()看一下工作路劲再append
import requests
import re
from dl import download
from ninegame import check as ninegame


def check(path="dldl_37/"):
    path = os.path.join("apks/",path)
    resp = requests.get("https://mg-api.37.com.cn/website/articlelist/51/46?webId=51&categoryId=46&pageSize=999").json()
    filename = re.search(r"point.*?版本.*?(?P<version>[\d\.]+).*?</div>",requests.get("https://a.9game.cn/dldlhsdj/").text,re.S).group("version")
    url = resp['data']['array'][0]['ext6']
    ninegame("dldlhsdj", filename)
    download(url,filename,path)
    

def main():
    check()

if __name__ == "__main__":
    main()
    