# DBから画像urlをもらう
import sys
sys.path.append("/Abunator/")

import os
import flask
import psycopg2

#ローカルDBへのアクセスに必要なもの
users = "postgres" 
dbnames = "Abunator"
passwords = "postgres"

#データベースにアクセスするための情報(ローカルの場合)
DATABASE_URL= " user=" + users +" dbname=" + dbnames +" password=" + passwords

#DBに接続
def get_connection():
    return psycopg2.connect(DATABASE_URL)

#DBのimg_urlカラムを一つずつリストに入れる
def imgUrlList():
    #空のリストを作成
    []
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT img_url FROM "+dbnames+" ;")
            results = cur.fetchall()
            print(results)
    #for文で一つずつリストにurlを入れる
    for i in results:
        imgurl_list=i[0]
        break

    return imgurl_list
 
