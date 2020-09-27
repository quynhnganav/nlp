from flask import Flask,request
from model import TextClassificationPredict
import requests
import json

link="http://localhost/laravel/chatbot/public/data/data_train"
list_key=["sajkfh8dhfs87fhds"]
app = Flask(__name__)
nlp = TextClassificationPredict()
nlp.convert_data(str(requests.get(link).text))
nlp.train_model()


@app.route('/api/tra_loi/<key>/',methods=['GET'])
def tra_loi(key):
    if key in list_key:
        msg = request.args.get('msg')
        print(msg)
        tra_loi = str(nlp.tra_loi(msg))
        print(tra_loi)
        return tra_loi
    else:
        return 'error'

@app.route('/api/train_model/<key>/',methods=['GET'])
def train_model(key):
    if key in list_key:
        nlp.convert_data(str(requests.get(link).text))
        nlp.train_model()
        return "ok"
    else:
        return 'error'

@app.route('/api/test/<key>/',methods=['GET','POST'])
def test(key):
    if key in list_key:
        return "ok"
    else:
        return 'error'


 
if __name__ == '__main__':
    app.run(host='localhost', port=5000,threaded=False)
   