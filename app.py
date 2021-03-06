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
#図鑑用クラスのインポート
import pic_book

PathList = [0]
#
#解答履歴を入れる変数を宣言
name = ''

@app.route('/',methods = ['GET'] )
def index():
    if name != '':
        return render_template('index.html',\
        name = name)
    else:
        return render_template('index.html',\
        name = '前回の検索結果はありません')


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
    #return render_template('/index.html')

    #前回の検索結果をスタート画面に表示したい グローバル変数で
    if name != '':
        return render_template('index.html',\
        name = name)
    else:
        return render_template('index.html',\
        name = '前回の検索結果はありません')



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

        #追加　グローバル変数で上書き
        global name
        name = result.resName(number)

        return render_template('/result.html',\
        number = number,\
        name = name,\
        dealing = result.resDealing(number))

    elif count == 0 or len(counter.ColumnList) >= 50:
        return render_template('/unknown.html')

    elif count >= 2 and len(counter.ColumnList) < 18:
        return render_template('/main.html',\
        question = sqlMethods.questionVerse(sqlMethods.getCalm(counter.ColumnList)))

    elif count >= 2 and len(counter.ColumnList) >= 18:
        column = Examine.getCulumn()
        question = Examine.getQuestion(column)
        if not question in counter.QuestionList:
            return render_template('/main.html',\
            question = question)
        else:
            while question in counter.QuestionList:
                column = Examine.getCulumn()
                question = Examine.getQuestion(column)  
            return render_template('/main.html',\
            question = question)            

    else:
        return render_template('/error.html')


#図鑑へのリンク
@app.route('/pic_book',methods = ['GET'] )
def zukan():
    return render_template('/picture_book.html')

#図鑑から解説への直通のリンク
@app.route('/picture_book',methods = ['POST'])
def kaisetu():
    if request.method == 'POST':
        no = request.form['no']
    else:
        no = "13"
    return render_template('/explanation.html',\
    no = no,\
    name = pic_book.resName(no),\
    dealing = pic_book.resDealing(no),\
    rank = pic_book.resRank(no))

#「前回の検索結果」で表示された動物について詳しく見られる機能
@app.route('/refer/<name>', methods = ['GET'])
def referrence(name):
    if name != '前回の検索結果はありません':
        name = name 
        no = pic_book.resNo(name)
        dealing = pic_book.resDealing(no)
        rank = pic_book.resRank(no)
        return render_template('/explanation.html',\
        no = no,\
        name = name,\
        dealing = dealing,\
        rank = rank)
    else:
        return render_template('/index.html',\
        name = '前回の検索結果はありません' )


if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)