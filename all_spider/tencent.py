#!bin/python
#encoding:utf-8
import requests
import re
import os,sys
sys.path.append(".")
from dl import download


def check(path="hpjy/",url="https://95f694c353ade32847c5f5e5f3139de2.dlied1.cdntips.net/godlied4.myapp.com/myapp/6337/cos.static-77964/1106467070.js?mkey=61ce8403def462cc&f=0000&time=1592375172&cip=222.244.68.57&proto=https&access_type="):
    path = "apks/"+path
    res = requests.get(url)
    res.encoding = "gbk"
    all = res.text
    url = re.search("https://dlied4.myapp.com/myapp/.*?apk",all).group()
    filename = re.search(r"(?P<u>.*/)(?P<filename>.*?apk)",url).group("filename")
    download(url,filename,path)

def main():
    check()

if __name__ == "__main__":
    main()