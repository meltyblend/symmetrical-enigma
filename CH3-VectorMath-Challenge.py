"""
Being able to manipulate vectors is a cornerstone technique for deep learning. See if you can
write functions that perform the following operations:
• def elementwise_multiplication(vec_a, vec_b)
• def elementwise_addition(vec_a, vec_b)
• def vector_sum(vec_a)
• def vector_average(vec_a)
Then, see if you can use two of these methods to perform a dot product!
"""

# aren chavez 5/ 24 / 2024

import numpy as np

vec_a = [1, 2, 3, 5]
vec_b = [8, 13, 21, 34]

# dot product notes in terms of neural network applications

# dot products or weighted sums are important because they give you the similarities between two vectors
# think orthogonality, linear independence, or used as a tool to measure
# how closely two vectors align to a specific point

#dot products can also be related to logical properties like AND
# example
# a = [ 0, 1, 0, 1]
# b = [ 1, 0, 1, 0]
# a ^ b logically = 0 so it fails the AND test

# there is also partial ANDing and negative weights
# ex : d = [.5, 0,.5, 0]
#      e = [-1, 1, 0, 0]
# negative weights insinuate a logical NOT column one will then be NOT col 1

# neural networks give higher scores to the inputs based on how similar they are to the weights
# Note: You cannot shuffle weights they have specific positions that they need to be in



def vector_multiplication(vec_a, vec_b): # multiplying two vectors
    assert len(vec_a) == len(vec_b)
    output = 0

    for i in range(len(vec_a)):
        output += vec_a[i] * vec_b[i] # the dot product of vec_a and b
    return output

def vector_addition(vec_a, vec_b): # adding two vectors
    assert len(vec_a) == len(vec_b)
    vec_c = [] # resultant vector to store added components of a and b

    for i in range(len(vec_a)):
        vec_c.append(vec_a[i] + vec_b[i])
    return vec_c

def vector_sum(vec_a): # func. that sums all compononets of a vector
    if(len(vec_a) > 0):
        result = 0
        for i in range(len(vec_a)):
            result += vec_a[i]
        return result
    print("vector a is empty")

def vector_average(vec_a): # function that takes the average of a single vector
    if(len(vec_a) > 0):
        result = 0
        for i in range(len(vec_a)):
            result += vec_a[i]
        return result / len(vec_a)
    print("vector a is empty")


print("vector a * vector b =", vector_multiplication(vec_a, vec_b))
print("vector a + vector b =", vector_addition(vec_a, vec_b))
print("sum of vector a =", vector_sum(vec_a))
print("average of vector a =", vector_average(vec_a))