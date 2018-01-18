from flask import Flask, jsonify, request, make_response, abort, render_template, redirect, session, url_for
from time import gmtime, strftime
from flask_cors import CORS, cross_origin
import json
import sqlite3

app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'
CORS(app)

##### Info API
@app.route("/api/v1/info")
def home_index():
    conn = sqlite3.connect('mydb.db')
    print("Opened database successfully")
    app_list=[]
    cursor = conn.execute("SELECT buildtime, version, methods, links from apirelease")
    for row in cursor:
        a_dict = {}
        a_dict['buildtime'] = row[0]
        a_dict['version'] = row[1]
        a_dict['methods'] = row[2]
        a_dict['links'] = row[3]
        app_list.append(a_dict)
    conn.close()
    return jsonify({'api_version': app_list}), 200

##### Users management
## Get
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return list_users()

def list_users():
    conn = sqlite3.connect('mydb.db')
    print("Opened database successfuly")
    api_list=[]
    cursor = conn.execute("SELECT username, full_name, email, password, id from users")
    for row in cursor:
        a_dict = {}
        a_dict['username'] = row[0]
        a_dict['name'] = row[1]
        a_dict['email'] = row[2]
        a_dict['password'] = row[3]
        a_dict['id'] = row[4]
        api_list.append(a_dict)
    conn.close()
    return jsonify({'user_list': api_list})

## Post
@app.route('/api/v1/users', methods=['POST'])
def create_user():
    if not request.json or not 'username' in request.json or not 'email' in request.json or not 'password' in request.json:
        abort(400)
    user = {
        'username': request.json['username'],
        'email': request.json['email'],
        'name': request.json.get('name',""),
        'password': request.json['password']
    }
    return jsonify({'status': add_user(user)}), 201

def add_user(new_user):
    conn = sqlite3.connect('mydb.db')
    print("Opened database successfully")
    api_list=[]
    cursor=conn.cursor()
    cursor.execute("SELECT * from users where username=? or email=?",(new_user['username'],new_user['email']))
    data = cursor.fetchall()
    if len(data) != 0:
        abort(409)
    else:
        cursor.execute("insert into users (username, email, password, full_name) values(?,?,?,?)",(new_user['username'],new_user['email'], new_user['password'], new_user['name']))
        conn.commit()
        return "Success"
    conn.close()
    return jsonify(a_dict)

## Delete
@app.route('/api/v1/users', methods=['DELETE'])
def delete_user():
    if not request.json or not 'username' in request.json:
        abort(400)
    user=request.json['username']
    return jsonify({'status': del_user(user)}), 200

def del_user(del_user):
    conn = sqlite3.connect('mydb.db')
    print("Opened database successfully")
    cursor=conn.cursor()
    cursor.execute("SELECT * from users where username=? ",(del_user,))
    data = cursor.fetchall()
    print("Data, ",data)
    if len(data) == 0:
        abort(404)
    else:
        cursor.execute("DELETE from users where username==?",(del_user,))
        conn.commit()
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
    print(user)
    return jsonify({'status': update_user(user)}), 200

def update_user(user):
    conn=sqlite3.connect('mydb.db')
    print("Opened database successfully")
    cursor=conn.cursor()
    cursor.execute("SELECT * from users where id=? ",(user['id'],))
    data = cursor.fetchall()
    print("Data, ",data)
    if len(data) == 0:
        abort(404)
    else:
        key_list=user.keys()
        for i in key_list:
            if i != "id":
                print(user, i)
                cursor.execute("""UPDATE users SET {0} = ? WHERE id = ?""".format(i), (user[i], user['id']))
                conn.commit()
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

## Get by user id
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
    app.run(host='0.0.0.0', port=5000, debug=True)