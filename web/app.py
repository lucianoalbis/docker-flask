from flask import Flask, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

try:
    connection = mysql.connector.connect(host='172.29.0.2', user='root', password='root', database='dbpython')
    if connection.is_connected():
       db_Info = connection.get_server_info()
       print("Connected to MySQL database... MySQL Server version on ",db_Info)
       cursor = connection.cursor()
       cursor.execute("select database();")
       record = cursor.fetchone()
       print ("Your connected to - ", record)
except Error as e :
    print ("Error while connecting to MySQL", e)

@app.route('/')
def add_user():
    sql_insert_query = """ INSERT INTO `users` (`id`, `name`, `age`) VALUES (0,'Luciano Albis', 34)"""
    cursor.execute(sql_insert_query)
    connection.commit()
    return 'User add!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
