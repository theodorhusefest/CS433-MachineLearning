# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""


import numpy as np


def split_data(x, y, ratio, seed=1):
    """
    split the dataset based on the split ratio. If ratio is 0.8 
    you will have 80% of your data set dedicated to training 
    and the rest dedicated to testing
    """
    # set seed
    np.random.seed(seed)
    # ***************************************************
    # INSERT YOUR CODE HERE
    # split the data based on the given ratio: TODO
    num_rows = len(y)
    indicies = np.random.permutation(num_rows)
    split = int(np.floor(num_rows*ratio))
    ind_tr = indicies[: split]
    ind_te = indicies[split :]
    y_tr = y[ind_tr]
    y_te = y[ind_te]
    x_tr = x[ind_tr]
    x_te = x[ind_te]
    return y_tr, x_tr, y_te, x_te