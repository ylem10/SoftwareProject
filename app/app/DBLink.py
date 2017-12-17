import pymysql


def conDB():
    db = pymysql.connect(
        host="localhost",
        database="student2",
        user="root",
        password="",
        port=3306,
        charset="utf8"
    )
    # db.autocommit(False)
    return db
