import numpy as np

data1 = np.load("dataset1.npz")
data2 = np.load("dataset2.npz")

classes, occurence = np.unique(data1["y"],return_counts=True)
data1_classes = dict(zip(classes,occurence))

print("dataset1")
print("class distribution:" + str(data1_classes))
print("")


classes, occurence = np.unique(data2["y"],return_counts=True)
data2_classes = dict(zip(classes,occurence))


print("dataset 2")
print("class distribution:" + str(data2_classes))


