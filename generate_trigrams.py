uppercaseAlphabet = []
for i in range(26):
    uppercaseAlphabet.append(chr(ord('A') + i))

trigrams = []
for i in range(26):
    for j in range(26):
        for k in range(26):
            trigrams.append(uppercaseAlphabet[i] + uppercaseAlphabet[j] + uppercaseAlphabet[k])

print(trigrams)
