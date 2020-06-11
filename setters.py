# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 09:50:58 2020

@author: School
"""
import sqlMethods
import counter
import Branch


#ここにある関数を使えば、好きな配列を初期化できる

def setPathList():
    Branch.PathList.clear()
    Branch.PathList.append(0)

def setColumnList():
    counter.ColumnList.clear()

def setQuestionList():
    counter.QuestionList.clear()

def setSQLList():
    counter.SQLList.clear()