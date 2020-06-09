# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:22:08 2020

@author: School
"""
from flask import Flask,render_template,request,session,redirect
import counter

PathList = [0]

app = Flask(__name__)

member_data = {}
message_data = {}

@app.route('/main', methods = ['POST'])

def branch():

    answer = int(request.form.get('answer'))
    column = str(request.form,get('column'))
    question = str(request.form.get('question'))
    path = int(request.form.get('path'))
    
    del PathList[len(PathList)-1]
    PathList.append(path)

    count = int(counter.Get_count(answer,column,question))

    if len(Answerlist) == 0 and PathList[len(tfList)-1] is 1:
        return redirect('/index')

    elif count == 1:
        return redirect('/result')

    elif count == 0:
        return redirect('/unknown')

    elif count >= 2:
        return redirect('/question')

    else:
        return redirect('/error')