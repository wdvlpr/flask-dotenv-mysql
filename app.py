#Autor: Fabio Camara

#pip install flask
from flask import Flask, jsonify

#pip install python-dotenv
import os
from dotenv import load_dotenv
load_dotenv('.env')

#pip install flask_mysqldb
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ.get("HOST")
app.config['MYSQL_USER'] = os.environ.get("USER")
app.config['MYSQL_PASSWORD'] = os.environ.get("PASSWORD")
app.config['MYSQL_DB'] = os.environ.get("DATABASE")

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM contatos")
    result = cursor.fetchall()
    cursor.close()
    return jsonify(result)

@app.route('/contato/<id>')
def contato(id):
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM contatos WHERE idcontato = %s"
    cursor.execute(sql, id)
    result = cursor.fetchall()
    cursor.close()
    return jsonify(result)