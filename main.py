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
    tencent_games = [
        ["wangzhe/", "6648837"],
        ["hpjy/", "7701857"]
    ]
    if not os.path.exists("apks"):
        os.mkdir("apks")
    for i in tencent_games:
        peapods(i[0],i[1])
    dldl_37()
    ys()
    sgs_youka()
    sgz()

if __name__ == "__main__":
    main()