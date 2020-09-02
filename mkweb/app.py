## �ö�ũ ���� : python3 -m flask run
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
articles = []
article_no = 1
# HTML�� �ִ� �κ�
@app.route('/')
def home():
    return 'This is Home!'
    
@app.route('/mypage')
def mypage():
    return render_template('index.html')
## API ������ �ϴ� �κ�
@app.route('/post', methods=['POST'])
def post():
    global articles # �� �Լ� �ȿ��� ������ articles �۷ι� ������ ����ŵ�ϴ�.
    global article_no # �� �Լ� �ȿ��� ������ article_no�� �۷ι� ������ ����ŵ�ϴ�.
    url_receive = request.form['url_give'] # Ŭ���̾�Ʈ�κ��� url�� �޴� �κ�
    comment_receive = request.form['comment_give'] # Ŭ���̾�Ʈ�κ��� comment�� �޴� �κ�
    article = {'url':url_receive,'comment':comment_receive, 'no':article_no} # ���� �� ��ųʸ��� ��
    article_no = article_no + 1
    articles.append(article) # �ִ´�
    return jsonify({'result':'success'})

@app.route('/post', methods=['GET'])
def view():
    return jsonify({'result':'success', 'articles':articles})

@app.route('/delete', methods=['POST'])
def delete():
    global articles # �� �Լ� �ȿ��� ������ articles �۷ι� ������ ����ŵ�ϴ�.
    no_receive = request.form['no_give'] # Ŭ���̾�Ʈ�κ��� no�� �޴� �κ�
    for article in articles: # �ݺ���: articles�� ���鼭,
        if str(article['no']) == no_receive: # ���ǹ�: ���� no�� ���� ��ȣ�� ��ƼŬ�� ã�Ƽ� (��, ���ڿ� == ���ڿ���!)
            articles.remove(article) # �ش� article�� �����,
            return jsonify({'result':'success'}) # ����� �ְ� �Լ��� ������.
    return jsonify({'result':'fail', 'msg':'nn'}) # ���� �ݺ����� �� ���Ƶ� ����� ���� �ʾ�����, ��ƼŬ�� ���ٰ� �Ѵ�.

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)