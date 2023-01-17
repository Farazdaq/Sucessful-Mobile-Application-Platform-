from symtable import Class
from flask import Flask
from flask_mysqldb import MySQL
def db_connection():
    mysql = MySQL() 
    conn = mysql.connect
    cursor =conn.cursor()
    return cursor