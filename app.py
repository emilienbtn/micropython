from flask import Flask, jsonify, request, make_response, abort, render_template, redirect, session, url_for, flash
from time import gmtime, strftime
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
from flask_mongoalchemy import MongoAlchemy
from flask_pymongo import PyMongo
from time import gmtime, strftime
from auth0.v3.authentication import GetToken
from auth0.v3.authentication import Users
from requests import Requests
import os
import json
import random
import bcrypt

# Object creation
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = '<some secret key>'
CORS(app)

app.config['MONGOALCHEMY_DATABASE'] = 'app'
app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://localhost:27017/'
connection = MongoClient("mongodb://localhost:27017/")

db = MongoAlchemy()

mongo=PyMongo(app)
# Initialize Database
def create_mongodatabase():
    try:
        dbnames = connection.database_names()
        if 'app' not in dbnames:
            db_api = connection.app.apirelease
            db_api.insert( {
              "buildtime": "2018-01-01 10:00:00",
              "links": "/api/v1/users",
              "methods": "get, post, put, delete",
              "version": "v1"
            })
            db_api.insert( {
              "buildtime": "2018-02-11 10:00:00",
              "links": "api/v1/tweets",
              "methods": "get, post",
              "version": "2018-01-10 10:00:00"
            })
            print ("Database Initialize completed!")
        else:
            print ("Database already Initialized!")
    except:
        print ("Database creation failed!!")


#### Link with frontend
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html', session = session['username'])

@app.route('/index')
def index():
    return render_template('index.html', session = session['username'])

@app.route('/login', methods=['POST'])
def do_admin_login():
    users = mongo.db.users
    api_list=[]
    login_user = users.find({'username': request.form['username']})
    for i in login_user:
        api_list.append(i)
    print (api_list)
    if api_list != []:
        # print (api_list[0]['password'].decode('utf-8'), bcrypt.hashpw(request.form['password'].encode('utf-8'), api_list[0]['password']).decode('utf-8'))
        if api_list[0]['password'].decode('utf-8') == bcrypt.hashpw(request.form['password'].encode('utf-8'), api_list[0]['password']).decode('utf-8'):
            session['logged_in'] = api_list[0]['username']
            return redirect(url_for('index'))
        return 'Invalide username/password!'
    else:
        flash("Invalid Authentication")
    return 'Invalid User!'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='POST':
        users = mongo.db.users
        api_list=[]
        existing_user = users.find({'$or':[{"username":request.form['username']} ,{"email":request.form['email']}]})
        for i in existing_user:
            # print (str(i))
            api_list.append(str(i))
        # print (api_list)
        if api_list == []:
            users.insert({
            "email": request.form['email'],
            "id": random.randint(1,1000),
            "name": request.form['name'],
            "password": bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt()),
            "username": request.form['username']
            })
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        return 'That user already exists'
    else :
        return render_template('signup.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('home'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method=='POST':
        users = mongo.db.users
        api_list=[]
        existing_users = users.find({"username":session['username']})
        for i in existing_users:
            # print (str(i))
            api_list.append(str(i))
        user = {}
        print (api_list)
        if api_list != []:
            print (request.form['email'])
            user['email']=request.form['email']
            user['name']= request.form['name']
            user['password']=request.form['pass']
            users.update({'username':session['username']},{'$set': user} )
        else:
            return 'User not found!'
        return redirect(url_for('index'))
    if request.method=='GET':
        users = mongo.db.users
        user=[]
        print (session['username'])
        existing_user = users.find({"username":session['username']})
        for i in existing_user:
            user.append(i)
        return render_template('profile.html', name=user[0]['name'], username=user[0]['username'], password=user[0]['password'], email=user[0]['email'])

#Set-up for Auth0
@app.route('/callback')
def callback_handling():
    code = request.args.get('code')
    get_token = GetToken('manishsethis.auth0.com')
    auth0_users = Users('manishsethis.auth0.com')
    token = get_token.authorization_code(os.environ['CLIENT_ID'], os.environ['CLIENT_SECRET'], code, 'http://localhost:5000/callback')
    user_info = auth0_users.userinfo(token['access_token'])
    session['profile'] = json.loads(user_info)
    return redirect('/dashboard')

@app.route("/dashboard")
def dashboard():
    return render_template('index.html', user=session['profile'])

##### Info API
@app.route("/api/v1/info")
def home_index():
    api_list=[]
    db = connection.micropython.apirelease
    for row in db.find():
        api_list.append(str(row))
    return jsonify({'api_version': api_list}), 200

##### Users management
## Get
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return Requests.list_users()

## Get user by id
@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return Requests.list_user(user_id)

## Post
@app.route('/api/v1/users', methods=['POST'])
def create_user():
    print(request.json)
    if not request.json or not 'username' in request.json or not 'email' in request.json or not 'password' in request.json:
        abort(400)
    user = {
        'username': request.json['username'],
        'email': request.json['email'],
        'name': request.json.get('name',""),
        'password': request.json['password'],
        'id': random.randint(1,1000)
    }
    return jsonify({'status': Requests.add_user(user)}), 201

## Delete
@app.route('/api/v1/users', methods=['DELETE'])
def delete_user():
    if not request.json or not 'username' in request.json:
        abort(400)
    user=request.json['username']
    return jsonify({'status': Requests.del_user(user)}), 200

## PUT
@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = {}
    if not request.json:
        abort(400)
    user['id']=user_id
    key_list = request.json.keys()
    for i in key_list:
        user[i] = request.json[i]
    return jsonify({'status': Requests.update_user(user)}), 200
  
##### Tweets management
## Get
@app.route('/api/v1/tweets', methods=['GET'])
def get_tweets():
    return Requests.list_tweets()

## Get by tweet id
@app.route('/api/v1/tweets/<int:id>', methods=['GET'])
def get_tweet(id):
    return Requests.list_tweet(id)

## POST
@app.route('/api/v1/tweets', methods=['POST'])
def add_tweets():
    print ("add tweet")
    user_tweet = {}
    if not request.json or not 'username' in request.json or not 'body' in request.json:
        abort(400)
    user_tweet['tweetedby'] = request.json['username']
    user_tweet['body'] = request.json['body']
    user_tweet['created_at']=strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
    user_tweet['id'] = random.randint(1,1000)
    return jsonify({'status': Requests.add_tweet(user_tweet)}), 201

##### Error handlers
@app.errorhandler(400)
def invalid_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.errorhandler(404)
def resource_not_found(error):
    return make_response(jsonify({'error': 'Resource not found !'}), 404)

@app.errorhandler(409)
def user_found(error):
    return make_response(jsonify({'error': 'Conflict! Record exist'}), 409)

# Main launcher
if __name__ == "__main__":
    create_mongodatabase()
    app.run(host='0.0.0.0', port=5000, debug=True)