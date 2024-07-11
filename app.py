from flask import Flask, request, render_template, url_for,session, abort, redirect
import bot 
from dotenv import load_dotenv
import pymongo
import os
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

client = pymongo.MongoClient(os.getenv("DATABASE_URL"))
db = client['studysquad']

users = db['users']
notes = db['notes']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html', error="")

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        user=users.find_one({'email':session['username']})
        data=[user['name']]
        data.append(user['email'])
        data.append(user['dob'])
        return render_template('dashboard.html',data=data)
    return abort(401)

@app.route('/room',)
def room():
    if 'username' in session:
        return render_template('room.html')
    return abort(401)

@app.route('/file')
def file():
    if 'username' in session:
        data=notes.find_one({'email':session['username']})
        if data is None:
            data=""
        else:
            data=data['notes']
        return render_template('fileReader.html',data=data)
    return abort(401)

@app.route('/video')
def video():
    if 'username' in session:
        return render_template('video.html')
    return abort(401)

@app.route('/ytnotes')
def ytnotes():
    if 'username' in session:
        return render_template('ytnotes.html',data="")
    return abort(401)

@app.route('/registration')
def registration():
    return render_template('registration.html')
# API Endpoints


@app.route('/valid', methods=['POST'])
def valid():
    email=request.form['email']
    password=request.form['password']
    user = users.find_one({'email':email,'password':password})
    if user is None:
        return render_template('login.html',error="Invalid Credentials")
    session['username'] = email
    return redirect(url_for('dashboard'))

@app.route('/generate' , methods=['POST'])
def gen():
    video_id = request.form['link']
    api_key = users.find_one({'email':session['username']})['api_key']
    response = bot.get_notes(api_key,video_id)
    session['notes'] = response
    return render_template('ytnotes.html',data=response)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/register', methods=['POST'])
def register():
    email=request.form['email']
    password=request.form['password']
    name = request.form['name']
    dob = request.form['dob']
    api_key = request.form['api']
    user = users.find_one({'email':email})
    if user is None:
        users.insert_one({'email':email,'password':password,'name':name,'dob':dob,'api_key':api_key})
    return redirect(url_for('login'))

@app.route('/save', methods=['POST'])
def save():
    email = session['username']
    user = users.find_one({'email':email})
    if user is not None:
        notes.insert_one({'email':email,'notes':session['notes']})
    return redirect(url_for('ytnotes'))
if __name__ == '__main__':
    app.run(host="0.0.0.0")