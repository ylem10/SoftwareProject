import os
from flask import Flask, request, url_for, send_from_directory, render_template, make_response, abort
import random, datetime, json

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'txt', 'xls'])

from __init__ import app

app.config['UPLOAD_FOLDER'] = os.getcwd() + '\static\images'
app.config['UPLOAD_FOLDER_EXCL'] = os.getcwd() + '\static\EXCL'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            # filename = file.filename
            now = datetime.datetime.now()
            filename = now.strftime('%Y%m%d%H%M%S') + '-' + str(random.randint(10000, 99999)) + '.' + \
                       file.filename.rsplit('.', 1)[1]
            if file.filename.rsplit('.', 1)[1] == "xls":
                file.save(os.path.join(app.config['UPLOAD_FOLDER_EXCL'], filename))
            else:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_url = url_for('uploaded_file', filename=filename)
    return file_url


@app.route("/downloadFile", methods=['GET', 'POST'])
def download_file():
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    filename = request.args.get("filename")
    print(filename)
    if request.method == "GET":
        if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER_EXCL'], filename)):
            return send_from_directory(app.config['UPLOAD_FOLDER_EXCL'], filename, as_attachment=True)
        abort(404)
    return render_template('webpages/user/modifyPwd.html')
