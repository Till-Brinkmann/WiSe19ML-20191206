import numpy as np
from classification.preprocessing import extract_features_bigram
from classification.classifier import NaiveBayesClassifier

data1 = np.load("dataset1.npz")

X = np.array([extract_features_bigram(x) for x in data1["X"]]) 
print("size X: " + str(X.shape))
print("size y: " + str(data1["y"].shape))
#print(X)


nb = NaiveBayesClassifier()

nb.fit(X,data1["y"])
