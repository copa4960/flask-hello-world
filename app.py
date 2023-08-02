import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def hello_word():
    conn = psycopg2.connect("postgres://maxdata_user:37E7NQuXm9T45FSPJbvyI9SQ1jOk8z1a@dpg-cj4pptgeba7s73a91e80-a/maxdata")
    conn.close()
    return 'database connection successful'