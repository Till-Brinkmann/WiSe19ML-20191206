import numpy as np

class NaiveBayesClassifier:
    
    def __init__(self):
        pass
    
    def fit(self,X,Y):
        #Pc is a dictionary mapping c to the probability P(Y=c)
        classes, occurence = np.unique(Y,return_counts=True)
        probability = []
        for i in range(occurence.size):
            probability.append(float(occurence[i])/occurence.size)
        self.Pc = dict(zip(classes, probability))
        
        self.XwhereYisc = {}
        for c in classes:
            self.XwhereYisc[c] = [X[i] for i in np.where(Y==c)]
        print(str(self.XwhereYisc))
         
    def predict(self,x):
        pass


