''' Starter code for you to complete Q5 of COMP9727 22T2 Assignment 1.
    No other lines should be altered, except for the indicated area.

    You should firstly extract `q5.csv` from `a1.zip`, and put `q5.csv`
    under the same directory with this file.

    It is your responsibility to ensure that this program can be run on
    any CSE machine's default environment in order to be awarded marks;
    otherwise, you will receive zero.
'''

import numpy as np
import random
import time
import pdb
import unittest
from PIL import Image

# Finds the L1 distance (i.e. Manhattan distance) between two vectors
# u and v are 1-dimensional np.array objects
# TODO: Implement this 
def l1(u, v):
    raise NotImplementedError

# Loads the data into a np array, where each row corresponds to
# an image patch -- this step is sort of slow.
# Each row in the data is an image, and there are 400 columns.
def load_data(filename):
    return np.genfromtxt(filename, delimiter=',')

# Creates a hash function from a list of dimensions and thresholds.
def create_function(dimensions, thresholds):
    def f(v):
        boolarray = [v[dimensions[i]] >= thresholds[i] for i in range(len(dimensions))]
        return "".join(map(str, map(int, boolarray)))
    return f

# Creates the LSH functions (functions that compute N K-bit hash keys).
# Each function selects k dimensions (i.e. column indices of the image matrix)
# at random, and then chooses a random threshold for each dimension, between 0 and
# 255.  For any image, if its value on a given dimension is greater than or equal to
# the randomly chosen threshold, we set that bit to 1.  Each hash function returns
# a length-k bit string of the form "0101010001101001...", and the N hash functions 
# will produce N such bit strings for each image.
def create_functions(k, N, num_dimensions=400, min_threshold=0, max_threshold=255):
    functions = []
    for i in range(N):
        dimensions = np.random.randint(low = 0, 
                                   high = num_dimensions,
                                   size = k)
        thresholds = np.random.randint(low = min_threshold, 
                                   high = max_threshold + 1, 
                                   size = k)

        functions.append(create_function(dimensions, thresholds))
    return functions

# Hashes an individual vector (i.e. image).  This produces an array with N
# entries, where each entry is a string of k bits.
def hash_vector(functions, v):
    return np.array([f(v) for f in functions])

# TODO: Hashes the data in A, where each row is a datapoint, using the N
# functions in "functions." You can use the hash_vector function to do this task.
def hash_data(functions, A):
    return NotImplementedError
# Retrieve all of the points that hash to one of the same buckets 
# as the query point.  Do not do any random sampling (unlike what the first
# part of this problem prescribes).
# Don't retrieve a point if it is the same point as the query point.
def get_candidates(hashed_A, hashed_point, query_index):
    return filter(lambda i: i != query_index and \
        any(hashed_point == hashed_A[i]), range(len(hashed_A)))

# Sets up the LSH.  You should try to call this function as few times as 
# possible, since it is expensive.
# A: The dataset in which each row is an image patch.
# Return the LSH functions and hashed data structure.
def lsh_setup(A, k = 24, N = 10):
    functions = create_functions(k = k, N = N)
    hashed_A = hash_data(functions, A)
    return (functions, hashed_A)

# TODO: Run the entire LSH algorithm by using the pre-defined hash_vector
# and get_candidates functions. It should return a list of best neighbours.
def lsh_search(A, hashed_A, functions, query_index, num_neighbors = 10):
    raise NotImplementedError

# Plots images at the specified rows and saves them each to files.
def plot(A, row_nums, base_filename):
    for row_num in row_nums:
        patch = np.reshape(A[row_num, :], [20, 20])
        im = Image.fromarray(patch)
        if im.mode != 'RGB':
            im = im.convert('RGB')
        im.save(base_filename + "-" + str(row_num) + ".png")

# Finds the nearest neighbors to a given vector, using linear search.
def linear_search(A, query_index, num_neighbors):
    raise NotImplementedError #TODO

# TODO: Write a function that computes the error measure

# TODO: Solve Problem d
def problemd():
    raise NotImplementedError

#### TESTS #####

class TestLSH(unittest.TestCase):
    def test_l1(self):
        u = np.array([1, 2, 3, 4])
        v = np.array([2, 3, 2, 3])
        self.assertEqual(l1(u, v), 4)

    def test_hash_data(self):
        f1 = lambda v: sum(v)
        f2 = lambda v: sum([x * x for x in v])
        A = np.array([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(f1(A[0,:]), 6)
        self.assertEqual(f2(A[0,:]), 14)

        functions = [f1, f2]
        self.assertTrue(np.array_equal(hash_vector(functions, A[0, :]), np.array([6, 14])))
        self.assertTrue(np.array_equal(hash_data(functions, A), np.array([[6, 14], [15, 77]])))

    ### TODO: Write your tests here (they won't be graded, 
    ### but you may find them helpful)


if __name__ == '__main__':
#    unittest.main() ### TODO: Uncomment this to run tests
    problemd()
