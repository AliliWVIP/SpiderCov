# -*- coding: utf-8 -*-

__author__ = 'wangli'
__date__ = '2020-03-06 21:18'

import requests
import json
import time
import pymysql
import traceback

def get_tencent_data():
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    url_other = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other"

    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) \
                            AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    }



    r = requests.get(url, headers)
    res = json.loads(r.text)
    data_all = json.loads(res['data'])

    r_other = requests.get(url_other, headers)
    res_other = json.loads(r_other.text)
    data_all_other = json.loads(res_other['data'])

    # 历史数据
    history = {}
    for i in data_all_other['chinaDayList']:
        ds = "2020." + i['date']
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)
        confirm = i["confirm"]
        suspect = i['suspect']
        heal = i["heal"]
        dead = i["dead"]
        history[ds] = {"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead}

    for i in data_all_other['chinaDayAddList']:
        ds = "2020." + i['date']
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)
        confirm = i["confirm"]
        suspect = i['suspect']
        heal = i["heal"]
        dead = i["dead"]
        history[ds].update({"confirm_add": confirm, "suspect_add": suspect, "heal_add": heal, "dead_add": dead})

    # print(data_all)

    # 当日详细数据
    details = []
    update_time = data_all["lastUpdateTime"]
    # list 各个国家的数据
    data_country = data_all["areaTree"]
    # 中国各省数据
    data_province = data_country[0]["children"]
    for pro_infos in data_province:
        # 省名
        province = pro_infos["name"]
        for city_infos in pro_infos["children"]:
            city = city_infos["name"]
            confirm = city_infos["total"]["confirm"]
            confirm_add = city_infos["today"]["confirm"]
            heal = city_infos["total"]["heal"]
            dead = city_infos["total"]["dead"]
            details.append([update_time, province, city, confirm, confirm_add, heal, dead])

    # print(details)

    return history, details

def get_conn():
    """

    :return: 连接，游标
    """
    # 建立连接
    conn = pymysql.connect(host='127.0.0.1',
                           user='root',
                           password='qweasd',
                           db='cov2019')

    # 创建游标，默认是元组形
    cursor = conn.cursor()
    return conn, cursor

def close_conn(conn, cursor):
    if cursor:
        cursor.close()

    if conn:
        conn.close()

def update_details():
    """
    更新details表
    :return:
    """
    cursor = None
    conn = None
    try:
        li = get_tencent_data()[1] # 0是历史数据字典 1是最新详细数据列表
        conn, cursor = get_conn()
        sql = "insert into details(update_time, province, city, confirm, confirm_add, heal, dead) " \
              "values(%s, %s, %s, %s, %s, %s, %s)"
        # 对比当前最大时间戳
        sql_query = 'select %s=(select update_time from details order by id desc limit 1)'
        cursor.execute(sql_query, li[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始更新最新数据")
            for item in li:
                cursor.execute(sql, item)
            # 提交事务 update delete insert 操作
            conn.commit()
            print(f"{time.asctime()}更新最新数据完毕")
        else:
            print(f"{time.asctime()}已是最新数据")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def insert_history():
    """
    插入历史数据
    :return:
    """
    cursor = None
    conn = None
    try:
        dic = get_tencent_data()[0] # 0是历史数据字典 1是最新详细数据列表
        print(f"{time.asctime()}开始插入历史数据")
        conn, cursor = get_conn()
        sql = "insert into history values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        for k, v in dic.items():
            cursor.execute(sql, [k, v.get("confirm"), v.get("confirm_add"), v.get('suspect'), v.get("suspect_add"),
                                 v.get("heal"), v.get("heal_add"), v.get("dead"), v.get("dead_add")])
        conn.commit()
        print(f"{time.asctime()}插入历史数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def update_history():
    """
    插入历史数据
    :return:
    """
    cursor = None
    conn = None
    try:
        dic = get_tencent_data()[0] # 0是历史数据字典 1是最新详细数据列表
        print(f"{time.asctime()}开始插入历史数据")
        conn, cursor = get_conn()
        sql = "insert into history values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        sql_query = "select confirm from history where ds=%s"
        for k, v in dic.items():
            if not cursor.execute(sql_query, k):
                cursor.execute(sql, [k, v.get("confirm"), v.get("confirm_add"), v.get('suspect'), v.get("suspect_add"),
                                 v.get("heal"), v.get("heal_add"), v.get("dead"), v.get("dead_add")])
        conn.commit()
        print(f"{time.asctime()}插入历史数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


# insert_history()
# update_details()


# sql = "select * from history"
# cursor.execute(sql)
# res = cursor.fetchall()
# print(res)



# sql = 'insert into history values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
# cursor.execute(sql, [time.strftime("%Y-%m-%d"), 10, 1, 2, 3, 4, 5, 6, 7])
# # 提交事务
# conn.commit()


# cursor.close()
# conn.close()


# res = requests.get(url)
# print(res.text)
# d = json.loads(res.text)
# print(d["data"])
# data_all = json.loads(d["data"])
# print(type(data_all))
# print(data_all.keys())
# print(data_all["lastUpdateTime"])
# print(data_all["chinaTotal"])pip
# print(data_all["chinaAdd"])
# print(data_all["chinaDayList"])
# print(data_all["chinaDayAddList"])
# print(data_all["areaTree"])
# print(len(data_all["areaTree"]))
# print(data_all["areaTree"][0].keys())
#
# for i in data_all["areaTree"][0]["children"]:
#     print(i["name"])



