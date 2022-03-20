import csv
from csv import writer
import numpy as np
import re

def userDataGetter(dataForAnalysis):
    print("userDataGetter function")
    userFile = "/home/mattei/Projects/dataScout/server/testData/testdata1.csv"

    with open(userFile, newline='') as csvfile:
        userData = csv.reader(csvfile, delimiter=' ', quotechar='|')
        #  data=[tuple(line) for line in csv.reader(csvfile)]
        
       # print(data)
        #for row in userData:
        #    dataForAnalysis.append(row)
        #    print(', '.join(row))
        #print(dataForAnalysis)
        return dataForAnalysis


def graphSelector(dataForAnalysis, graphChoice):
    print('\n' + "Finding the most suitable graph for your data…")
    x = len(dataForAnalysis[0])
    print(x)
    #Pythons alternative for "switchcase"
    def graphOptions(x, graphType):
        match x:
            # For 3 values
            case 1:
                graphType= 'line'
                return graphType
            case _:
                graphType= 'bubble'
                return graphType

    graphChoice = graphOptions(x, graphChoice)
    print("Graph style: [" + graphChoice + "], has been selected \n")
    return graphChoice

def dataFormatter(dataForAnalysis, graphChoice):
    print("Formatting your data…")
    
    
    
    #data = dataForAnalysis
    #dataList = np.array(data)
    #dataTuple = [tuple(x) for x in dataList.tolist()]
    #print (dataTuple)

#    labels = []
 #   values = []
  #  for row in dataTuple:
   #     labels.append(row)
    #    values.append(row)
    
    #print(labels)
    #print(values)