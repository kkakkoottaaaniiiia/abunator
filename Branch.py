# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:22:08 2020

@author: School
"""
from flask import Flask,render_template,request,session,redirect
app = Flask(__name__)
app.secret_key = b'random string...'

import counter

PathList = []

member_data = {}
message_data = {}


@app.route('/',methods = ['GET'] )
def index():
    return render_template('/index.html')


@app.route('/start',methods = ['GET'])
def starter():
    return render_template('/main.html')

@app.route('/return',methods = ['GET'])
def returner():
    return render_template('/index.html')


@app.route('/main', methods=['POST'])
def branch():

    answer = int(request.form.get('answer'))
    column = str(request.form.get('column'))
    question = str(request.form.get('question'))
    path = int(request.form.get('path'))
    
    del PathList[len(PathList)-1]
    PathList.append(path)

    count = int(counter.Get_count(answer,column,question))

    if (PathList[len(PathList)-1] is 1) and (counter.QuestionList[len(counter.QuestionList)-1] is counter.QuestionList[0]):
        return render_template('/index.html')

    elif count == 1:
        return render_template('/result.html')

    elif count == 0:
        return render_template('/unknown.html')

    elif count >= 2:
        return render_template('/question.html')

    else:
        return render_template('/error.html')
   
if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)  

    