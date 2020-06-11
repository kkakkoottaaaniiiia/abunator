# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:22:08 2020

@author: School
"""
from flask import Flask,render_template,request,session,redirect
app = Flask(__name__)

import sys
sys.path.append("/Abunator/")

import counter
import setters
import sqlMethods

PathList = [0] 

@app.route('/',methods = ['GET'] )
def index():  
    return render_template('/index.html')


@app.route('/start',methods = ['GET'])
def starter():
    setters.setPathList()
    setters.setColumnList()
    setters.setQuestionList()
    setters.setSQLList()
    return render_template('/main.html',\
        question = sqlMethods.questionVerse(sqlMethods.getCalm(counter.ColumnList)))

@app.route('/return',methods = ['GET'])
def initial():
    return render_template('/index.html')


#@app.route('/main',methods = ['GET'])
#def procedure():
#    return render_template('/main.html',\
#        question = sqlMethods.questionVerse(sqlMethods.getCalm(counter.ColumnList)))
    
        
def back():
    pass


@app.route('/main', methods=['POST'])
def branch():
    answer = request.form.get('answer')
    column = request.form.get('column')
    question = request.form.get('question')
    path = request.form.get('path')
    
    del PathList[len(PathList)-1]
    PathList.append(path)

    count = int(counter.Get_count(answer,column,question))

    if (PathList[len(PathList)-1] is 1) and (counter.QuestionList[len(counter.QuestionList)-1] is counter.QuestionList[0]):
        return render_template('/index.html')
    
    elif count >= 2 and PathList[len(PathList)-1] is 1:
        back()
    
    elif count == 1:
        return render_template('/result.html')

    elif count == 0:
        return render_template('/unknown.html')

    elif count >= 2:
        return render_template('/main.html',\
        question = sqlMethods.questionVerse(sqlMethods.getCalm(counter.ColumnList)))

    else:
        return render_template('/error.html')
   
if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)  