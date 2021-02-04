

import requests as rq
from bs4 import BeautifulSoup
import io
import time
import pandas as pd

pd.describe.options() 
  
def sleeptime(hour, min, sec):
    return hour*3600 + min*60 + sec


tStart = time.time()  # 計時開始
fp = io.open("marryData-List.txt", "ab+")
i = 1
while (i <= 33):
    nextlink = "https://www.marry.com.tw/venue-shop-kwbt2004mmir0mmpg" + \
        str(i)+"mm"
    nl_response = rq.get(nextlink)  # 用 requests 的 get 方法把網頁抓下來
    soup = BeautifulSoup(nl_response.text, "lxml")  # 指定 lxml 作為解析器
    for url in soup.findAll('a', {'class': 'shop_name'}):
        response = rq.get(url.get('href'))  # 用 requests 的 get 方法把網頁抓下來
        html_doc = response.text  # text 屬性就是 html 檔案
        soup = BeautifulSoup(response.text, "lxml")  # 指定 lxml 作為解析器
        if soup.select('h1') != []:
            company = soup.select('h1')[0].find('a').text
            # 判斷是否有H1
            if company != '':
                # 服務內容(有打勾)
                pid = soup.findAll('li', {'class': 'icon-check'})
                Con = ",".join([p.text.strip() for p in pid])
                # 地址
                address = soup.findAll('ul', {'class': 'contacts_list'})[
                    0].find('span', {'class': 'contacts_info'}).text
                fp.write(company.encode('utf-8') + '='.encode('utf-8'))
                fp.write(Con.encode('utf-8') + '?'.encode('utf-8') +
                         address.encode('utf-8') + '\n'.encode('utf-8'))
                time.sleep(sleeptime(0, 1, 0))
    i = i + 1
tEnd = time.time()  # 計時結束
fp.close()
print("It cost %f sec" % (tEnd - tStart))  # 會自動做近位

help(io)


