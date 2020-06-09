# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:36:33 2020

@author: School
"""
import os
import counter
import psycopg2
import flask

url = 'Yotsudsuka'

def get_connection():
    return psycopg2.connect(url)
    
def resName():
    with get_connection() as con:
            with con.cursor as cur :
                cur.execute("select name from animals where " + counter.SQLmaker())
                results = cur.fetchall()
    for i in results:
        Aragat = i[0]
        break
    return str(Aragat)

def resDealing():
    with get_connection() as con:
            with con.cursor as cur :
                cur.execute("select dealing from animals where " + counter.SQLmaker())
                results = cur.fetchall()
    for i in results:
        Azhdahak = i[0]
        break
    return str(Azhdahak)