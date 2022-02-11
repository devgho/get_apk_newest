import requests 
import json

j1 = json.loads(requests.get("https://api-takumi.mihoyo.com/event/download_porter/link/bh3_cn/bh3/android_official").json)