#!bin/python
#encoding:utf-8

import requests
from lxml import etree
import os,sys,re,json
from platform import system

from requests.api import request
from shutil import copyfile


def download(url,filename,path):
    if not os.path.exists(path):
        os.mkdir(path)  
    filepath = path+filename
    if os.path.exists(filepath):
        return
    D = Downloader(url,filepath)
    D.start()
    try:
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
        jym_path = "/home/data/jymdata/apks/"
        with open(jym_path+name+".json","w",encoding="utf8") as f:
            f.write(info_json)
        copyfile(filepath,jym_path+last_filename)
    except:
        os.remove(filepath)
        download(url,filename,path)
    
    
    

class Downloader(object):
    def __init__(self, url, file_path):
        self.url = url
        self.file_path = file_path
 
    def start(self):
        res_length = requests.get(self.url, stream=True)
        total_size = int(res_length.headers['Content-Length'])
        print(res_length.headers)
        print(res_length)
        if os.path.exists(self.file_path):
            temp_size = os.path.getsize(self.file_path)
            print("当前：%d 字节， 总：%d 字节， 已下载：%2.2f%% " % (temp_size, total_size, 100 * temp_size / total_size))
        else:
            temp_size = 0
            print("总：%d 字节，开始下载..." % (total_size,))
 
        headers = {'Range': 'bytes=%d-' % temp_size,
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}
        res_left = requests.get(self.url, stream=True, headers=headers)
 
        with open(self.file_path, "ab") as f:
            for chunk in res_left.iter_content(chunk_size=1024):
                temp_size += len(chunk)
                f.write(chunk)
                f.flush()

                # done = int(50 * temp_size / total_size)
                # sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))       #百分比显示下载进度，进度条每2%多一个█
                # sys.stdout.flush()  



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