import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    x = np.asarray(X)
    N = x.shape[0]
    if  N < 2 or x.ndim <= 1:
        return None
    

    centered = x - np.mean(x,axis=0)
    return (1/(N-1))* centered.T @ centered
    pass