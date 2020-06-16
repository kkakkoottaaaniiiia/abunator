#図鑑のDB pic_bookと連動する
#result.pyのtableを変えた物を作る

import sys
sys.path.append("/Abunator/")
import os
import counter
import psycopg2
import flask

users = "postgres" 
dbnames = "Abunator"
passwords = "postgres"

#データベースにアクセスするための情報(ローカルの場合)
DATABASE_URL= " user=" + users +" dbname=" + dbnames +" password=" + passwords

def get_connection():
    return psycopg2.connect(DATABASE_URL)
    
#noは画像クリックの際にpostでもらう

def resName(no):
    with get_connection() as con:
            with con.cursor() as cur:
                cur.execute("select name from pic_book where no = " + str(no))
                results = cur.fetchall()
    for i in results:
        animals = i[0]
        break
    return str(animals)

def resDealing(no):
    with get_connection() as con:
            with con.cursor() as cur:
                cur.execute("select dealing from pic_book where no = " + str(no))
                results = cur.fetchall()
    for i in results:
        explanation = i[0]
        break
    return str(explanation)