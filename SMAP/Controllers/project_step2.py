from flask import Blueprint, render_template, request, redirect, url_for 
import math 
import json
from sentence_transformers import SentenceTransformer, util
from Controllers.S_C_sub_controller import SCSubController 
from Controllers.project_step1 import visovalue
projectStep2Controller = Blueprint("add_project_step2", __name__)
@projectStep2Controller.route('/', methods=['GET', 'POST'])
def add_project_step2():
    if request.method == 'POST':
        searchFeatuers = SCSubController()
        vision = visovalue()
        
        result0, result1, result2, result3, result4, result5, result6, result7,secore0, secore1, secore2, secore3, secore4, secore5, secore6, secore7  = searchFeatuers.semanticSearch(vision)
        print()
 # type: ignore        
        return redirect(url_for('add_project_step3',passed_result0 = result0, passed_result1 =result1, passed_result2 =result2, passed_result3 =  result3, passed_result4 = result4,passed_result5 = result5,passed_result6 = result6, passed_result7 = result7, passed_score0=secore0, passed_score1=secore1, passed_score2=secore2, passed_score3=secore3, passed_score4=secore4, passed_score5=secore5, passed_score6=secore6, passed_score7=secore7))
        
    return render_template('add_project_step2.html')