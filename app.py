from flask import Flask, jsonify
import json
import sqlite3

app = Flask(__name__)

@app.route ("/api/v1/info")
def home_index():
    conn = sqlite3.connect('mydb.db')
    print ("Opened database successfully");
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)