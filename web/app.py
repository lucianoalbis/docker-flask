from flask import Flask, request
import mysql.connector
from mysql.connector import Error
from env import load
import json
import os

app = Flask(__name__)

load()

try:
    connection = mysql.connector.connect(host=os.environ['HOST'], user=os.environ['USER'], password=os.environ['PASSWORD'], database=os.environ['DATABASE'])
    if connection.is_connected():
       cursor = connection.cursor()
except Error as e :
    print ("Error while connecting to MySQL", e)

@app.route('/')
def add_user():
    sql_insert_query = """ INSERT INTO `users` (`id`, `name`, `age`) VALUES (0,'Luciano Albis', 34)"""
    cursor.execute(sql_insert_query)
    connection.commit()
    return 'User add!'

@app.route('/list_user')
def list_user():
    users = []
    user = {}

    sql_select_query = """ SELECT * FROM `users`"""
    cursor.execute(sql_select_query)
    records = cursor.fetchall()

    for row in records:
        user = {
            "id": row[0],
            "name": row[1],
            "age": row[2]
        }
        users.append(user)

    return json.dumps(users)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
