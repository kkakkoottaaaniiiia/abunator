# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 09:50:58 2020

@author: School
"""
import sqlMethods
import counter
import Branch


def setPathList():
    Branch.PathList.clear()
    Branch.PathList = [0]

def setColumnList():
    counter.ColumnList.clear()

def setQuestionList():
    counter.QuestionList.clear()

def setSQLList():
    counter.SQLList.clear()