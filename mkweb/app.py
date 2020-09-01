from flask import Flask, render_template
app = Flask(__name__)

##html
@app.route('/')
def home():
    return 'This is HOME'

@app.route('/mypage')
def mypage():
    return render_template('index.html')

## API
@app.route('/test', methods=['POST'])
def test_post():
    return jsonify({'result' : 'success', 'msg':'이 요청은 POST'})

@app.route('/test', methods=['GET'])
def test_get():
    return jsonify({'result':'success', 'msg':'이 요청은 GET!'})
    

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)