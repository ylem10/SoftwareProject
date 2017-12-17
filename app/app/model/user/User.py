import DBLink
from flask import session


def userRegister(username, password, cellphone):
    # 插入数据库
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    sql = "insert into table_user_info values('%s', '%s', '', '%s', '', '17.jpg')" % (username, password, cellphone)
    print(sql)
    try:
        # 插入数据
        cur.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print(e)
        db.rollback()
        return False


def modifyPasswordByPhone(phone, new_password):
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    sql = "update table_user_info set user_pwd = '%s' where user_phone = '%s'" % (new_password, phone)
    print(sql)
    try:
        # 更新数据
        cur.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print(e)
        db.rollback()
        return False


# 根据电话号取出用户名
def getUsernaemByphone(phone):
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    sql = "select user_login_name from table_user_info where user_phone = '%s'" % phone
    print(sql)
    try:
        # 更新数据
        cur.execute(sql)
        data = cur.fetchone()
        return data[0]
    except Exception as e:
        print(e)
        db.rollback()
        return False


def user_login(username, password):
    # 查询数据库
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    sql = "select user_login_name, user_pwd from table_user_info where user_login_name='%s'" % username
    # print(sql)
    try:
        # 查询数据
        cur.execute(sql)
        row = cur.fetchone()
        if row[0] == username and row[1] == password:
            session['username'] = row[0]
            return True
    except Exception as e:
        print(e)
        db.rollback()
        return False


def checkUsername(username):
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    sql = "select count(*) from table_user_info where user_login_name='%s'" % username
    # print(sql)
    try:
        # 查询数据
        cur.execute(sql)
        row = cur.fetchone()
        if row[0] == 0:
            return False
        else:
            return True
    except Exception as e:
        print(e)
        db.rollback()
        return False


# 获取用户的个人信息
def get_userinfo(username):
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    sql = "select user_login_name,user_pwd,user_Nick_name,user_Email,user_phone,user_pic_url \
           from table_user_info where user_login_name='%s'" % username
    cur.execute(sql)
    info_data = cur.fetchone()
    # print(info_data)
    return info_data


# 修改个人信息
def modify_userinfo(Nick_name,Email):
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    sql = "update table_user_info set user_Nick_name= \
            '%s',user_Email='%s' where user_login_name='%s'" % (Nick_name,Email,session['username'])
    try:
        cur.execute(sql)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        print(e)
        return False


# 意见反馈
def feedbackInsert(username, feedback_context):
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    sql = "insert into table_feedback values(now(), '%s', 'admin', '1', '%s')" % (username, feedback_context)
    print(sql)
    try:
        # 插入数据
        cur.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print(e)
        db.rollback()
        return False