#!flask/bin/python
from flask import Flask, jsonify,request,json,flash,redirect,render_template
from werkzeug.utils import secure_filename
from flask_wtf.file import FileField,FileRequired
from flask_wtf import FlaskForm
import logging

from werkzeug.datastructures import CombinedMultiDict
import flask

app = Flask(__name__, template_folder='D:/PythonProgram/Server/api')

@app.route('/test')
def upload():
    return render_template('upload1.html')



@app.route('/test/upload',methods = ['GET','POST'])
def uploader():
    if request.method == 'POST':

        print(flask.request.data)
        print(request.get_data)
        description = request.form['description']
        print(description)
        uploaded_file = request.files.getlist('fi')
        print(uploaded_file)
    
    return description

@app.route('/test/user',methods=['GET','POST'])
def test():
    if request.method == "GET":
        return jsonify({"response":"Get Request Called"})

    elif request.method == "POST":
        name=request.json['name']
        email=request.json['email']
        age=request.json['age']
        subject= request.json['subject']
        response = {
            'name' : name,
            'email':email,
            'age':age,
            'topics':subject,
            'id':453
        }
        
        return jsonify(response)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)