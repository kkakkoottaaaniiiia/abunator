# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:20:26 2020

@author: School
"""


# coding: utf-8

import os
import flask
import psycopg2

#これまでのSQL文、カラム、質問を収納します
SQLList = []
ColumnList = []
QuestionList = []

users = "Postgres" 
dbnames = "Abunator"
passwords = "postgres"

#データベースにアクセスするための情報(ローカルの場合)
DATABASE_URL= " user=" + users +" dbname=" + dbnames +" password=" + passwords

#DBに接続
def get_connection():
    return psycopg2.connect(DATABASE_URL)

#回答をリストに記録
def Listmaker(answer,column,question):
    if answer == 0 :
        Mher = column + " = '" + question + "'"
        SQLList.append(Mher)
    elif answer == 1 :
        Mher = column + " != '" + question + "'"
        SQLList.append(Mher)
    elif answer == 2 :
        Mher = "no >= 1"
        SQLList.append(Mher)

#過去の回答内容を取り出してSQL文にする
def SQLmaker():
    Searchsql = "no >= 1"
    for i in range(0,len(SQLList)-1):
        Searchsql = Searchsql + " and " + SQLList[i]
    return  Searchsql

#回答の内容に合致する動物の数を数える
def Get_count(answer,column,question):
        Listmaker(answer,column, question)
        with get_connection() as con:
            with con.cursor as cur :
                cur.execute("select count (*) from animals where " + SQLmaker())
                results = cur.fetchall()
        for i in results:
            Ararat = i[0]
            break
        return int(Ararat)