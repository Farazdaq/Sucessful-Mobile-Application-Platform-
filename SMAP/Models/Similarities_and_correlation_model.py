import csv
class Similarities_correlation:
    
        #loading the featuers file.csv in the reade mode
     file = open("Models/dataset.csv", "r")
     reader = csv.reader(file)
     #create a list to store the file colunmms
     collected = []
     #store the columms in a list 
     for row in reader:
        collected.append(row[0]) 
        