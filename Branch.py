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
import Examine
import result

PathList = [0] 
# 

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
#    return render_template('/main.html',\count = count ,\
#        question = sqlMethods.questionVerse(sqlMethods.getCalm(counter.ColumnList)))
    

@app.route('/main', methods = ['POST'])
def branch():
    answer = request.form.get("answer")
    path = request.form.get("path")
    column = counter.ColumnList[len(counter.ColumnList)-1]
    question = counter.QuestionList[len(counter.QuestionList)-1]
    
    
    del PathList[len(PathList)-1]
    PathList.append(int(path))
    
    counter.ListMaker(int(answer),column,question)
    count = counter.GetCount()

    if PathList[len(PathList)-1] is 1 and counter.QuestionList[len(counter.QuestionList)-1] is counter.QuestionList[0]:
        return render_template('/index.html')
    
    elif PathList[len(PathList)-1] is 1:
        del counter.SQLList [len(counter.SQLList)-1]
        del counter.SQLList [len(counter.SQLList)-1]
        del counter.ColumnList [len(counter.ColumnList)-1]
        del counter.QuestionList [len(counter.QuestionList)-1]
        return render_template('/main.html',\
        question = 'それは' + counter.QuestionList[len(counter.QuestionList)-1] + '？')
            
    elif count == 1:
        number = result.resNumber()
        return render_template('/result.html',\
        number = number,\
        name = result.resName(number),\
        dealing = result.resDealing(number))

    elif count == 0 or len(counter.ColumnList) >= 50:
        return render_template('/unknown.html')

    elif count >= 2 and len(counter.ColumnList) < 18:
        return render_template('/main.html',\
        question = sqlMethods.questionVerse(sqlMethods.getCalm(counter.ColumnList)))
            
    elif count >= 2 and len(counter.ColumnList) >= 18:
        return render_template('/main.html',\
        question = Examine.getQuestion(Examine.getCulumn()))
            
    else:
        return render_template('/error.html')


#図鑑へのリンク
@app.route('/picture_book',methods = ['GET'] )
def picture_book(): 
    return render_template('/picture_book.html')

   
if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)  