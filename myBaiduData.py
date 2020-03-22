# -*- coding: utf-8 -*-

__author__ = 'wangli'
__date__ = '2020-03-08 19:47'


# 爬取百度热搜数据 http://npm.taobao.org/mirrors/chromedriver/
from selenium.webdriver import Chrome, ChromeOptions
import time, traceback
from myTencentData import get_conn, close_conn


def get_baidu_hot():
    """

    :return: 百度疫情热搜
    """
    option = ChromeOptions()
    option.add_argument("--headless") # 隐藏浏览器
    option.add_argument("--no-sandbox")

    url = "https://voice.baidu.com/act/virussearch/virussearch?from=osari_map&tab=0&infomore=1"

    browser = Chrome(options=option)
    browser.get(url)
    # print(browser.page_source)
    but = browser.find_element_by_css_selector('#ptab-0 > div > div.VirusHot_1-5-4_32AY4F.VirusHot_1-5-4_2RnRvg > section > div')
    # 点击展开
    but.click()
    # 等待3s
    time.sleep(3)

    c = browser.find_elements_by_xpath('//*[@id="ptab-0"]/div/div[2]/section/a/div/span[2]')
    context = [i.text for i in c]
    # for i in c:
    #     print(i.text)

    # browser.close()
    return context

def update_hotsearch():
    """
    将疫情热搜数据插入数据库
    :return:
    """
    cursor = None
    conn = None
    try:
        context = get_baidu_hot()
        print(f"{time.asctime()}开始更新热搜数据")
        conn, cursor = get_conn()
        sql = "insert into hotsearch(dt, content) values(%s,%s)"
        ts = time.strftime("%Y-%m-%d %X")
        for i in context:
            cursor.execute(sql, (ts, i)) # 插入数据
        conn.commit()
        print(f"{time.asctime()}更新热搜数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)

update_hotsearch()
