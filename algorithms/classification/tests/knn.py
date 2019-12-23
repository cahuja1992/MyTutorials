from algorithms.classification.knn import KNN
import numpy as np

X = np.array([
    [0.1, 0.1],
    [0.2, 0.1],
    [0.3, 0.1],
    [0.1, 0.2],
    [0.1, 0.9],
])

y = np.array([
    [1],
    [1],
    [0],
    [1]
])

model = KNN(2)
model.fit(X, y)
output = model.predict([0.1, 0.0])
print(output)