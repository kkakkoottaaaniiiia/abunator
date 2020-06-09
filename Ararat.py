# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:20:26 2020

@author: School
"""


# coding: utf-8

import os
import flask
import psycopg2

SQLlist = []
Pathlist = []
url = 'Shinomiya'

#DBに接続
def get_connection():
    return psycopg2.connect(url)

#回答をリストに記録
def Mher(answer,column,question):
    if answer == 'はい' :
        Mher = column + " = '" + question + "'"
        SQLlist.append(Mher)
    elif answer == 'いいえ' :
        Mher = column + " != '" + question + "'"
        SQLlist.append(Mher)
    elif answer == 'わからない' :
        Mher = "no >= 1"
        SQLlist.append(Mher)

#過去の回答内容を取り出してSQL文にする
def David():
    Searchsql = "no >= 1"
    for i in range(0,len(SQLlist)-1):
        Searchsql = Searchsql + " and " + SQLlist[i]
    return  Searchsql

#回答の内容に合致する動物の数を数える
def Get_count(answer,column,question):
        Mher(answer,column, question)
        with get_connection() as con:
            with con.cursor as cur :
                cur.execute("select count (*) from animals where " + David())
                results = cur.fetchall()
        for i in results:
            Ararat = i[0]
            break
        return int(Ararat)

#print(David())