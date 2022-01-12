#!bin/python
#encoding:utf-8

import os
from all_spider.pea_pods import check as peapods
from all_spider.dldl_37 import check as dldl_37
from all_spider.ys import check as ys
from all_spider.sgs_youka import check as sgs_youka
from all_spider.tencent import check as tencent
from all_spider.sgz import check as sgz


def main():
    if not os.path.exists("apks"):
        os.mkdir("apks")
    peapods("apks/dldl_9you/","8130690")        #斗罗大陆九游
    peapods("apks/sgs_9you/","6561883")         #三国杀九游
    dldl_37()
    sgs_youka()
    ys()
    tencent()       #和平精英
    tencent("apks/wangzhe/", "https://696214c97ffe3b0032745108cb06ef60.dlied1.cdntips.net/godlied4.myapp.com/myapp/6337/cos.static-77964/1104466820.js?mkey=61ce95bcdef462cc&f=0ae6&time=1596093184&cip=222.244.68.57&proto=https&access_type=") #王者荣耀
    sgz()
    
    

if __name__ == "__main__":
    main()