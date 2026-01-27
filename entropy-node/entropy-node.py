import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    _,count = np.unique(y,return_counts = True)
    proportion = count/count.sum()
    
    return -np.sum(proportion*np.log2(proportion))

    