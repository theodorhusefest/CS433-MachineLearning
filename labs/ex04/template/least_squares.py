# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares solution."""
    
    w_star = np.linalg.solve(np.dot(tx.T, tx), np.dot(tx.T, y))
    mse = (1/len(y))*np.transpose(y - tx@w_star).dot((y - tx@w_star))
    
    return w_star
    