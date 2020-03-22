# -*- coding: utf-8 -*-

__author__ = 'wangli'
__date__ = '2020-03-06 20:46'

from bs4 import BeautifulSoup
import requests

url = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd/fyzt.shtml"

res = requests.get(url)
res.encoding = "utf-8"
html = res.text
# print(html)
soup = BeautifulSoup(html)
title = soup.find("h2").text
print(title)
a = soup.find("a").attrs
print(a['href'])

new_url = "http://wsjkw.sc.gov.cn" + a['href']
new_res = requests.get(new_url)
new_res.encoding = 'utf-8'
# print(new_res.text)
new_soup = BeautifulSoup(new_res.text)
print(new_soup.find('p'))