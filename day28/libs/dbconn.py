# 패키지 라이브러리 : 모듈을 가져와서 사용하고 싶을 때 만듦.
import sqlite3


def getconn():
    conn = sqlite3.connect("c:/webdb/webdb.db")
    return conn