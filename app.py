from flask import Flask, render_template, jsonify
from jieba.analyse import extract_tags
import utils
import string


app = Flask(__name__)

#
# @app.route("/abc")
# def hello_1():

@app.route('/ajax', methods=["POST"])
def postAjax():
    return "1000"

@app.route("/time")
def get_time():
    return utils.get_time()

@app.route("/c1")
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({"confirm": str(data[0]), "suspect": str(data[1]), "heal": str(data[2]), "dead": str(data[3])})

@app.route("/c2")
def get_c2_data():
    res = []
    for tup in utils.get_c2_data():
        print(tup)
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})

@app.route("/l1")
def get_l1_data():
    data = utils.get_l1_data()
    day, confirm, suspect, heal, dead = [], [], [], [], []
    for a, b, c, d, e in data[7:]:
        # a是datetime类型
        day.append(a.strftime("%m-%d"))
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({"day": day, "confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead})

@app.route("/l2")
def get_l2_data():
    data = utils.get_l2_data()
    day, confirm_add, suspect_add = [], [], []
    for a, b, c in data[7:]:
        # a是datetime类型
        day.append(a.strftime("%m-%d"))
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({"day": day, "confirm_add": confirm_add, "suspect_add": suspect_add})

@app.route("/r1")
def get_r1_data():
    data = utils.get_r1_data()
    city, confirm = [], []
    for a, b in data:
        # a是datetime类型
        city.append(a)
        confirm.append(str(b))
    return jsonify({"city": city, "confirm": confirm})

@app.route("/r2")
def get_r2_data():
    data = utils.get_r2_data()
    d = []
    for a in data:
        k = a[0].rstrip(string.digits)
        v = a[0][len(k):]
        ks = extract_tags(k)
        for j in ks:
            if not j.isdigit():
                d.append({"name": j, "value": v})
    return jsonify({"kws": d})


@app.route('/')
def hello_world():
    return render_template('main.html')
    # url = "http://www.baidu.com"
    # res = request.urlopen(url)  #获取响应
    #
    # print(res.info())   #响应头
    # print(res.getcode())  #状态吗
    # print(res.geturl()) #返回响应地址

    # 解码

    # html = res.read().decode('utf-8')
    # print(html)


    # url = "http://www.dianping.com"
    # header = {
    #     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) \
    #                     AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    # }
    # req = request.Request(url, headers=header)
    # res = request.urlopen(req)
    # print(res.info())
    # print(res.getcode())
    # return 'Hello World!'

#
if __name__ == '__main__':
    app.run()
