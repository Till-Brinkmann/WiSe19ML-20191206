import numpy as np
from classification.preprocessing import extract_features_bigram
from classification.classifier import KnnClassifier
from intromltoolbox.plotting import plot_datapoints_with_indices

data1 = np.load("dataset2.npz")

X = np.array([extract_features_bigram(x) for x in data1["X"]]) 
Y = data1["y"]

#split 50 data elements from the dataset

testSize = 20

datasets = np.split(X,[X.shape[0]-testSize])
classes = np.split(Y,[Y.shape[0]-testSize])

trainingsdata = datasets[0]
testdata = datasets[1]

trainingclasses = classes[0]
testclasses = classes[1]

knn = KnnClassifier()

knn.learn(trainingsdata,trainingclasses)

klist = []
for k in range(0,10):
    correctCount = 0
    for i in range(0,testdata.shape[0]):
        if knn.predict(testdata[i],k) == testclasses[i]:
            correctCount += 1
    print("Right answers wih k=" + k + ": " + correctCount)
    kList.add(correctCount/testSize)

plot_datapoints_with_indices(klist)
