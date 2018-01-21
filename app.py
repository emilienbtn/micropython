from flask import Flask, jsonify, request, make_response, abort, render_template, redirect, session, url_for
from time import gmtime, strftime
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
import json
import random

app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'
CORS(app)

#Connection to the database
connection = MongoClient("mongodb://localhost:27017/")
def create_mongodatabase():
    try:
        dbnames = connection.database_names()
        if 'micropython' not in dbnames:
            db_users = connection.micropython.users
            db_tweets = connection.micropython.tweets
            db_api = connection.micropython.apirelease

            db_users.insert({
            "email": "user1@users.com",
            "id": 1,
            "name": "User 1",
            "password": "user1",
            "username": "user1"
            })

            db_tweets.insert({
            "body": "Test new db #MongoDB",
            "id": 1,
            "timestamp": "2018-01-19T06:39:40Z",
            "tweetedby": "user1"
            })

            db_api.insert( {
              "buildtime": "2018-01-01 10:00:00",
              "links": "/api/v1/users",
              "methods": "get, post, put, delete",
              "version": "v1"
            })

            db_api.insert( {
              "buildtime": "2018-01-02 10:00:00",
              "links": "/api/v1/tweets",
              "methods": "get, post",
              "version": "v1"
            })
            print ("Database Initialize completed!")
        else:
            print ("Database already Initialized!")
    except:
        print ("Database creation failed!")

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
    return list_users()

def list_users():
    db = connection.micropython.users
    api_list=[]
    for row in db.find():
        api_list.append(str(row))
    return jsonify({'user_list': api_list})

## Get user by id
@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return list_user(user_id)

def list_user(user_id):
    print (user_id)
    api_list=[]
    db = connection.cloud_native.users
    for row in db.find({'id':user_id}):
        api_list.append(str(row))
    if api_list == []:
        abort(404)
    return jsonify({'user_details':api_list})

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
    return jsonify({'status': add_user(user)}), 201

def add_user(new_user):
    db = connection.micropython.users
    api_list=[]
    user = db.find({'$or':[{"username":new_user['username']},{"email":new_user['email']}]})
    for row in user:
        print(str(row))
        api_list.append(str(row))
    if api_list == []:
        db.insert(new_user)
        return "Success"
    else:
        abort(409)

## Delete
@app.route('/api/v1/users', methods=['DELETE'])
def delete_user():
    if not request.json or not 'username' in request.json:
        abort(400)
    user=request.json['username']
    return jsonify({'status': del_user(user)}), 200

def del_user(del_user):
    db = connection.micropython.users
    api_list = []
    for i in db.find({'username':del_user}):
        api_list.append(str(i))
    if api_list == []:
        abort(404)
    else:
        db.remove({"username":del_user})
        return "Success"

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
    return jsonify({'status': update_user(user)}), 200

def update_user(user):
    db = connection.micropython.users
    exist_user = db.find_one({"id":user['id']})
    if exist_user is None:
        abort(404)
    else:
        db_user.update({'id':user['id']},{'$set': user}, upsert=False )
        return "Success"

##### Tweets management
## Get
@app.route('/api/v1/tweets', methods=['GET'])
def get_tweets():
    return list_tweets()

def list_tweets():
    conn = sqlite3.connect('mydb.db')
    print("Opened database successfully")
    api_list=[]
    cursor=conn.cursor()
    cursor.execute("SELECT username, body, tweet_time, id from tweets")
    data = cursor.fetchall()
    print(data)
    print(len(data))
    if len(data) == 0:
        return api_list
    else:
        for row in data:
            tweets = {}
            tweets['tweetedby'] = row[0]
            tweets['body'] = row[1]
            tweets['timestamp'] = row[2]
            tweets['id'] = row[3]
            print(tweets)
            api_list.append(tweets)
    conn.close()
    print(api_list)
    return jsonify({'tweets_list': api_list})

## Get by tweet id
@app.route('/api/v1/tweets/<int:id>', methods=['GET'])
def get_tweet(id):
    return list_tweet(id)

def list_tweet(user_id):
    print(user_id)
    conn = sqlite3.connect('mydb.db')
    print("Opened database successfully")
    api_list=[]
    cursor=conn.cursor()
    cursor.execute("SELECT * from tweets where id=?",(user_id,))
    data = cursor.fetchall()
    print(data)
    if len(data) == 0:
        abort(404)
    else:
        user = {}
        user['id'] = data[0][0]
        user['username'] = data[0][1]
        user['body'] = data[0][2]
        user['tweet_time'] = data[0][3]
    conn.close()
    return jsonify(user)

## POST
@app.route('/api/v1/tweets', methods=['POST'])
def add_tweets():
    user_tweet = {}
    if not request.json or not 'username' in request.json or not 'body' in request.json:
        abort(400)
    user_tweet['username'] = request.json['username']
    user_tweet['body'] = request.json['body']
    user_tweet['created_at']=strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
    print (user_tweet)
    return  jsonify({'status': add_tweet(user_tweet)}), 201

def add_tweet(new_tweets):
    conn = sqlite3.connect('mydb.db')
    print("Opened database successfully")
    cursor=conn.cursor()
    cursor.execute("SELECT * from users where username=? ", (new_tweets['username'],))
    data = cursor.fetchall()
    if len(data) == 0:
        abort(404)
    else:
        cursor.execute("INSERT into tweets (username, body, tweet_time) values(?,?,?)",(new_tweets['username'],new_tweets['body'],new_tweets['created_at']))
        conn.commit()
        return "Success"

#### Link with frontend

def sumSessionCounter():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1

@app.route('/')
def main():
    sumSessionCounter()
    return render_template('main.html')

@app.route('/adduser')
def adduser():
    return render_template('adduser.html')

@app.route('/addtweets')
def addtweets():
    return render_template('addtweets.html')

@app.route('/addname')
def addname():
    if request.args.get('yourname'):
        session['name'] = request.args.get('yourname')
        # And then redirect the user to the main page
        return redirect(url_for('main'))
    else:
        return render_template('addname.html', session=session)

@app.route('/clear')
def clearsession():
    # Clear the session
    session.clear()
    # Redirect the user to the main page
    return redirect(url_for('main'))

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