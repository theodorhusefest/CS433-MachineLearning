# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""

    feature_matrix = np.ones([len(x), degree])
    
    for deg in range(1, degree+1):
        feature_matrix = np.c_[feature_matrix, np.power(x, deg)]
    
    return feature_matrix