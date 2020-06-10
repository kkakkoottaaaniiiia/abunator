# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:36:33 2020

@author: School
"""
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
    
def resNumber():
    with get_connection() as con:
            with con.cursor as cur :
                cur.execute("select no from animals where " + counter.SQLmaker())
                results = cur.fetchall()
    for i in results:
        Aramazd = i[0]
        break
    return int(Aramazd)

def resName(number):
    with get_connection() as con:
            with con.cursor as cur :
                cur.execute("select name from animals where no = " + number)
                results = cur.fetchall()
    for i in results:
        Anahit = i[0]
        break
    return str(Anahit)

def resDealing(number):
    with get_connection() as con:
            with con.cursor as cur :
                cur.execute("select dealing from animals where no = " + number)
                results = cur.fetchall()
    for i in results:
        Vahagn = i[0]
        break
    return str(Vahagn)

#変数としてresNumberの結果を記録し、それを鍵として、動物の名前と画像とコメントを取り出せないかな