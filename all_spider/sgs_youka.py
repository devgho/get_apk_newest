#!bin/python
#encoding:utf-8

import requests
import re
import os,sys
sys.path.append(".")
from dl import download


def check(path="sgs_youka/"):
    path = os.path.join("apks/",path)
    url = "https://www.sanguosha.cn/"
    resp = requests.get(url,timeout=500)
    url = re.search(r"http.*?apk",resp.text).group()
    filename = re.search(r".*/(?P<v>.*)",url).group('v')
    download(url,filename,path)

def main():
    check()

if __name__ == "__main__":
    main()
