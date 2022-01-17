#!bin/python
#encoding:utf-8

import os
from threading import Thread
from all_spider.pea_pods import check as peapods
from all_spider.dldl_37 import check as dldl_37
from all_spider.ys import check as ys
from all_spider.sgs_youka import check as sgs_youka
from all_spider.tencent import check as tencent
from all_spider.sgz import check as sgz


def Multithreading(target,args=""):
    thread = Thread(target=target,args=args)
    thread.start()

def main():
    peapods_games = [
        ["dldl_9you/","8130690"],
        ["sgs_9you/","6561883"]
    ]
    tencent_games = [
        ["wangzhe/", "https://696214c97ffe3b0032745108cb06ef60.dlied1.cdntips.net/godlied4.myapp.com/myapp/6337/cos.static-77964/1104466820.js?mkey=61ce95bcdef462cc&f=0ae6&time=1596093184&cip=222.244.68.57&proto=https&access_type="],
        ["hpjy/", "https://696214c97ffe3b0032745108cb06ef60.dlied1.cdntips.net/godlied4.myapp.com/myapp/6337/cos.static-77964/1104466820.js?mkey=61ce95bcdef462cc&f=0ae6&time=1596093184&cip=222.244.68.57&proto=https&access_type="]
    ]
    if not os.path.exists("apks"):
        os.mkdir("apks")
    for i in peapods_games:
        Multithreading(peapods,i)
    for i in tencent_games:
        Multithreading(tencent,i)
    Multithreading(dldl_37)
    Multithreading(ys)
    Multithreading(sgs_youka)
    Multithreading(sgz)
    

if __name__ == "__main__":
    main()