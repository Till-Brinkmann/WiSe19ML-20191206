import numpy as np

class NaiveBayesClassifier:
    
    def __init__(self):
        pass
    
    def fit(self,X,Y):
        #Pc is a dictionary mapping c to the probability P(Y=c)
        classes, occurence = np.unique(Y,return_counts=True)
        self.classes = classes
        probability = []
        #print("Occurence: " + str(occurence))
        for i in range(occurence.shape[0]):
            probability.append(float(occurence[i])/Y.size)
        self.Pc = dict(zip(classes, probability))
        #print(self.Pc)
        self.xAvg = {}
        for c in classes:
            #print(np.sum(np.array([X[i] for i in np.where(Y==c)[0]]), axis=0))
            #print("I shape: " + str(indices[0].shape))
            self.xAvg[c] = np.divide(np.sum(np.array([X[i] for i in np.where(Y==c)[0]]), axis=0),np.array([X.shape[1]]*X.shape[1]))
            self.xAvg[c] = np.vectorize(lambda x : 1 if x > 0.5 else 0)(self.xAvg[c])
            print(self.xAvg[c])
            #self.xAvg = np.array([(1 if (xiSum/self.XwhereYisc[c]) > 0.5 else 0) for xi in np.sum(self.XwhereYisc)])

    def predict(self,x):
       probability = {}
       for c in self.classes:
           probability[c] = 1 * self.Pc[c]




class KnnClassifier:

    def __init__(self):
        pass

    def fit(self, X, Y):
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


