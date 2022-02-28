# Necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Libraries for creating and assessing machine learning classifiers
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# combinatorics
from itertools import product, combinations
# clear display
from IPython import display
# access to math.log2
import math
# random number generator
import random as rnd
import string

from DiscreteFactors import Factor
from Graph import Graph
from BayesNet import BayesNet

### This helper function converts a number between 0 and x*y into an (x,y) coordinate
def int_to_coord(pos, size_y):
    """
    argument 
    `pos`, a position expressed as an integer number between 0 and image's size_x * size_y
    `size_y`, number of columns of the image matrix
    
    Returns pos converted into a (x, y) coordinate
    """
    return int(pos / size_y), pos % size_y

# This helper function returns a list with the neighbours of a (x, y) pixel respecting the image limits
def neighbours(x, y, size_x, size_y):
    """
    argument 
    `x, y`, pixel coordinate
    `size_x, size_y`, image size
    
    Returns a list with valid (x, y) neighbours
    """
    
    neighbours = list()
    if x > 0:
        neighbours.append((x-1, y))
    if x < size_x - 1:
        neighbours.append((x+1, y))
    if y > 0:
        neighbours.append((x, y-1))
    if y < size_y - 1:
        neighbours.append((x, y+1))
    return neighbours

# This helper function defines energy between two data points
def energy_point(x, y):
    """
    argument 
    `x, y`, pixel color [0,255] range

    Returns the absolute difference between x and y. Other measures of dissimilarity may also work such as (x - y)**2
    """    
    return abs(x - y)
    
# This helper function plots the results every 10 iterations so we can see the convergence
def plot_results(it, image_x, image_y, energies, max_iter):
    """
    argument 
    `it`, current iteraction
    `image_x`, filtered image
    `image_y`, observed image
    `energies`, list of energy values computed for each iteration
    `max_iter`, maximum number of iterations
    """    
    
    (size_x, size_y) = image_y.shape
    energy = sum([energy_point(image_x[x][y], image_y[x][y]) for x in range(size_x) for y in range(size_y)])
    energy += sum([energy_point(image_x[x][y], image_x[x+1][y]) for x in range(size_x-1) for y in range(size_y)])
    energy += sum([energy_point(image_x[x][y], image_x[x][y+1]) for x in range(size_x) for y in range(size_y-1)])
    energies.append(energy)               
    display.clear_output(wait=True)
    print("Iteration:")
    print(it)
    plt.figure(figsize=(10, 10))
    plt.subplot(2, 1, 1)
    axes = plt.gca()
    axes.set_xlim([0, max_iter])
    axes.set_ylim([min(max(energies)/2,min(energies)), max(energies)])
    plt.plot(energies, 'ro')
    plt.subplot(2, 2, 3)
    plt.imshow(image_y, cmap='gray') 
    plt.subplot(2, 2, 4)    
    plt.imshow(image_x, cmap='gray') 
    plt.show()

def stochastic_search(image_y, max_iter=101, eps=.001, step_stdev=.05):
    """
    argument 
    `image_y`, observed image
    `max_iter`, maximum number of iteractions
    `eps`, probability of accepting a higher energy change
    `step_stdev`, standard deviation. Changes are randon numbers from a Gaussian distribuion N(0, step_stdev)
    """
    
    # List of energy values for each iteration. Initialise with empty list
    energies = []
    # Image size expressed as number of rows and columns
    (size_x, size_y) = image_y.shape
    # Image size expressed as number of pixels
    size = size_x * size_y
    # Let's use image_y as starting point for image_x. It will be faster than if we start with a random assignment
    image_x = image_y.copy()

    for it in range(max_iter):
        # order has the indexes of all pixels in the image
        order = list(range(size))
        # Let's shuffle these indexes so each pass will use a different order
        rnd.shuffle(order)
        for o in order:
            # Use the int_to_coord helper function to convert o into an (x,y) coordinate
            (x, y) = int_to_coord(o, size_y)
            # Use energy_point to initialise energy_prev with the energy between image_x and image_y in the same pixel position
            energy_prev = energy_point(image_x[x][y], image_y[x][y])
            # step defines the change in image_x pixel. We will use a random value from a normal distribution with mean zero and a small standard deviation
            step = rnd.gauss(0, step_stdev)
            # Use energy_point to initialise energy_post with the energy between image_x +step and image_y in the same pixel position
            energy_post = energy_point(image_x[x][y] + step, image_y[x][y])
            # Use neighbours to find all valid neighbours of the current pixel
            for (i, j) in neighbours(x, y, size_x, size_y):
                # Use energy_point to update energy_prev for each neighbour pixel
                energy_prev += energy_point(image_x[x][y], image_x[i][j])
                # Use energy_point to update energy_post for each neighbour pixel
                energy_post += energy_point(image_x[x][y] + step, image_x[i][j])
            # Update image_x if the change led to an decrease of energy    
            if energy_post < energy_prev or rnd.random() < eps:
                image_x[x][y] += step
        # Call plot_results to show the progress so far
        plot_results(it, image_x, image_y, energies, max_iter)