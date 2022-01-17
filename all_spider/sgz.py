#!bin/python
#encoding:utf-8
import requests
import os,sys,re
sys.path.append(".")
from dl import download

# url = "https://sgzzlb.lingxigames.com/m"
# resp = requests.get(url)
# page = BeautifulSoup(resp.text,'lxml')
# dl_link = page.find('a',{
#     "class":"btn-an",
#     "title":"安卓下载"
# })['href']
# print(dl_link)
# with open("dl.html", "w", encoding="utf8") as p:
#     p.write(page.prettify())

def check(path="sgz/"):
    path = "apks/"+path
    url = "https://cdn-cn.lingxigames.com/prism-sgzzlb/1.0.0/test/static/js/fabm.620a04ba.js"
    headers = {
        "Referer": "https://sgzzlb.lingxigames.com/",
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '1',
        'sec-ch-ua-platform': '"Android"',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36 Edg/97.0.1072.55'
    }
    resp = requests.get(url,headers=headers)
    dl_link = re.search(r'Android"==i\.platformName&&g\(\)\("\.bottom_dl,\.download,\.btn-download"\)\.attr\("href","(?P<link>.*?)"\)',resp.text).group("link")

    # dl_link = re.search("link:\"(?P<link>https://.*?)\"",resp.text).group('link')

    file_name = re.search(r"(?P<u>.*/)(?P<filename>.*)", dl_link).group("filename")+".apk"
    download(dl_link,file_name,path)

def main():
    check()

if __name__ == "__main__":
    check()