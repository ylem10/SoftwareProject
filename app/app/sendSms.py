from __init__ import app
import urllib.request, sys
from flask import Flask, request, json, session, render_template, make_response
import random, socket

app.config['SECRET_KEY'] = '123456'


# 生成验证码
def SmsCode():
    code = random.randint(1000, 10000)
    session["SmsCode"] = code
    return code


@app.route('/SendSms', methods=['POST'])
def senSms():
    # 先把验证码存入cookie
    code = str(SmsCode())
    # session["Sms"] = code
    resp = make_response()
    resp.set_cookie('sms', code)  # 设置cookies
    print(code)
    # 前台的手机号
    data = json.loads(request.form.get('data'))
    phone = data['cellphone']
    host = 'http://yzx.market.alicloudapi.com'
    path = '/yzx/sendSms'
    method = 'POST'
    appcode = 'e257c68887304c4d8e1bba01b5453885'
    querys = urllib.parse.urlencode({
        "mobile": phone,
        "param": "code:" + code,
        "tpl_id": "TP1710262"
    }).encode('utf-8')
    bodys = {}
    url = host + path
    req = urllib.request.Request(url, querys, method=method)
    req.add_header('Authorization', 'APPCODE ' + appcode)
    response = urllib.request.urlopen(req)
    content = response.read()
    if (content):
        print(content)
    return resp