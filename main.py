from flask import Flask, request, jsonify
from kakao_regular import get_kakao_regular

app = Flask(__name__)
#app.config['JSON_AS_ASCII'] = False #한글이 깨지지 않도록
 
@app.route('/userLogin', methods = ['POST'])
def userLogin():
    user = request.get_json()#json 데이터를 받아옴
    return jsonify(user)# 받아온 데이터를 다시 전송
 
@app.route('/')
def hello_world():
    return jsonify("hello world")


@app.route('/kakao_regular')
def test() :
    data = get_kakao_regular()
    return jsonify(data)
    

if __name__ == "__main__":
    app.run()
