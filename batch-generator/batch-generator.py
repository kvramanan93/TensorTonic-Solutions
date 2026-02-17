import numpy as np

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    """
    Randomly shuffle a dataset and yield mini-batches (X_batch, y_batch).
    """
    X = np.asarray(X)
    y = np.asarray(y)
    n_samples = len(X)
    index_array = np.arange(n_samples) #Creates an index of length n_samples and elements from 0 to n_samples

    
    #Shufling index as original array not to be modified in-place
    if rng == None:
        np.random.shuffle(index_array)
    else:
        rng.shuffle(index_array)

    #Calculating Number of batches to yield
    n_batches = n_samples//batch_size
    if not drop_last and n_samples % batch_size != 0:
        n_batches += 1

    #Yield batch using shuffled index 
    for i in range(n_batches):
        start = i * batch_size
        end = start+batch_size
        batch_index = index_array[start:end]
        
        yield(X[batch_index],y[batch_index])
        
    
    # Write code here
    pass