import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    m,n = len(A),len(A[0])
    A_T = np.zeros((n,m),dtype = int)

    for i in range(m):
        for j in range(n):
            A_T[j][i] = A[i][j]
    return A_T
    
    
    pass
