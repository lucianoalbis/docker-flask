from flask import Flask, request
from MySQLdb import _mysql

app = Flask(__name__)

try:
    db=_mysql.connect(host="172.27.0.2",port=3306,user="root",passwd="root",db="dbpython")
except:
    print("Can't connect to database")

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
