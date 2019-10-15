# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    feature_matrix = np.zeros([len(x), degree])

    for i in range(len(x)):
        for j in range(degree):
            feature_matrix[i][j] = x[i]**(j+1)
            
    return feature_matrix
    # polynomial basis function: TODO
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data
    # ***************************************************
    