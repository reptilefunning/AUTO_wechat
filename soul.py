import requests
from lxml import etree
import re
import random


def Soul():
    url = 'http://www.59xihuan.cn/'
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"}
    res = requests.get(url, headers=headers).content
    html = etree.HTML(res)
    soul_sen = html.xpath("//div[@class='mLeft']")
    soul_dict = {}
    for soul_s in soul_sen:
        soul_dict[1] = soul_s.xpath('./div[1]/div[2]/div[2]/text()')[0].strip()
        soul_dict[2] = soul_s.xpath('./div[2]/div[2]/div[2]/text()')[0].strip()
        soul_dict[3] = soul_s.xpath('./div[3]/div[2]/div[2]/text()')[0].strip()
        soul_dict[4] = soul_s.xpath('./div[4]/div[2]/div[2]/text()')[0].strip()
        soul_dict[5] = soul_s.xpath('./div[5]/div[2]/div[2]/text()')[0].strip()
        soul_dict[6] = soul_s.xpath('./div[6]/div[2]/div[2]/text()')[0].strip()
        soul_dict[7] = soul_s.xpath('./div[7]/div[2]/div[2]/text()')[0].strip()
        soul_dict[8] = soul_s.xpath('./div[8]/div[2]/div[2]/text()')[0].strip()
        soul_dict[9] = soul_s.xpath('./div[9]/div[2]/div[2]/text()')[0].strip()
        soul_dict[10] = soul_s.xpath('./div[10]/div[2]/div[2]/text()')[0].strip()
    i = random.randint(1,10)
    return soul_dict[i]
if __name__ == "__main__":
    Soul()

