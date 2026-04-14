import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x_new= np.array(x)
    z=1+np.exp(-x_new)
    z_new=1/z
    return z_new
    pass