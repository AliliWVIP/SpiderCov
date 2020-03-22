# -*- coding: utf-8 -*-

__author__ = 'wangli'
__date__ = '2020-03-05 10:00'

import requests

# url = 'http://www.baidu.com'
#
# resp = requests.get(url)
# print(resp.encoding)
# print(resp.status_code)
# html = resp.text
# print(html)
# resp.encoding = 'utf-8'
# html = resp.text
# print(html)


url2 = 'http://www.dianping.com'
header = {
    "Host": "www.dianping.com",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) \
                        AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

resp2 = requests.get(url2, headers=header)
print(resp2.encoding)
print(resp2.status_code)
resp2.encoding = 'utf-8'
print(resp2.text)