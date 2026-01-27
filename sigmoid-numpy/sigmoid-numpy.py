import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    a = np.asarray(x,dtype=float)

    return (1/(1+np.exp(-a)))