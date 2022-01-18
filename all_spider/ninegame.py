from fileinput import filename
import requests
import re,sys,os
sys.path.append(".")
from dl import download


def check(game):
    path = os.path.join("apks/",game)
    url = "https://www.9game.cn/"+game
    resp = requests.get(url)
    gameid = re.search(r'data-gameid="(?P<id>.*?)"',resp.text).group("id")
    filename = re.search(r'<span class="ngame-update">更新时间：(?P<datetime>.*?) </span>',resp.text).group("datetime")
    dlink = f"https://www.9game.cn/game/downs_{gameid}_2.html"
    download(dlink,filename,path)


def main():
    check("sgzzlb")


if __name__ == "__main__":
    main()