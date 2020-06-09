# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:22:08 2020

@author: School
"""
from flask import Flask,render_template.request,session,redirect
from Ararat import Mher
from Ararat import David
from Ararat import Get_count

tfList = [0]

app = (Flask__name__)
app.secret_key = b'random string...'

member_data = {}
message_data = {}

@app.route('/question', methods = ['POST'])

def branch():
count = int(Get_count(answer,column,question))

if (len(Answerlist) == 0) and (tfList[len(tfList)-1] == 1):
    return redirect('/index')

elif (count == 1):
    return redirect('/answer')

elif (count == 0):
    return redirect('/unknown')

elif (count >= 2):
    return redirect('/question')

else:
    return redirect('/error')