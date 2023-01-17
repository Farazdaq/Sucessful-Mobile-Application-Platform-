from flask import Blueprint, render_template, request, redirect, url_for 
from Models.login_recover_model import login_data

loginController = Blueprint("login", __name__)
@loginController.route('/', methods=['GET', 'POST']) # type: ignore
def login():
     if request.method == 'POST':
      username = request.form.get('username') 
      password = request.form.get('password')
      result = login_data(username,password) 
      if result: # type: ignore
         print("Pass")
      else:
         print("not pass")
     return render_template('login.html')