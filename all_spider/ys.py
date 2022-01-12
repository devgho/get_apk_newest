#!bin/python
#encoding:utf-8

import os
import re
import requests
import sys
sys.path.append(".")
from dl import download

def check(path="apks/ys/"):
    url = "https://ys.mihoyo.com/main/m"
    resp = requests.get(url)
    resp.encoding="utf8"
    result = re.search(r"version:\"(?P<v>.*?)\"", resp.text).group("v")
    version = re.search(r"[\d\.]+",result).group()
    filename = version+".apk"
    if not os.path.exists(filename):
        download("https://ys-api.mihoyo.com/event/download_porter/link/ys_cn/official/android_default",filename,path)


def main():
    check()

if __name__ == "__main__":
    main()