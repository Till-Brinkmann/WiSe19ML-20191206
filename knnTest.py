import numpy as np
from classification.preprocessing import extract_features_bigram
from classification.classifier import KnnClassifier
data1 = np.load("dataset2.npz")

X = np.array([extract_features_bigram(x) for x in data1["X"]]) 
Y = data1["y"]

print(X)
print(Y)

#split 50 data elements from the dataset

shuffled = np.array([(X[i],Y[i]) for i in range(X.shape[0])])
np.random.shuffle(shuffled)
X = np.array([shuffled[i][0] for i in range(X.shape[0])])
Y = np.array([shuffled[i][1] for i in range(Y.shape[0])])

print(X)
print(Y)

testSize = 20

datasets = np.split(X,[X.shape[0]-testSize])
classes = np.split(Y,[Y.shape[0]-testSize])

trainingsdata = datasets[0]
testdata = datasets[1]

trainingclasses = classes[0]
testclasses = classes[1]

knn = KnnClassifier()

knn.learn(trainingsdata,trainingclasses)


#no experimental(für standart result)
klist = []
for k in range(1,5):
    correctCount = 0
    for i in range(0,testdata.shape[0]):
        if knn.predict(testdata[i],k,False) == testclasses[i]:
            correctCount += 1
    print("Right answers wih k=" + str(k) + ": " + str(correctCount))
    print("Probability: " + (correctCount/testSize))
    #klist.append(correctCount/testSize)

#experimental(für further improvments)
klist = []
for k in range(1,5):
    correctCount = 0
    for i in range(0,testdata.shape[0]):
        if knn.predict(testdata[i],k,True) == testclasses[i]:
            correctCount += 1
    print("Right answers wih k=" + str(k) + ": " + str(correctCount))
    print("Probability: " + (correctCount/testSize))
    #klist.append(correctCount/testSize)

