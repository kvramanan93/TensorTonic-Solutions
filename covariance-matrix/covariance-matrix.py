import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    x = np.asarray(X)
    dim = x.ndim
    N = x.shape[0]
    
    if dim != 2 or N < 2:
        return None
    
    center = x - np.mean(x,axis=0)
    return (1/(N-1))*(center.T @ center)

    pass