import numpy as np

class NaiveBayesClassifier:
    
    def __init__(self):
        
    
    def learn(self,X,Y,Xt=None,Yt=None): 
        #Pc is a dictionary mapping c to the probability P(Y=c)
        classes, occurence = np.unique(Y,return_counts=True)
        probability = []
        for i in range(occurence.size):
            probability[i] = float(occurence[i])/occurence.size
        self.Pc = zip(classes, occurence)

        #for c in self.Pc: #for every class
         #   self.Pc[c] = 

        
    
    def predict(self,x):


