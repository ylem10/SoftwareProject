from flask import render_template, request, session, jsonify
from __init__ import app
import json, model.user.User


@app.route('/')
def index():
    sms_phone = request.args.get('phone')
    # 短信验证登录
    if sms_phone != None:
        username = model.user.User.getUsernaemByphone(sms_phone)
        session['username'] = username
        return render_template("index.html", username=username)
    # 判断用户名是否在 session中
    if 'username' in session:
        username2 = session['username']
    else:
        username2 = ""
    print(str(sms_phone) + "--------")
    if sms_phone != None or username2 != "":
        if sms_phone != None:
            username = model.user.User.getUsernaemByphone(sms_phone)
            if username != "":
                return render_template("index.html", username=username)
            else:
                print("出错")
        else:
            username = username2
            return render_template("index.html", username=username)
    else:
        return render_template("index.html")


@app.route("/user/login")
def gotoLogin():
    return render_template("webpages/user/login.html")


@app.route("/user/SmsLogin")
def gotoSmsLogin():
    return render_template("webpages/user/SmsLogin.html")


@app.route("/user/checkSmsCode", methods=['POST'])
def checkSmsCode():
    # 前端获取到验证码
    data = json.loads(request.form.get('data'))
    SmsCode = data['SmsCode']
    print(SmsCode)
    # session中验证码获取到
    # SmsCode2 = session['Sms']
    SmsCode2 = request.cookies.get('sms', None)
    if SmsCode2 == SmsCode:
        print("相等")
        return jsonify({'ok': True})
    else:
        print("不相等")
        return jsonify({'ok': False})


@app.route("/user/register")
def register():
    return render_template("webpages/user/register.html")


@app.route("/user/forgetPwd")
def forgetPwd():
    return render_template("webpages/user/forgetPwd.html")


@app.route("/user/modifyPwd")
def modifyPwd():
    return render_template("webpages/user/modifyPwd.html")


@app.route('/user/register', methods=['POST'])
def userRegister():
    data = json.loads(request.form.get('data'))
    username = data['username']
    phone = data['phone']
    password = data['password']
    print(password)
    infoInsert = model.user.User.userRegister(username, password, phone)
    if infoInsert:
        return jsonify({'ok': True})
    else:
        return jsonify({'ok': False})


@app.route('/user/loginCheck', methods=['POST'])
def userloginCheck():
    data = json.loads(request.form.get('data'))
    username = data['username']
    password = data['password']
    identifyCode1 = data['validCode']
    identifyCode2 = session['validCode']
    # print(username+':'+password+':'+identifyCode1+':'+identifyCode2)
    info_exist = model.user.User.user_login(username, password)
    if info_exist and identifyCode1 == identifyCode2:
        print('exist')
        return jsonify({'ok': True})
    elif identifyCode1 != identifyCode2:
        print('验证码输入错误')
        return jsonify({'ok': 'validError'})
    else:
        print("密码错误！")
        return jsonify({'ok': 'pwdError'})


@app.route('/user/modifyPwd2', methods=['POST'])
def modifyPassword():
    data = json.loads(request.form.get('data'))
    new_password = data['new_password']
    phone = data['phone']
    print(new_password)
    print(phone)
    infoUpdate = model.user.User.modifyPasswordByPhone(phone, new_password)
    if infoUpdate:
        return jsonify({'ok': True})
    else:
        return jsonify({'ok': False})


@app.route('/user/checkUsernameExist', methods=['POST'])
def checkNameExist():
    data = json.loads(request.form.get('data'))
    username = data['username']
    if model.user.User.checkUsername(username):
        return jsonify({'ok': True})
    else:
        return jsonify({'ok': False})


@app.route('/user/info')
def gotoUserInfo():
    if 'username' in session:
        username = session['username']
    else:
        username = ""
    data = model.user.User.get_userinfo(username)
    return render_template("webpages/user/userInfo.html", username=username, data=data)


@app.route('/user/checkUserInfo', methods=['POST'])
def modify_info():
    data = json.loads(request.form.get('data'))
    Nick_name = data['user_Nick_name']
    Email = data['user_Email']
    if model.user.User.modify_userinfo(Nick_name, Email):
        return jsonify({'ok': True})
    else:
        return jsonify({'ok': False})


@app.route('/user/outlogin')
def out_login():
    if 'username' in session:
        session.pop('username')
    return render_template("webpages/user/login.html")


@app.route('/user/goFeedback')
def goFeedback():
    if 'username' in session:
        username = session['username']
    else:
        username = ""
    return render_template('webpages/user/feedback.html', username=username)


@app.route('/user/feedback', methods=['POST'])
def feedback():
    if 'username' in session:
        username = session['username']
        data = json.loads(request.form.get('data'))
        feedback_context = data['feedback_context']
        if model.user.User.feedbackInsert(username, feedback_context):
            return jsonify({'ok': True})
        else:
            return jsonify({'ok': False})
    else:
        username = ""
        return jsonify({'ok': 'unlogin'})


