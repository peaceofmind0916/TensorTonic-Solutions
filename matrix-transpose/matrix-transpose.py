import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A=np.array(A)
    M, N= A.shape
    new_A= np.zeros((N,M),dtype=A.dtype)
    for i in range(M):
        for j in range(N):
            new_A[j][i]= A[i][j]
    pass
    return new_A
