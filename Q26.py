import numpy as np

def expectation(t):
    exp_x=0
    exp_y=0
    for i in range(1, np.size(t, 0)):
        exp_x= exp_x + t[i,0] * np.sum(t[i, 1:], axis=1)
    for i in range(1, np.size(t, 1)):
        exp_x= exp_x + t[0,i] * np.sum(t[1:, i], axis=0)
    return exp_x,exp_y



table= np.array([[0, -1, 0, 5], [1, 0.3, 0.3, 0], [2, 0.1, 0.2, 0.1]])
res_x,res_y=expectation(table)
