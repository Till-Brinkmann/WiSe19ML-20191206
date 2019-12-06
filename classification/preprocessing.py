import numpy as np

ordA = ord('A')

def extract_features_bigram(x):
    if len(x) < 2:
        return np.empty;
    bigram_vector = np.zeros(26**2)
    for i in range(len(x)-1):
       bigram_vector[(ord(x[i])-ordA)*26+(ord(x[i+1])-ordA)] = 1
    return bigram_vector

#print(extract_features_bigram("ZA"))
#print(len(extract_features_bigram("AFGDJKLSDFHJKAS")))
