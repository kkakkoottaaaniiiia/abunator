# coding: utf-8

import os
import flask
import psycopg2
import random

#host = "18.181.156.243"
#port = "5432"
#dbname = "abunator"
#user = "postgres"
#password = "Ag9e832p@_30g!3d0b8alvm20;"
#table = "animals"
#DATABASE_URL = "host=" + user + "port=" + port + "dbname=" + dbname + "user=" + user + "password=" + password
#サーバー上のDBにつなぐときは↑



users = "Postgres"
dbnames = "Abunator"
passwords = "postgres"
table = "maintable"
DATABASE_URL= " user=" + users +" dbname=" + dbnames +" password=" + passwords
#ローカルのDBにつなぐときは↑

culumnList = ["size","division","color","region","place","time","season","poison","pattern","symptoms","food","sucker","epidemic","foreigner","individuality","dealing"]

questionList = []

def setQuestion():
    questionList.clear

def get_connection():
#    return psycopg2.connect(DATABASE_URL)

    return psycopg2.connect(host="abunator.postgres.database.azure.com",database="Abunator",user="teamD@abunator",port=5432, password="Nagato1109")


def getCulumn():
    if (len(questionList) <= 35):
        num = random.randint(1,len(culumnList))
        culumn = culumnList[num]
        return culumn
    else:
        culumn = "individuality"
        return culumn

def getQuestion(culumn):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT" + culumn + "FROM"+ table +"ORDER BY random() limit 1")
            result = cur.fetchall()
            question = result.getString(1)

            return 'それは'+ question + '？'