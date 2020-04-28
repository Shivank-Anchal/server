#!flask/bin/python
from flask import Flask, jsonify,request,json,flash,redirect,render_template
from werkzeug.utils import secure_filename
from random import randint

app = Flask(__name__, template_folder='D:/PythonProgram/Server/api')

@app.route('/test')
def upload():
    return render_template('upload1.html')



@app.route('/test/upload',methods = ['GET','POST'])
def uploader():
    if request.method == 'POST':

        if 'parts' not in request.files:
            print('no file part')
        for file in request.files.getlist('parts'):
            filename = secure_filename(file.filename)
            file.save(filename)
        print(request.form['description'])
        
    
    return "lol"

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
            'id':randint(0,9999)
        }
        print(response['id'])
        
        return jsonify(response)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)