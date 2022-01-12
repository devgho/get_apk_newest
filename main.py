import os
from all_spider.pea_pods import check as peapods
from all_spider.dldl_37 import check as dldl_37
from all_spider.ys import check as ys
from all_spider.sgs_youka import check as sgs_youka


def main():
    if not os.path.exists("apks"):
        os.mkdir("apks")
    peapods("apks/dldl_9you/","8130690")        #斗罗大陆九游
    peapods("apks/sgs_9you/","6561883")         #三国杀九游
    dldl_37()
    sgs_youka()
    ys()
    
    

if __name__ == "__main__":
    main()