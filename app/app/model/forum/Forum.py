import DBLink, json, math


def showForum():
    # 插入数据库
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    sql = "select * from a_post_view"
    print(sql)
    try:
        # 取数据
        cur.execute(sql)
        rows = cur.fetchall()
        users = []
        data = {}
        for r in rows:
            user = {}
            user['user_login_name'] = r[0]
            user['user_Nick_name'] = r[1]
            user['user_pic_url'] = r[2]
            user['post_id'] = r[3]
            user['post_time'] = str(r[4])
            user['post_content'] = r[5]
            user['post_title'] = r[6]
            user['post_type'] = r[7]
            user['pic_id'] = r[8]
            user['pic_route'] = r[9]
            users.append(user)
        # jsonStr = json.dumps(data)
        cur.close()
        db.close()
        return users
    except Exception as e:
        print(e)
        db.rollback()
        return False


def showComment():
    # 插入数据库
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    sql = "select * from post_comment_view "
    print(sql)
    try:
        # 插入数据
        cur.execute(sql)
        rows = cur.fetchall()
        users = []
        data = {}
        for r in rows:
            user = {}
            user['post_id'] = r[0]
            user['comt_id'] = r[1]
            user['comt_commenter'] = r[2]
            user['comt_time'] = r[3]
            user['comt_content'] = str(r[4])
            user['pic_id'] = r[5]
            user['pic_route'] = r[6]
            users.append(user)
        # jsonStr = json.dumps(data)
        cur.close()
        db.close()
        return users
    except Exception as e:
        print(e)
        db.rollback()
        return False


def addCommnet(post_id, commenter, content):
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    sql = "insert into table_comment(comt_commenter, comt_post_id, comt_time, comt_content) values('%s', %s, now(), '%s')" % (
        commenter, post_id, content)
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


def delComment(comm_id):
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    sql = "delete from table_comment where comt_id='%s'" % (comm_id)
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


def getPostById(post_id):
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    sql = "select * from a_post_view where a_post_view.post_id = %s" % (post_id)
    print(sql)
    try:
        # 取数据
        cur.execute(sql)
        r = cur.fetchall()
        cur.close()
        db.close()
        return r
    except Exception as e:
        print(e)
        db.rollback()
        return False


def getCommentById(post_id, page):
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    page = 5 * page
    sql = "select * from post_comment_view INNER JOIN table_user_info on post_comment_view.comt_commenter = table_user_info.user_login_name where post_comment_view.post_id = %s order by comt_time desc limit %s, 5" % (
        post_id, page)
    print(sql)
    try:
        cur.execute(sql)
        rows = cur.fetchall()
        datas = []
        data = {}
        for r in rows:
            user = {}
            user['post_id'] = r[0]
            user['comt_id'] = r[1]
            user['comt_commenter'] = r[2]
            user['comt_time'] = str(r[3])
            user['comt_content'] = str(r[4])
            user['pic_id'] = r[5]
            user['pic_route'] = r[6]
            user['com_pic'] = r[12]
            datas.append(user)
        # jsonStr = json.dumps(data)
        cur.close()
        db.close()
        return datas
    except Exception as e:
        print(e)
        db.rollback()
        return False


def getPagesById(post_id):
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    sql = "select count(*) from post_comment_view where post_comment_view.post_id = %s" % (post_id)
    print(sql)
    try:
        # 取数据
        cur.execute(sql)
        r = cur.fetchall()
        print(r)
        cur.close()
        db.close()
        return r
    except Exception as e:
        print(e)
        db.rollback()
        return False


# 编辑论坛信息并添加
def addArticleInfo(user, post_title, post_content, pic, bool, post_id):
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    if bool == 'add':
        print(bool)
        sql = "insert into table_poster(post_user, post_time, post_content, post_title,post_type) VALUES \
          ('%s', now(), '%s', '%s','%s')" % (user, post_content, post_title, 'guanghanjiba')
    else:
        print(bool)
        sql = "update table_poster set post_title='%s',post_content='%s' where post_id=%s" % (
            post_title, post_content, post_id)
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


def delUserForum(post_id):
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    sql1 = "delete from table_poster where post_id = '%s'" % post_id
    sql2 = "delete from table_comment where comt_post_id = '%s'" % post_id
    print(sql1 + ':' + sql2)
    try:
        cur.execute(sql1)
        cur.execute(sql2)
        db.commit()
        return True
    except Exception as e:
        print(e)
        db.rollback()
        return False


def show_info(post_id):
    db = DBLink.conDB()
    db.autocommit(False)
    cur = db.cursor()
    sql = "select post_title,post_content from table_poster where post_id = '%s'" % post_id
    print(sql)
    try:
        cur.execute(sql)
        data = cur.fetchone()
        # print('laji:'+data[0])
        db.commit()
        return data
    except Exception as e:
        print(e)
        db.rollback()
        return None
