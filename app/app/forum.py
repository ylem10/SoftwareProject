from __init__ import app
from flask import render_template, session, request, jsonify
import model.forum.Forum, json, math


@app.route('/forum/gotoForum')
def gotoForum():
    getForum = model.forum.Forum.showForum()
    getComment = model.forum.Forum.showComment()
    if 'username' in session:
        username = session['username']
    else:
        username = ""
    return render_template('webpages/forum/forum.html', getForum=getForum, getComment=getComment, username=username)


@app.route('/forum/addComment', methods=['POST'])
def addComment():
    data = json.loads(request.form.get('data'))
    post_id = data['post_id']
    comm_name = data['comm_name']
    comm_content = data['comm_content']
    # 插入数据库
    insertCom = model.forum.Forum.addCommnet(post_id, comm_name, comm_content)
    if insertCom:
        return jsonify({'ok': True})
    else:
        return jsonify({'ok': False})


@app.route('/forum/delcomment', methods=['GET', 'POST'])
def delcomment():
    comm_id = request.args.get('comm_id', '')
    print(comm_id)
    delCom = model.forum.Forum.delComment(comm_id)
    if delCom:
        return jsonify({'ok': True})
    else:
        return jsonify({'ok': False})


@app.route('/forum/editPost')
def editForum():
    username = session['username']
    return render_template('webpages/forum/editPost.html', username=username)


@app.route('/forum/goAddPost')
def goAddPost():
    username = session['username']
    return render_template('webpages/forum/editPost.html', username=username)


@app.route('/forum/goForumDetail', methods=['GET'])
def goForumDetail():
    post_id = request.args.get('post_id', '')
    getPost = model.forum.Forum.getPostById(post_id)
    getComment = model.forum.Forum.getCommentById(post_id, 0)
    comms = model.forum.Forum.getPagesById(post_id)[0][0]
    pages = math.ceil(model.forum.Forum.getPagesById(post_id)[0][0] / 5)
    if 'username' in session:
        username = session['username']
    else:
        username = ""
    return render_template('webpages/forum/forumDetail.html', getPost=getPost, getComment=getComment,
                           username=username, pages=pages, comms=comms)


# 评论分页
@app.route('/forum/commentPage', methods=['POST'])
def commentPage():
    data = json.loads(request.form.get('data'))
    page_num = int(data['page_num']) - 1
    post_id = data['post_id']
    getComment = model.forum.Forum.getCommentById(post_id, page_num)
    return json.dumps(getComment)


@app.route('/forum/commit_article', methods=['GET', 'POST'])
def commit_article():
    data = json.loads(request.form.get('data'))
    user = session['username']
    post_id = data['post_id']
    post_title = data['post_title']
    post_content = data['post_content']
    pic = data['pic']
    bool = data['bool']
    # 插入数据库
    insertCom = model.forum.Forum.addArticleInfo(user, post_title, post_content, pic, bool, post_id)
    if insertCom:
        return jsonify({'ok': True})
    else:
        return jsonify({'ok': False})


@app.route('/forum/delUserForum', methods=['GET', 'POST'])
def delUserForum():
    data = json.loads(request.form.get('data'))
    post_id = data['post_id']
    del_forum = model.forum.Forum.delUserForum(post_id)
    if del_forum:
        return jsonify({'ok': True})
    else:
        return jsonify({'ok': False})


@app.route('/forum/show_info', methods=['GET', 'POST'])
def show_info():
    post_id = request.args.get('post_id')
    info = model.forum.Forum.show_info(post_id)
    return render_template('webpages/forum/editPost.html', post_title=info[0], post_content=info[1])
