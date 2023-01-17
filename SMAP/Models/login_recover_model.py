from flask import Blueprint, render_template, request, redirect, url_for 
from Models.dbconnection import db_connection
def login_data(username, password):
   databasecinnection = db_connection() 
   databasecinnection.execute('SELECT * FROM account WHERE first_name = % s AND passward = % s', (username, password))
   databasecinnection.fetchone()
   mydata=databasecinnection.close()
   return mydata
   
       