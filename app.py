# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:49:11 2020

@author: School
"""
from flask import Flask,render_template,request,session,redirect
app = Flask(__name__)

import counter

PathList = []

member_data = {}
message_data = {}


@app.route('/')

def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True)  