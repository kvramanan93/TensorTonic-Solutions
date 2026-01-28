import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x_new , y_new = np.asarray(x),np.asarray(y)

    return np.sqrt(np.sum((x_new - y_new) ** 2))

    pass