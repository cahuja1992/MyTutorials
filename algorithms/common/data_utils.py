import numpy as np

def to_categorical(x, num_col = None):
    if not num_col:
        num_col = np.amax(x) + 1
    one_hot = np.zeros((x.shape[0], num_col))
    one_hot[np.arange(x.shape[0]), x] = 1
    return one_hot


def shuffle_data(X, y, seed = None):
    if seed:
        np.random.seed(seed)
    idx = np.arange(X.shape[0])
    np.random.shuffle(idx)
    return X[idx], y[idx]


def train_test_split(X, y, test_size=0.5, shuffle=True, seed=None):
    if shuffle:
        X, y = shuffle_data(X, y, seed)
    split_i = len(y) - int(len(y) // (1 / test_size))
    X_train, X_test = X[:split_i], X[split_i:]
    y_train, y_test = y[:split_i], y[split_i:]

    return X_train, X_test, y_train, y_test


def batch_iterator(X, y = None, batch_size = 128):
    num_samples = X.shape[0]
    for i in np.arange(0, num_samples, batch_size):
        begin, end = i, min(i + batch_size, num_samples)
        if y is not None:
            yield X[begin:end], y[begin:end]
        else:
            yield X[begin:end]

