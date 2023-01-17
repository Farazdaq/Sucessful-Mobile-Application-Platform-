from flask import Flask, render_template,request
from sentence_transformers import SentenceTransformer, util
from Models.Similarities_and_correlation_model import Similarities_correlation
import math
import torch
import csv
import numpy as np

#The class S&C Sub-controler to conver the texts into embeddings 
# find the semantic relationship between the texts 
#doing the semantic search 
class SCSubController:
  
    
  def ConverTextIntoNumbers(self,firstText, secondText):
        #load the embedding coverting model
      model = SentenceTransformer('all-MiniLM-L6-v2')
        #encode the the text 
      embeddingsFirstText = model.encode(firstText,convert_to_tensor=True)
      embeddingsSecondText = model.encode(secondText,convert_to_tensor=True)
        #calculate the cosin relationship 
      cosineRelaltionScores = util.cos_sim(embeddingsFirstText, embeddingsSecondText)
        #conver the output into float number 
      relationshipResult = cosineRelaltionScores.item()
      return relationshipResult

 #----------------------------------------------------------------------------------------------       
  def semanticSearch(self,queriesList):
     
    SimilaritiesCorrelation = Similarities_correlation()
    featuersText = SimilaritiesCorrelation.collected
     
     #load the embedding coverting model
    model = SentenceTransformer('all-MiniLM-L6-v2')
     #encode the the text 
    embeddingsQueriesList = model.encode(queriesList,convert_to_tensor=True)
     #defining for the system to search for the 8 top featuers 
    topFeatuers = min(8, len(featuersText))
    for query in featuersText:
       embeddingsFeatuersText= model.encode(featuersText,convert_to_tensor=True)
       # We use cosine-similarity and torch.topk to find the highest 5 scores
       cos_scores = util.cos_sim(embeddingsQueriesList, embeddingsFeatuersText)[0]
       topFeatuers = torch.topk(cos_scores, k=topFeatuers)
       
        #for score, idx in zip(topFeatuers[0], topFeatuers[1]):
        #featuersText[idx] + "(Score: {:.4f})".format(score)
       result0=featuersText[0] 
       result1=featuersText[1]  
       result2=featuersText[2] 
       result3=featuersText[3] 
       result4=featuersText[4] 
       result5=featuersText[5] 
       result6=featuersText[6] 
       result7=featuersText[7] 
       score0="(Score: {:.4f})".format(cos_scores[0])
       score1="(Score: {:.4f})".format(cos_scores[1])
       score2="(Score: {:.4f})".format(cos_scores[2])
       score3="(Score: {:.4f})".format(cos_scores[3])
       score4="(Score: {:.4f})".format(cos_scores[4])
       score5="(Score: {:.4f})".format(cos_scores[5])
       score6="(Score: {:.4f})".format(cos_scores[6])
       score7="(Score: {:.4f})".format(cos_scores[7])
       return result0,result1, result2,result3,result4,result5,result6,result7, score0, score1, score2, score3, score4, score5, score6, score7