import numpy as np
from algorithms.classification.base import Classification
from algorithms.common.distances import *

class KNN(Classification):
    def __init__(self, k = 10, distance = 'euclidean'):
        self._k = k
        self._distance_fn = distance
        self._y = None
        self._X = None

    def fit(self, X, y):
        nrows, ncols = X.shape
        self._X = X
        self._y = y
        if self._k > X.shape[0]:
            raise ValueError(f"Expected k <= num_samples, but num_samples = {nrows}, k = {self._k}")

        if self._distance_fn == 'euclidean':
            self._distance_fn = euclidean_distance

        if self._distance_fn == 'cosine':
            self._distance_fn = cosine_distance

    def predict(self, x):
        """
            O(m) + O(nlogk) + O(k) + O(labels)
        """
        
        import heapq
        # O(m) for calculating time complexity with all the points
        distances = {}
        for idx, train_x in enumerate(self._X):
            distances[idx] = self._distance_fn(train_x, x)

        # O(mlogk) for selecting k points with least distance
        labels = self._y[heapq.nsmallest(self._k, distances)]

        # O(k) for calculating frequency map and 
        # O(labels) for finding class with max frequency
        return np.bincount(labels.squeeze()).argmax()
        
