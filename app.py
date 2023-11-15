from flask import Flask, render_template, jsonify, request
import requests
import bs4 import BeautifulSoup
from pymongo import MongoClient


conenction_string = 'mongodb+srv://sahrul:sahrul@cluster0.nsaxt60.mongodb.net/?retryWrites=true&w=majority'
db = MongoClient(conenction_string)
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diary', methods=['GET'])
def show_diary():
    articles = list(db.diary.find({}, {'_id' : False}))
    return jsonify({'articles' : articles})

@app.route('/diary', methods=['POST'])
def save_diary():
    #sample_receive = request.form['sample_give']
    #print(sample_receive)
    title_receive = request.from.get('title_give')
    content_receive = request.from.get('content_give')
    
    file = request.files["file_give"]
    save_to = 'static/mypicture.jpg'
    file.save(save_to)

    doc = {
        'title' : filename,
        'title': title_receive
        'content':content_receive
    }
    db.diary.insert_one(doc)
    return jsonify({'message':'data was!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
