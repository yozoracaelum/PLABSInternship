# Neural Network
import math
import numpy as np
import matplotlib.pyplot as plt
'''
Activation Function
'''
# Linear Activation Function
# phi(x) = x
def la(x):
    return x
# Step Activation Function
''' 
    phi(x) = 1, if x >= 0.5, 0, otherwise
'''
def sa(x):
    if x >= 0.5:
        return 1
    else:
        return 0
# Sigmoid Activation Function
'''
    phi(x) = 1/1+e^-x
'''
def sigmoid(x):
    return 1/(1+np.exp(-x))
# Hyperbolic Tangent Function
'''
    phi(x) = tanh(x)
'''
def ht(x):
    return np.tanh(x)
# Rectified Linear Unit (ReLU)
'''
    phi(x) = max(0,x)
'''
def relu(x):
    return max(0.0,x)
# The Softmax Function
'''
    phi[i] = e^zi/sigma(e^zj,j element group)
'''
def softmax(neuron_output):
    sm = 0
    for v in neuron_output:
        sm += v
    sm =  math.exp(sm)
    proba = []
    for i in range(len(neuron_output)):
        pb = math.exp(neuron_output[i])/sm
        proba.append(pb)
    return proba
# Single-Input NN
'''
    f(x,w,b) = 1/(1+exp(-(wx+b)))
'''
def singleinput(x,w,b):
    return 1/(1+np.exp(-(w*x+b)))
# Hopfield Energy
'''
    E = - (sigma(wij*si*sj,i<j)+sigma(thetai*si,i))
'''
def energy(weights,state,threshold,neuron_count):
    # First term
    a = 0
    for i in range(neuron_count):
        for j in range(neuron_count):
            a += weights[i][j] * state[i] * state[j]
    a *= -0.5
    # Second term
    b = 0
    for i in range(neuron_count):
        b += state[i] * threshold[i]
    # Result
    return a + b
# Hopfield Hebbian Learning
'''
    wij = 1/n * sigma(e^ui*e^uj, u=1 -> n)
'''
def hopfieldHebbian(weights,pattern,n,neuron_count):
    for i in range(neuron_count):
        for j in range(neuron_count):
            if i==j:
                weights[i][j] = 0
            else:
                weights[i][j] = weights[i][j] + ((pattern[i]*pattern[j])/n)
# Hopfield Storkey Local Field
'''
    hij = sigma(wik*ek, k=1, k!=i,j)
'''
def hopfieldStorkey(weights, i, j, pattern):
    sm = 0
    for k in range(len(pattern)):
        if k != i:
            sm += weights[i][k] * pattern[k]
    return sm
#-----------------------#
x = np.arange(-4,4+0.1,0.1)
y1 = [singleinput(i,1.0,1.0) for i in x]
y2 = [singleinput(i,1.0,0.5) for i in x]
y3 = [singleinput(i,1.0,1.5) for i in x]
y4 = [singleinput(i,1.0,2.0) for i in x]
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#-----------------------#