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


sum_string_length = 0.

for x in data1["X"]:
    sum_string_length += len(x)

sum_string_length /= data1["X"].shape[0]
print("Average string length data1: " + str(sum_string_length))


sum_string_length = 0.
for x in data2["X"]:
    sum_string_length += len(x)

sum_string_length /= data2["X"].shape[0]
print("Average string length data1: " + str(sum_string_length))
