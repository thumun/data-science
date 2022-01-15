'''
Author      : Neha Thumu
Class       : CS260
Date        : 9/6/21

Description: This is the numpy tutorial file. This file goes over the basics
of numpy- array initialization and manipulation (slicing/indexing,
filling in numbers, getting dimensins, concatenation, and operations).
'''

# Some examples below are from Numpy's Quickstart tutorial:
# https://numpy.org/doc/stable/user/quickstart.html

import numpy as np
import random
import sys

################################################################################
# MAIN
################################################################################

def main():
    # NOTE: make sure to run the code frequently and analyze all output before
    # doing the TODO sections

    print("Array Initialization\n")

    # arrays of zeros, 1D array/vector
    ex_array_1d = np.zeros((5))
    print("1D array (of zeros)")
    print(ex_array_1d)
    print("number of dimensions:", ex_array_1d.ndim)
    print("dimensions:", ex_array_1d.shape, "\n")

    # fill with random numbers
    for i in range(ex_array_1d.shape[0]):
        ex_array_1d[i] = random.randrange(0, 101)
    print("1d array (filled with random numbers)")
    print(ex_array_1d, "\n")

    # 2-D array initialized with random numbers
    print("2D array of random numbers")
    ex_array_2d = np.random.rand(5, 4)
    print(ex_array_2d, "\n")

    ### ========== TODO 1 : START ========== ###

    # Create a 3D array of zeros with the dimensions (4,6,5)

    array_3d = np.zeros((4, 5, 6))

    # Fill the array with random values from [0, 301)

    for i in range(array_3d.shape[0]):
        for j in range(array_3d.shape[1]):
            for k in range(array_3d.shape[2]):
                array_3d[i, j, k] = random.randrange(0, 301)

    # Print out the array and its dimensions

    print("3D array of random numbers")
    print(array_3d, "\n")
    print("Dimensions of the 3D array")
    print(array_3d.ndim, "\n")

    # Create two 1D arrays, one filled with ones and one that is empty

    empty_array_1d = np.ones((5))
    full_array_1d = np.empty((5))

    # Print them out. README: Explain the output of the empty array

    print("1D array of one's")
    print(empty_array_1d, "\n")
    print("1D empty array")
    print(full_array_1d, "\n")

    ### ========== TODO 1 : END ========== ###
    #sys.exit("finish TODO 1") # comment to continue lab

    # array from a list
    fib_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    ex_array_from_list = np.array(fib_list)
    print("fibonacci list")
    print(fib_list)
    print("1d array from the list")
    print(ex_array_from_list, "\n")

    # array from a range: [start index, end index), step size
    ex_array_from_range_a = np.arange(10)
    ex_array_from_range_b = np.arange(0, 2, 0.3)
    print("1d array from a range (10)")
    print(ex_array_from_range_a)
    print("1d array from a range (0, 2, 0.3)")
    print(ex_array_from_range_b, "\n")

    print("Adding Elements\n")

    print("the original 1d array")
    print(ex_array_1d, "\n")

    # add a new element to the array (CAUTION: expensive operation!)
    ex_array_1d = np.append(ex_array_1d, 45)
    print("after appending one value (45)")
    print(ex_array_1d)

    # appending an array of elements to another array
    ex_array_1d = np.append(ex_array_1d, ex_array_from_list)
    print("array to be appended")
    print(ex_array_from_list)
    print("after appending an array")
    print(ex_array_1d, "\n")

    print("Removing Elements\n")

    # remove element at index (CAUTION: it is rarely necessary to do this!)
    ex_array_1d = np.delete(ex_array_1d, 3)
    print("after deleting element at index 3")
    print(ex_array_1d)
    indicies_to_remove = np.array([0, ex_array_1d.shape[0] - 1])
    ex_array_1d = np.delete(ex_array_1d, indicies_to_remove)
    print("after deleting the first and last element")
    print(ex_array_1d, "\n")

    print("Sorting\n")

    # sort
    ex_array_1d_sorted = np.sort(ex_array_1d)
    print("the sorted array")
    print(ex_array_1d_sorted, "\n")

    # Append, delete, and sort all return a COPY of the array with the changes
    # and do not modify the original array.

    # In general, you should avoid using append and delete as these operations
    # both slow and costly. But, its still good to be aware of them.

    print("Array Slicing\n")

    ### ========== TODO 2 : START ========== ###

    # Read the section 'Basic Slicing and Indexing' of a page from the numpy
    #documentation (https://numpy.org/doc/stable/reference/arrays.indexing.html)
    for i in range(ex_array_2d.shape[0]):
        for j in range(ex_array_2d.shape[1]):
            ex_array_2d[i][j] = random.randrange(0, 101)
    print("2d array (filled with random numbers)")
    print(ex_array_2d, "\n")

    # For the commented out examples of array slicing, write out the expected
    # output in your README.

    """
    print("ex_array_2d[2]")
    print(ex_array_2d[2], "\n")

    print("ex_array_2d[:,1]")
    print(ex_array_2d[:,1], "\n")

    print("ex_array_2d[:3,:2]")
    print(ex_array_2d[:3,:2], "\n")
    """

    # Comment the code back in and check your answer against the actual output.

    ### ========== TODO 2 : END ========== ###
    #sys.exit("finish TODO 2") # comment to continue lab

    # --------------
    # TODO 3: go through the following code and make sure it makes sense

    print("Array Concatenation\n")
    # concatenation
    print("2d array (main one in the concatenation examples) (5x4)")
    print(ex_array_2d, "\n")
    to_be_concat = np.arange(2, 10, 2)
    to_be_concat = np.reshape(to_be_concat, (1,4))
    print("array (to be concatenated to the 2d array) (1x4)")
    print(to_be_concat)
    print("After concatenation (axis=0) (6x4)")
    print(np.concatenate((ex_array_2d, to_be_concat), 0), "\n")

    # Note: the official documentation states that "the arrays must have the
    # same shape, except in the dimension corresponding to axis (the first, by
    # default)."
    #(https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html)

    # Thus the following code throws an error
    try:
        print("2d array with the above array concatenated to it (axis=1)")
        print(np.concatenate((ex_array_2d, to_be_concat), 1), "\n")
    except ValueError:
        print("Arrays must have the same shape, excluding the axis they are " +\
            "joined upon.")

    to_be_concat_2 = np.arange(5)
    to_be_concat_2 = np.reshape(to_be_concat_2, (5,1))
    print("array (to be concatenated to the 2d array) (5x1)")
    print(to_be_concat_2)
    print("After concatenation (axis=1) (5x5)")
    print(np.concatenate((ex_array_2d, to_be_concat_2), 1), "\n")

    print("Basic Operations\n")

    a = np.arange(4)
    b = np.arange(3, 11, 2)

    print("vector a")
    print(a)
    print("vector b")
    print(b, "\n")

    # Basic Operations
    # elementwise
    # +
    print("a + 2")
    print(a + 2)
    print("a + b")
    print(a + b, "\n")

    # -
    print("a - 7")
    print(a - 7)
    print("b - a")
    print(b - a, "\n")

    # **, exponents -> x^y
    print("b**2 (b^2)")
    print(b**2, "\n")

    # *, multiplication
    print("a * 0.5")
    print(a * 0.5)
    print("a * b")
    print(a * b, "\n")

if __name__ == "__main__":
    main()
