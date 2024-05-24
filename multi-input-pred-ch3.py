#grokking deep learning chapter 3

#making a prediction neural network with multi inputs

# aren chavez 5/ 24/ 2024

import numpy as np

weights = [0.1, 0.2, 0]

def w_sum(a, b):
    assert(len(a) == len(b)) # ensuring vectors a and b are the same length
    output = 0 #intializing the output var to 0

    for i in range(len(a)):
        output += a[i] * b[i] #dot product of vector a and b
    return output

def neural_network(input, weights):
    pred = w_sum(input, weights)
    return pred

# our data set

toes = [8.5, 9.5, 9.9, 9.0] #number of players toes
wl_rec = [0.65, 0.8, 0.8, 0.9] #win loss record percent
nfans = [1.2, 1.3, 0.5, 1.0] # number of fans in the millions

# our input takes index 0 from each component of our data set a
input = [toes[0], wl_rec[0], nfans[0]]

pred = neural_network(input, weights)
print(pred)