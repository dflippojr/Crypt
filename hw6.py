import numpy as np
import itertools

ciphertext = open("HW6/cle.txt", "r").read()

# create numpy array to hold ciphertext
arr = np.empty((11, 42), dtype='U1')

count = 0
for i in range(42):
    for j in range(11):
        arr[j][i] = ciphertext[count]
        count += 1


for perm in itertools.permutations(range(arr.shape[1])):
    print(arr[:, perm])
