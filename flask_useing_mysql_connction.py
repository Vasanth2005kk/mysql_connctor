import flask
from flask import request, jsonify, json

import mysql.connector

app = flask.Flask(__name__)

@app.route("/")
def index():
    return '<h1> WELCOME TO ALL </h1>'.upper()

# MySQL configurations
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'vasanth'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('select * from users')  
    rows = cursor.fetchall()
    # cursor.close()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)

#pip install mysql-connector-python