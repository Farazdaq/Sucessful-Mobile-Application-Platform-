from flask import Blueprint, render_template, request,redirect, url_for 
import math

from sentence_transformers import SentenceTransformer, util
from Controllers.S_C_sub_controller import SCSubController 
projectStep1Controller = Blueprint("add_project_step1", __name__)
@projectStep1Controller.route('/', methods=['GET', 'POST'])
 
def add_project_step1():
    if request.method == 'POST':
        global vision
        goal = request.form.get('goal') 
        vision = request.form.get('vision')
        category = request.form.get('category-list')
        calucluateRerlationsip = SCSubController()
        cosineRelaltionScores= calucluateRerlationsip.ConverTextIntoNumbers(goal,vision)
        if cosineRelaltionScores > 0.9000:
         return redirect(url_for('add_project_step2',relationship= str(round(cosineRelaltionScores, 2)), describtion="Very Strong"))
        elif cosineRelaltionScores > 0.7000 and cosineRelaltionScores < 0.9000 :
            return redirect(url_for('add_project_step2',relationship= str(round(cosineRelaltionScores, 2)), describtion="Strong"))
        elif cosineRelaltionScores > 0.5000 and cosineRelaltionScores < 0.7000:
            return redirect(url_for('add_project_step2',relationship= str(round(cosineRelaltionScores, 2)), describtion="Good"))
        elif cosineRelaltionScores == 0.5000 and  cosineRelaltionScores < 0.7000:
            return redirect(url_for('add_project_step2',relationship= str(round(cosineRelaltionScores, 2)), describtion="Neutral"))
        elif  cosineRelaltionScores < 0.5000:
          return redirect(url_for('add_project_step2',relationship= str(round(cosineRelaltionScores, 2)), describtion="Bad"))
        else:
           pass
    return render_template('add_project_step1.html')
    
def visovalue(): 
      return vision