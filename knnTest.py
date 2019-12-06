import numpy as np
from classification.preprocessing import extract_features_bigram
from classification.classifier import KnnClassifier
from intromltoolbox.plotting import plot_datapoints_with_indices

data1 = np.load("dataset2.npz")

X = np.array([extract_features_bigram(x) for x in data1["X"]]) 
Y = data1["y"]

#split 50 data elements from the dataset

shuffled = np.shuffle(np.array([(X[i],Y[i]) for i in range(X.shape[0])]))
X = np.array([shuffled[0][i] for i in range(X.shape[0])])
Y = np.array([shuffled[1][i] for i in range(Y.shape[0])])

testsize = 20

datasets = np.split(X,[X.shape[0]-testSize])
classes = np.split(Y,[Y.shape[0]-testSize])

trainingsdata = datasets[0]
testdata = datasets[1]

trainingclasses = classes[0]
testclasses = classes[1]

knn = KnnClassifier()

knn.fit(trainingsdata,trainingclasses)

klist = []
for k in range(0,10):
    correctCount = 0
    for i in range(0,testdata.shape[0]):
        if knn.predict(testdata[i],k) == testclasses[i]:
            correctCount += 1
    print("Right answers wih k=" + str(k) + ": " + str(correctCount))
    #klist.append(correctCount/testSize)

#plot_datapoints_with_indices(klist)
