# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np


def ridge_regression(y, tx, lambda_):
    """implement ridge regression."""
    aI = 2 * tx.shape[0] * lambda_ * np.identity(tx.shape[1])
    a = tx.T.dot(tx) + aI
    b = tx.T.dot(y)
    w_ridge = np.linalg.solve(a, b)
    loss_ridge = (1/len(y))*np.transpose(y - tx@w_ridge).dot((y - tx@w_ridge))
    return loss_ridge, w_ridge
