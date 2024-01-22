from flask import Flask, render_template, request, redirect, url_for, flash, g, jsonify, get_flashed_messages, json
from werkzeug.utils import secure_filename
import os
import sqlite3
from mapper.db import create_db
from mapper.insert import insert_gpx

urls = {1: 'https://i.ibb.co/PtFTSRy/output-01.jpg',
    2: 'https://i.ibb.co/sgBRjVv/output-02.jpg',
    3: 'https://i.ibb.co/FbrBQ3H/output-03.jpg',
    4: 'https://i.ibb.co/zJNXLNf/output-04.jpg',
    5: 'https://i.ibb.co/Y0PDZdJ/output-05.jpg',
    6: 'https://i.ibb.co/CPR6qJZ/output-07.jpg',
    7: 'https://i.ibb.co/cLJd61X/output-06.jpg',
    8: 'https://i.ibb.co/zmS1r6v/output-08.jpg',
    9: 'https://i.ibb.co/PrtpV50/output-09.jpg',
    10: 'https://i.ibb.co/yddVKs4/output-10.jpg',
    11: 'https://i.ibb.co/NSfcpyF/output-11.jpg',
    12: 'https://i.ibb.co/k8VS1CV/output-12.jpg',
    13: 'https://i.ibb.co/1mKC857/output-13.jpg',
    14: 'https://i.ibb.co/YfYhxcV/output-14.jpg',
    15: 'https://i.ibb.co/RvhxwFz/output-15.jpg',
    16: 'https://i.ibb.co/LPhW6Gt/output-16.jpg',
    17: 'https://i.ibb.co/pyCZLT6/output-17.jpg',
    18: 'https://i.ibb.co/BjJTkQn/output-18.jpg',
    19: 'https://i.ibb.co/g72dWNt/output-19.jpg',
    20: 'https://i.ibb.co/r446xP7/output-20.jpg',
    21: 'https://i.ibb.co/kJBW6BQ/output-21.jpg',}


app = Flask(__name__)

app.secret_key = 'ishouldreallychangethis'

create_db()

def connect_db():
    sql = sqlite3.connect('./sqlite/gpx.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def home():
    return render_template('home.html', urls = urls)

@app.route('/linkstreetview', methods=['GET', 'POST'])
def linkstreetview():
    data = request.get_json()
    result = data
    return jsonify(result=result)






    




