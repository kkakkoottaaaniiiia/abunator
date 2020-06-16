# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 09:50:58 2020

@author: School
"""
import sys
sys.path.append("/Abunator/")

import sqlMethods
import counter
import app


#ここにある関数を使えば、好きな配列を初期化できる

def setPathList():
    app.PathList.clear()
    app.PathList.append(0)

def setColumnList():
    counter.ColumnList.clear()
    counter.ColumnList.append("no")
    counter.ColumnList.append("name")
    counter.ColumnList.append("dealing")

def setQuestionList():
    counter.QuestionList.clear()

def setSQLList():
    counter.SQLList.clear()
    counter.SQLList.append("no >= 1")
    


