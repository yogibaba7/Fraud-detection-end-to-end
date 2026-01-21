import numpy as np

def log_abs_transform(x):
    return np.log1p(np.abs(x))