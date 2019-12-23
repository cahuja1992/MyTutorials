import numpy as np

def euclidean_distance(u, v):
    if not isinstance(u, np.ndarray):
        u = np.asarray(u)
    
    if not isinstance(v, np.ndarray):
        v = np.asarray(v)
    
    return np.sqrt(np.sum((u - v) ** 2))

def cosine_distance(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))