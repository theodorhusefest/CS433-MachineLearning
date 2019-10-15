# -*- coding: utf-8 -*-
""" Grid Search"""

import numpy as np
import costs


def generate_w(num_intervals):
    """Generate a grid of values for w0 and w1."""
    w0 = np.linspace(-100, 200, num_intervals)
    w1 = np.linspace(-150, 150, num_intervals)
    return w0, w1


def get_best_parameters(w0, w1, losses):
    """Get the best w from the result of grid search."""
    min_row, min_col = np.unravel_index(np.argmin(losses), losses.shape)
    return losses[min_row, min_col], w0[min_row], w1[min_col]

def compute_loss(y, tx, w):
    
    """Calculate the loss.

    You can calculate the loss using mse or mae.
    
    """
    
    # return (1/len(y))*np.abs(y-np.dot(tx,w)) MAE
    
    return (1/(2*len(y)))*np.dot((y-np.dot(tx,w)).T,y-np.dot(tx,w)) # MSE


def grid_search(y, tx, w0, w1):
    """Algorithm for grid search"""
    losses = np.zeros((len(w0), len(w1)))
    # ***************************************************
    # INSERT YOUR CODE HERE
    for i in range(len(w0)):
        for j in range(len(w1)):
            losses[i,j] = compute_loss(y, tx, [w0[i], w1[j]])
    
    # TODO: compute loss for each combination of w0 and w1.
    # ***************************************************
    return losses
