# -*- coding: utf-8 -*-

__author__ = 'wangli'
__date__ = '2020-03-06 21:00'

import re

text = "新增确定病历15例,新增出院病历20例"

# .*后边的问号叫非贪心模式
pattern = '新增确定病历(\d+).*?出院病历(\d+)'

res = re.search(pattern, text)
print(res)
# groups = res.groups()
print(res.groups())
print(res.group(0))
print(res.group(1))
print(res.group(2))
