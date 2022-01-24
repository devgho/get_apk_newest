from fileinput import filename
import requests
import re,sys,os
sys.path.append(".")
from dl import download


def check(game,filename):
    path = os.path.join("apks/",game)
    url = "https://www.9game.cn/"+game
    resp = requests.get(url)
    gameid = re.search(r'data-gameid="(?P<id>.*?)"',resp.text).group("id")
    dlink = f"https://www.9game.cn/game/downs_{gameid}_2.html"      #爬九游的版本号https://a.9game.cn/sgs/,现在暂时是官网更了九游就一起爬
    download(dlink,filename,path)


def main():
    check("dldlhsdj","dldlhsdj.apk")


if __name__ == "__main__":
    main()