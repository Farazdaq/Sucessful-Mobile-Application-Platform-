from flask import Flask, render_template,request
from Controllers.project_step1 import projectStep1Controller
from Controllers.project_step2 import projectStep2Controller
from Controllers.login_controller import loginController
from flask_session import Session
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'smap_db'
mysql = MySQL(app)

@app.route('/' , methods=['GET', 'POST'])
def index(): 
    return render_template("index.html")

app.register_blueprint(projectStep1Controller, url_prefix="/add_project_step1") 
app.register_blueprint(projectStep2Controller, url_prefix="/add_project_step2")
app.register_blueprint(loginController, url_prefix="/login")
@app.route('/about')
def about():
    return render_template('about.html')
   
@app.route('/decpanel_view')
def decpanel_view():
    return render_template('decpanel_view.html') 

@app.route('/add_project-step1')
def add_project_step1():
    return render_template('add_project_step1.html')

@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/add_project-step3')
def add_project_step3():
    feature0 = request.args.get('passed_result0')
    feature1 = request.args.get('passed_result1')
    feature2 = request.args.get('passed_result2')
    feature3 = request.args.get('passed_result3')
    feature4 = request.args.get('passed_result4')
    feature5 = request.args.get('passed_result5')
    feature6 = request.args.get('passed_result6') 
    feature7 = request.args.get('passed_result7')
    score0 = request.args.get('passed_score0')
    score1 = request.args.get('passed_score1')
    score2 = request.args.get('passed_score2')
    score3 = request.args.get('passed_score3')
    score4 = request.args.get('passed_score4')
    score5 = request.args.get('passed_score5')
    score6 = request.args.get('passed_score6')
    score7 = request.args.get('passed_score7')
    return render_template('add_project_step3.html',featureviwed0=feature0, featureviwed1=feature1, featureviwed2=feature2,  featureviwed3=feature3, featureviwed4=feature4, featureviwed5=feature5, featureviwed6=feature6,featureviwed7=feature7,scoreview0=score0,scoreview1=score1, scoreview2=score2, scoreview3=score3, scoreview4=score4, scoreview5=score5, scoreview6=score6, scoreview7=score7) 
@app.route('/add_project-step2')
def add_project_step2():
    passed_relationship = request.args.get('relationship')
    passed_describtion = request.args.get('describtion')
    return render_template('add_project_step2.html',describtion=passed_describtion,relationship=passed_relationship)

if __name__ == '__main__':
    app.run(depug=True)