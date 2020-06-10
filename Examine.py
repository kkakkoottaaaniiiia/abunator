# coding: utf-8

import os
import flask
import psycopg2
import random

users = "Postgres"
dbnames = "Abunator"
passwords = "postgres"

DATABASE_URL= " user=" + users +" dbname=" + dbnames +" password=" + passwords

culumnList = ["size","division","color","region","place","pattern","symptoms","food","decider01","decider02"]

questionList = []

def setQuestion():
    questionList.clear

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def getCulmn():
    if (len(questionList) <= 35):
        num = random.randint(1,len(culumnList))
        culumn = culumnList[num]
        return culumn
    else:
        culumn = "decider02"
        return culumn

def getQuestion(culumn):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT" + culumn + "FROM animals ORDER BY random() limit 1")
            result = cur.fetchall()
            question = result.getString(1)

            return question
