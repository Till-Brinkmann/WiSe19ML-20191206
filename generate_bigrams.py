import numpy as np

uppercaseAlphabet = []
for i in range(26):
    uppercaseAlphabet.append(chr(ord('A') + i))

bigrams = []
for i in range(26):
    for j in range(26):
        bigrams.append(uppercaseAlphabet[i] + uppercaseAlphabet[j])

print(bigrams)
#with open("bigrams.npy","w") as f:
#    np.save(f,np.array(bigrams))
