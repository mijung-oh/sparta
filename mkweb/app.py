#!/usr/bin/python
# -*- coding: utf-8 -*-

## 플라스크 실행 : python3 -m flask run

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
articles = []
article_no = 1
@app.route('/')
def home():
    return 'This is Home!'


@app.route('/mypage')
def mypage():
    return render_template('index2.html')


@app.route('/post', methods=['POST'])
def post():
    global articles
    global article_no
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    article = {'url': url_receive, 'comment': comment_receive, 'no': article_no}
    article_no = article_no + 1
    articles.append(article)
    return jsonify({'result':'success'})


@app.route('/post', methods=['GET'])
def view():
    return jsonify({'result':'success', 'articles': articles})


@app.route('/delete', methods=['POST'])
def delete():
    global articles
    no_receive = request.form['no_give']
    for article in articles:
        if str(article['no']) == no_receive:
            articles.remove(article)
            return jsonify({'result':'success'})
    return jsonify({'result':'fail', 'msg':'nn'})


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)