import numpy as np
import plotting 
class KnnClassifier:

    def __init__(self):
        pass

    def learn(self, X, Y):
        self.Dataset = X
        self.Classes = Y

    def predict(self,x,k):
        #get the distances from c
        distances = self.getDatasetDistances(x, self.Dataset, self.Classes)
        #get k-nearest elements
        kNearestElementsList = []
        for i in range(k):
            minimumDist = 10e10
            selectedElem = None
            for distance in distances:
                if distance[0] < minimumDist:
                    minimumDist = distance[0]
                    selectedElem = distance
            kNearestElementsList.append(selectedElem)
            distances.remove(selectedElem)
        #compute the class of c
        a = {}
        for elem in kNearestElementsList:
            if(elem[1] not in a):
                a[elem[1]] = 1
            else:
                a[elem[1]] += 1

        maximalElement = 0
        selectedClass = None
        for c in a:
            if(a[c] > maximalElement):
                maximalElement = a[c]
                selectedClass = c 
        return selectedClass 
  
    def getDatasetDistances(self, x, dataset, classes):
        distances = []
        for i in range(self.Dataset.shape[0]):
            distances.append([self.computeNorm(np.subtract(x, dataset[i]),1),classes[i]])
        return distances	
 
    def computeNorm(self,Vector,Norm):
        sum = 0
        for value in Vector:
            sum += np.power(value,Norm)
        return np.power(sum,(1/Norm))
    
