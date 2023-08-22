from sklearn import preprocessing
import numpy as np
import sys
import random

x_array = [random.randint(15, 15272) for _ in range(300)]

normalized_arr = preprocessing.normalize([x_array])
normalized_arr = [round(i*1000) for i in normalized_arr[0]]
print(max(x_array))
print(min(x_array))
with open("scores.txt", 'w') as f:
    sys.stdout = f
    for i in range(299):
        print(f"{x_array[i]} --> {normalized_arr[i]}")

