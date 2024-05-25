#aren chavez 5/ 25 / 2024
# neural network predictions with multiple outputs using a single input
#grokking ch3 pg. 36

import numpy as np


# i[0] = hurt, i[1] = win, i[2] = sad
weights = np.array([0.3, 0.2, 0.9])

# defining scalar multiplication function
def scalar_mul(scalar, vector):
    output = np.zeros(len(vector))
    assert(len(output) == len(vector))
    for i in range(len(vector)):
        output[i] = scalar * vector[i] # scalaing a vector
    return output

def neural_network(input, weights):
    pred = scalar_mul(input, weights)
    return pred

# data set
wl_rec = np.array([0.65, 0.8, 0.8, 0.9])  # team win loss percentage
input = wl_rec[0] # our single input
print("hurt,   win,   sad")
pred = neural_network(input, weights)

print(pred)
